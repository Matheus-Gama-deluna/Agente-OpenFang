# TOOLS.md - Orchestrator

## Ferramentas Disponíveis

### 1. hand_spawn
**Descrição:** Cria/aciona um hand especializado (Produtividade)
**Uso:** `hand_spawn(hand_id: string, payload: dict)`  
**Quando usar:**
- Quando a intenção for de produtividade ou captura (inbox-collector, gtd-processor, project-manager)
- Para acessar a memória vetorial de longo prazo (obsidian-bridge)
- Quando a tarefa envolver gestão de vida pessoal

**Exemplo:**
```
hand_spawn(
  hand_id="obsidian-bridge",
  payload={"action": "search", "query": "projetos WappTV ativos"}
)
```

---

### 2. agent_spawn
**Descrição:** Cria/aciona um agente técnico
**Uso:** `agent_spawn(agent_name: string, task: string, context: dict)`  
**Quando usar:**
- Quando a tarefa requer especialização de engenharia
- Para arquitetura de código → Architect
- Para operações de CLI/rede → Operator
- Para processar anotações em Zettelkasten → Archivist

**Exemplo:**
```
agent_spawn(
  agent_name="architect",
  task="Analisar arquitetura do repositório OpenFang",
  context={"focus": "performance e caching"}
)
```

---

### 3. web_fetch (antigo web_search)
**Descrição:** Busca dados e conteúdo via URL ou API (Mecanismo nativo OpenFang)
**Uso:** `web_fetch(url: string)`  
**Quando usar:**
- ANTES de confirmar qualquer fato técnico temporal
- Para verificar informações atualizadas
- Para acessar documentações online

**⚠️ IMPORTANTE:** Sempre verifique a precisão de afirmações categóricas.

---

### 4. agent_send / hand_message
**Descrição:** Envia mensagens para agentes ou hands já em execução 
**Quando usar:**
- Para não criar um novo processo via `spawn_hand` ou `agent_spawn` caso o agente alvo já esteja vivo e agendado.

---

### Workflow Padrão
1. Recebe request do usuário
2. Analisa a intenção cruzando com `AGENTS.md`
3. Se precisa de dados históricos/referências → `hand_spawn` -> `obsidian-bridge` (action="search")
4. Decide: resolver no local ou delegar a um especialista
5. Se delegar → `hand_spawn` (produtividade) ou `agent_spawn` (técnico)
6. Retorna resultado ao usuário

### Fallbacks
- Se o hand especializado falhar: informar que e tentar repassar o erro contextualizado
- Se `web_fetch` falhar: atuar baseado em conhecimento intrínseco e declarar a data de corte
- Se o `obsidian-bridge` falhar (Ollama desligado): operar sem contexto de longo prazo

## Orquestração de Ferramentas

