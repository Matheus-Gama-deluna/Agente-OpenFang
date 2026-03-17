# TOOLS.md - Archivist

## Ferramentas Disponíveis

### 1. openviking_write
**Descrição:** Escrever notas na base de conhecimento  
**Uso:** `openviking_write(path: string, content: string, metadata: dict)`  
**Quando usar:**
- Salvar notas Zettelkasten formatadas
- Persistir conhecimento processado
- Criar entradas no vault

**Exemplo:**
```python
openviking_write(
  path="/03-Zettelkasten/20250317120000-arquitetura-api.md",
  content="# Decisão Arquitetural...",
  metadata={
    "id": "20250317120000",
    "tags": ["arquitetura", "api"],
    "related": ["20250316110000"]
  }
)
```

---

### 2. openviking_merge_knowledge
**Descrição:** Fazer merge de informações duplicadas  
**Uso:** `openviking_merge_knowledge(existing_id: string, new_content: string)`  
**Quando usar:**
- Quando detectar nota similar existente
- Atualizar nota com nova informação
- Evitar duplicatas

**Exemplo:**
```python
openviking_merge_knowledge(
  existing_id="20250316110000",
  new_content="Nova informação sobre o tópico"
)
```

---

### 3. openviking_search
**Descrição:** Buscar na base de conhecimento  
**Uso:** `openviking_search(query: string, namespace: string = "all")`  
**Quando usar:**
- Verificar duplicatas antes de criar
- Encontrar notas relacionadas para linkar
- Recuperar contexto

**Exemplo:**
```python
openviking_search(
  query="decisão arquitetural WappTV",
  namespace="03-Zettelkasten"
)
```

---

### 4. json_formatter
**Descrição:** Format estruturas JSON  
**Uso:** `json_formatter(data: any, indent: int = 2)`  
**Quando usar:**
- Formatar metadados
- Estruturar dados de saída
- Validar JSON

---

### 5. yaml_generator
**Descrição:** Criar YAML frontmatter  
**Uso:** `yaml_generator(data: dict)`  
**Quando usar:**
- Gerar YAML frontmatter para notas
- Criar metadados estruturados
- Format headers de markdown

**Exemplo:**
```python
yaml_generator({
  "id": "20250317120000",
  "title": "Decisão Arquitetural",
  "date_created": "2025-03-17",
  "tags": ["arquitetura", "api"]
})
```

---

### 6. embedding_generator
**Descrição:** Gerar vetores para busca semântica  
**Uso:** `embedding_generator(text: string, model: string = "nomic-embed-text")`  
**Quando usar:**
- Criar embeddings para notas
- Habilitar busca vetorial
- Indexar conhecimento

---

## Workflow Padrão

```
1. Receber resumo do Orchestrator
2. Analisar conteúdo para extrair fatos valiosos
3. Buscar duplicatas (openviking_search)
4. Se duplicata encontrada → merge
5. Se nova → formatar como Zettelkasten
6. Criar YAML frontmatter
7. Definir pasta apropriada (/01-Inbox/, /02-Projetos/, /03-Zettelkasten/)
8. Buscar notas relacionadas para linkar
9. Escrever via openviking_write
10. Retornar ID ao Orchestrator
```

## Estrutura de Pastas

### 01-Inbox/
- Ideias cruas
- Capturas rápidas
- Processamento inicial

### 02-Projetos/
- Notas temporárias
- Vinculadas a projetos ativos
- Associadas a tarefas TickTick

### 03-Zettelkasten/
- Conhecimento permanente
- Notas atômicas
- Bem linkadas
- Com metadados completos

### 99-Config/
- Preferências do usuário
- Configurações de sistema
- Personal Operating Procedures

## Sequência de Processamento

1. **Recebimento** → Resumo de interação
2. **Análise** → Extrair fatos, decisões, ideias
3. **Deduplicação** → Verificar existência
4. **Formatação** → Zettelkasten + YAML
5. **Linkagem** → Identificar conexões
6. **Persistência** → Salvar no vault
7. **Indexação** → Gerar embeddings

## Padrões de Linkagem

### Criar Links Bidirecionais
```markdown
Nota A:
## Ligações
- [[20250316110000]] - decisão relacionada

Nota B:
## Ligações
- [[20250317120000]] - contexto da decisão
```

### Tags para Conexão
- Usar tags consistentes
- Incluir ano ("2024", "2025")
- Incluir contexto ("arquitetura", "wapp-tv")
- Incluir tipo ("decisão", "bug", "feature")
