# MEMORY.md - Archivist

## Estrutura de Memória

### Short-Term Memory (Context Window)
**Tipo:** Resumo sendo processado atualmente  
**Retenção:** Duração do processamento  
**Limite:** ~128k tokens  

**O que armazena:**
- Resumo recebido do Orchestrator
- Nota sendo formatada
- Metadados em construção
- Links identificados

---

### Long-Term Memory (OpenViking)
**Tipo:** Base de conhecimento persistente  
**Retenção:** Permanente  
**Acesso:** Via ferramentas openviking_*  

**O que armazena:**
- Todas as notas Zettelkasten criadas
- Índices de busca semântica
- Metadados de notas
- Relações entre notas

**Namespaces:**
- `/01-Inbox/` - Ideias cruas
- `/02-Projetos/` - Notas de projetos
- `/03-Zettelkasten/` - Conhecimento permanente
- `/99-Config/` - Configurações

---

## Ciclo de Vida do Conhecimento

### 1. Captura (via Orchestrator)
- Resumo de interação enviado
- Fato/ideia/decisão identificada
- Contexto mantido em short-term

### 2. Processamento
- Análise do conteúdo
- Extração de valor
- Formatação Zettelkasten
- Criação de metadados

### 3. Deduplicação
- Busca por notas similares
- Se encontrada → merge
- Se nova → prosseguir

### 4. Persistência
- Escrita no OpenViking
- Geração de embeddings
- Criação de links
- Indexação para busca

### 5. Recuperação
- Notas disponíveis para outros agentes
- Busca semântica habilitada
- Contexto histórico acessível

## Padrões de Armazenamento

### Nota Zettelkasten
```markdown
---
id: "YYYYMMDDHHMMSS"
title: "Título da Nota"
date_created: "YYYY-MM-DD"
date_modified: "YYYY-MM-DD"
tags: ["tag1", "tag2", "contexto"]
source: "origem"
author: "Arquivista"
related: ["id1", "id2", "id3"]
---

# Título da Nota

## Resumo
2-3 frases com ideia central

## Contexto
De onde/how/when surgiu

## Conteúdo
Ideia atômica, auto-contida

## Ligações
- [[id1]] - relação específica
- [[id2]] - outra relação

## Referências
- Fontes
- Links
```

### Pasta Determinada por:
- **01-Inbox:** Ideias cruas, processamento inicial
- **02-Projetos:** Associadas a projetos ativos
- **03-Zettelkasten:** Conhecimento permanente
- **99-Config:** Preferências e configs

## Sistema de Links

### Bidirecional
```
Nota A → [[id-B]]
Nota B → [[id-A]]
```

### Tags Consistentes
- Ano: "2025", "2024"
- Projeto: "wapp-tv", "voltz", "dek", "maestro"
- Tipo: "decisão", "bug", "feature", "arquitetura"
- Domínio: "backend", "frontend", "infra", "design"

## Retenção

### Permanente (Tudo)
- Todas as notas são retidas para sempre
- Embeddings atualizados periodicamente
- Links mantidos consistentes
- Histórico completo preservado

### Garbage Collection
- Notas órfãs (sem links) são identificadas
- Revisão periódica de qualidade
- Merge de duplicatas
- Reindexação semanal

## Otimização

### Embeddings
- Gerados via Ollama (nomic-embed-text)
- Indexados para busca semântica
- Atualizados quando notas são editadas

### Cache
- Resultados de busca cacheados por 5 min
- Metadados carregados em batch
- Links resolvidos lazy-loading

## Namespace Específico

```
openviking/
├── 01-Inbox/          # Processamento inicial
├── 02-Projetos/       # Temporário
├── 03-Zettelkasten/   # Permanente
│   ├── arquitetura/
│   ├── decisoes/
│   ├── bugs/
│   └── features/
└── 99-Config/         # Configs
    └── user/
        └── preferences.md
```
