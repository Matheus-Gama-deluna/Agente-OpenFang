#!/usr/bin/env python3
"""
vault_ops.py - Utilitários de vault Obsidian para OpenFang
Usado pelos hands via shell_exec para operações que requerem
processamento local (YAML frontmatter, busca vetorial, etc.)

Uso:
  python vault_ops.py frontmatter <note_path>
  python vault_ops.py progress <note_path>
  python vault_ops.py stale [--days N] [--folder PATH]
  python vault_ops.py search <query> [--top-k N] [--threshold F] [--vault PATH]
  python vault_ops.py reindex [--vault PATH] [--ollama URL] [--model MODEL]
  python vault_ops.py find_duplicates [--threshold F] [--folder PATH]
  python vault_ops.py update_frontmatter <note_path> <key> <value>

Dependências:
  pip install pyyaml numpy requests
  Opcional (para busca vetorial): pip install numpy
  Ollama rodando em http://localhost:11434 com nomic-embed-text instalado
"""

import sys
import json
import os
import re
import argparse
import datetime

try:
    import yaml
except ImportError:
    print("ERRO: pyyaml não instalado. Execute: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


# ─────────────────────────────────────────────────────────────────────────────
# UTILITÁRIOS DE FRONTMATTER
# ─────────────────────────────────────────────────────────────────────────────

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extrai YAML frontmatter e corpo de uma nota Markdown."""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
                return fm, body
            except yaml.YAMLError:
                pass
    return {}, content


def write_frontmatter(frontmatter: dict, body: str) -> str:
    """Serializa frontmatter e corpo de volta para Markdown."""
    fm_str = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False)
    return f"---\n{fm_str}---\n\n{body}"


def cmd_frontmatter(args):
    """Extrai e imprime o frontmatter de uma nota."""
    path = os.path.expandvars(args.note_path)
    if not os.path.exists(path):
        print(json.dumps({"error": f"Arquivo não encontrado: {path}"}))
        return 1

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    fm, _ = parse_frontmatter(content)
    print(json.dumps(fm, ensure_ascii=False, indent=2, default=str))
    return 0


def cmd_update_frontmatter(args):
    """Atualiza um campo do frontmatter de uma nota."""
    path = os.path.expandvars(args.note_path)
    if not os.path.exists(path):
        print(json.dumps({"error": f"Arquivo não encontrado: {path}"}))
        return 1

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    fm, body = parse_frontmatter(content)

    # Tentar parsear o valor para tipo correto
    value = args.value
    if value.lower() in ("true", "false"):
        value = value.lower() == "true"
    elif value.isdigit():
        value = int(value)
    else:
        try:
            value = float(value)
        except ValueError:
            pass  # mantém como string

    fm[args.key] = value
    fm["updated_at"] = datetime.datetime.now().astimezone().isoformat()

    new_content = write_frontmatter(fm, body)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(json.dumps({"success": True, "key": args.key, "value": value}))
    return 0


# ─────────────────────────────────────────────────────────────────────────────
# CÁLCULO DE PROGRESSO
# ─────────────────────────────────────────────────────────────────────────────

def cmd_progress(args):
    """Calcula o progresso de um projeto (% de checkboxes marcados)."""
    path = os.path.expandvars(args.note_path)
    if not os.path.exists(path):
        print(json.dumps({"error": f"Arquivo não encontrado: {path}"}))
        return 1

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    fm, body = parse_frontmatter(content)

    # Contar checkboxes
    total = len(re.findall(r"- \[[ x]\]", body))
    done = len(re.findall(r"- \[x\]", body, re.IGNORECASE))
    percent = round((done / total * 100) if total > 0 else 0)

    result = {
        "note": path,
        "actions_total": total,
        "actions_done": done,
        "progress_percent": percent,
        "status": fm.get("status", "unknown"),
        "outcome": fm.get("outcome", ""),
        "next_action": fm.get("next_action", ""),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


# ─────────────────────────────────────────────────────────────────────────────
# DETECÇÃO DE PROJETOS/NOTAS STALE
# ─────────────────────────────────────────────────────────────────────────────

def cmd_stale(args):
    """Lista notas/projetos que não foram atualizados recentemente."""
    folder = os.path.expandvars(args.folder)
    threshold_days = args.days
    cutoff = datetime.datetime.now().astimezone() - datetime.timedelta(days=threshold_days)

    stale_notes = []
    healthy_notes = []

    for fname in os.listdir(folder):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(folder, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        fm, _ = parse_frontmatter(content)
        status = fm.get("status", "")
        if status in ("completed", "archived"):
            continue

        updated_at = fm.get("updated_at") or fm.get("date_modified")
        days_stale = None
        if updated_at:
            try:
                dt = datetime.datetime.fromisoformat(str(updated_at))
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=datetime.timezone.utc)
                days_stale = (datetime.datetime.now().astimezone() - dt).days
            except (ValueError, TypeError):
                pass

        note_info = {
            "path": fpath,
            "name": fname,
            "status": status,
            "days_since_update": days_stale,
            "outcome": fm.get("outcome", ""),
            "next_action": fm.get("next_action", ""),
        }

        if days_stale is None or days_stale > threshold_days:
            stale_notes.append(note_info)
        else:
            healthy_notes.append(note_info)

    result = {
        "stale_count": len(stale_notes),
        "healthy_count": len(healthy_notes),
        "threshold_days": threshold_days,
        "stale": sorted(stale_notes, key=lambda x: x["days_since_update"] or 9999, reverse=True),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


# ─────────────────────────────────────────────────────────────────────────────
# BUSCA VETORIAL (requer numpy + Ollama)
# ─────────────────────────────────────────────────────────────────────────────

def get_embedding(text: str, ollama_url: str, model: str) -> list[float] | None:
    """Gera embedding via Ollama API."""
    if not REQUESTS_AVAILABLE:
        print("ERRO: requests não instalado. Execute: pip install requests", file=sys.stderr)
        return None
    try:
        resp = requests.post(
            f"{ollama_url}/api/embed",
            json={"model": model, "input": text},
            timeout=10
        )
        resp.raise_for_status()
        data = resp.json()
        # Ollama retorna {"embeddings": [[...]]} ou {"embedding": [...]}
        if "embeddings" in data:
            return data["embeddings"][0]
        return data.get("embedding")
    except Exception as e:
        print(f"ERRO ao obter embedding: {e}", file=sys.stderr)
        return None


def cosine_similarity(a: list, b: list) -> float:
    """Calcula similaridade de cosseno entre dois vetores."""
    if not NUMPY_AVAILABLE:
        # Fallback sem numpy
        dot = sum(x * y for x, y in zip(a, b))
        mag_a = sum(x ** 2 for x in a) ** 0.5
        mag_b = sum(x ** 2 for x in b) ** 0.5
        return dot / (mag_a * mag_b) if (mag_a * mag_b) > 0 else 0.0
    a_arr, b_arr = np.array(a), np.array(b)
    return float(np.dot(a_arr, b_arr) / (np.linalg.norm(a_arr) * np.linalg.norm(b_arr)))


def load_index(index_path: str) -> dict:
    """Carrega índice vetorial do disco."""
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"notes": [], "indexed_at": None}


def save_index(index: dict, index_path: str):
    """Salva índice vetorial no disco."""
    os.makedirs(os.path.dirname(index_path), exist_ok=True)
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False)


def cmd_reindex(args):
    """Indexa todas as notas do vault via Ollama."""
    vault_path = os.path.expandvars(args.vault)
    index_path = os.path.expandvars(args.index)
    ollama_url = args.ollama
    model = args.model

    index = load_index(index_path)
    indexed = []
    errors = []

    for root, _, files in os.walk(vault_path):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                fm, body = parse_frontmatter(content)
                # Texto para embedding: título + corpo (sem frontmatter)
                title = fm.get("title") or os.path.splitext(fname)[0]
                text = f"{title}\n\n{body[:2000]}"  # limitar para 2000 chars
                embedding = get_embedding(text, ollama_url, model)
                if embedding is None:
                    raise ValueError("Embedding retornou None")
                indexed.append({
                    "path": fpath,
                    "title": title,
                    "tags": fm.get("tags", []),
                    "embedding": embedding,
                })
            except Exception as e:
                errors.append({"path": fpath, "error": str(e)})

    index["notes"] = indexed
    index["indexed_at"] = datetime.datetime.now().isoformat()
    index["total"] = len(indexed)
    save_index(index, index_path)

    print(json.dumps({
        "indexed": len(indexed),
        "errors": len(errors),
        "index_path": index_path,
        "error_details": errors[:5],  # mostrar apenas 5 primeiros erros
    }, ensure_ascii=False, indent=2))
    return 0


def cmd_search(args):
    """Busca semântica no vault via similaridade de cosseno."""
    index_path = os.path.expandvars(args.index)
    index = load_index(index_path)

    if not index["notes"]:
        print(json.dumps({"error": "Índice vazio. Execute: python vault_ops.py reindex"}))
        return 1

    query_embedding = get_embedding(args.query, args.ollama, args.model)
    if query_embedding is None:
        print(json.dumps({"error": "Não foi possível gerar embedding da query. Ollama disponível?"}))
        return 1

    results = []
    for note in index["notes"]:
        score = cosine_similarity(query_embedding, note["embedding"])
        if score >= args.threshold:
            results.append({
                "path": note["path"],
                "title": note["title"],
                "score": round(score, 4),
                "tags": note.get("tags", []),
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    results = results[:args.top_k]

    print(json.dumps({
        "query": args.query,
        "results": results,
        "total_found": len(results),
    }, ensure_ascii=False, indent=2))
    return 0


def cmd_find_duplicates(args):
    """Detecta notas com conteúdo muito similar."""
    index_path = os.path.expandvars(args.index)
    index = load_index(index_path)

    if not index["notes"]:
        print(json.dumps({"error": "Índice vazio. Execute: python vault_ops.py reindex"}))
        return 1

    duplicates = []
    notes = index["notes"]
    for i, note_a in enumerate(notes):
        for note_b in notes[i + 1:]:
            score = cosine_similarity(note_a["embedding"], note_b["embedding"])
            if score >= args.threshold:
                duplicates.append({
                    "note_a": note_a["path"],
                    "note_b": note_b["path"],
                    "similarity": round(score, 4),
                })

    print(json.dumps({
        "duplicates_found": len(duplicates),
        "threshold": args.threshold,
        "duplicates": sorted(duplicates, key=lambda x: x["similarity"], reverse=True),
    }, ensure_ascii=False, indent=2))
    return 0


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Utilitários de vault Obsidian para OpenFang")
    subparsers = parser.add_subparsers(dest="command")

    # frontmatter
    p_fm = subparsers.add_parser("frontmatter", help="Extrair frontmatter de uma nota")
    p_fm.add_argument("note_path")

    # update_frontmatter
    p_ufm = subparsers.add_parser("update_frontmatter", help="Atualizar campo do frontmatter")
    p_ufm.add_argument("note_path")
    p_ufm.add_argument("key")
    p_ufm.add_argument("value")

    # progress
    p_prog = subparsers.add_parser("progress", help="Calcular progresso de um projeto")
    p_prog.add_argument("note_path")

    # stale
    p_stale = subparsers.add_parser("stale", help="Listar notas stale")
    p_stale.add_argument("--days", type=int, default=7)
    p_stale.add_argument("--folder", default="/data/obsidian_vault/02-Projects")

    # reindex
    p_reindex = subparsers.add_parser("reindex", help="Indexar vault com embeddings")
    p_reindex.add_argument("--vault", default="/data/obsidian_vault")
    p_reindex.add_argument("--ollama", default="http://localhost:11434")
    p_reindex.add_argument("--model", default="nomic-embed-text")
    p_reindex.add_argument("--index", default="/data/openfang/obsidian_index/index.json")

    # search
    p_search = subparsers.add_parser("search", help="Busca semântica no vault")
    p_search.add_argument("query")
    p_search.add_argument("--top-k", type=int, default=5, dest="top_k")
    p_search.add_argument("--threshold", type=float, default=0.70)
    p_search.add_argument("--ollama", default="http://localhost:11434")
    p_search.add_argument("--model", default="nomic-embed-text")
    p_search.add_argument("--index", default="/data/openfang/obsidian_index/index.json")

    # find_duplicates
    p_dup = subparsers.add_parser("find_duplicates", help="Detectar notas duplicadas")
    p_dup.add_argument("--threshold", type=float, default=0.95)
    p_dup.add_argument("--index", default="/data/openfang/obsidian_index/index.json")

    args = parser.parse_args()

    if args.command == "frontmatter":
        sys.exit(cmd_frontmatter(args))
    elif args.command == "update_frontmatter":
        sys.exit(cmd_update_frontmatter(args))
    elif args.command == "progress":
        sys.exit(cmd_progress(args))
    elif args.command == "stale":
        sys.exit(cmd_stale(args))
    elif args.command == "reindex":
        sys.exit(cmd_reindex(args))
    elif args.command == "search":
        sys.exit(cmd_search(args))
    elif args.command == "find_duplicates":
        sys.exit(cmd_find_duplicates(args))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
