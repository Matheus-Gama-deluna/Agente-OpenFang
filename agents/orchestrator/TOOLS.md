# TOOLS.md - Orchestrator

## Ferramentas Disponíveis

### 1. openviking_read_abstract
**Descrição:** Lê resumos da base de conhecimento OpenViking  
**Uso:** `openviking_read_abstract(query: string, limit: int = 5)`  
**Quando usar:**
- Antes de tomar decisões, para verificar contexto histórico
- Para recuperar informações do Zettelkasten
- Para consultar preferências do usuário

**Exemplo:**
```
openviking_read_abstract("preferências usuário projetos")
```

---

### 2. spawn_hand
**Descrição:** Cria/aciona um agente especializado  
**Uso:** `spawn_hand(agent_name: string, task: string, context: dict)`  
**Quando usar:**
- Quando a tarefa requer especialização
- Para código complexo → Architect
- Para comandos CLI → Operator
- Para processar conhecimento → Archivist
- Para tarefas TickTick → Synchronizer

**Exemplo:**
```
spawn_hand(
  agent_name="architect",
  task="Analisar arquitetura do WappTV",
  context={"repository": "wapp-tv-api", "focus": "performance"}
)
```

---

### 3. mcp_calendar_read
**Descrição:** Consulta agenda/calendário do usuário  
**Uso:** `mcp_calendar_read(date_range: string, event_type: string = "all")`  
**Quando usar:**
- Antes de agendar algo novo
- Para verificar disponibilidade
- Para criar resumos matinais

**Exemplo:**
```
mcp_calendar_read("2025-03-17", "meetings")
```

---

### 4. web_search
**Descrição:** Busca dados atualizados na web  
**Uso:** `web_search(query: string, num_results: int = 5)`  
**Quando usar:**
- ANTES de confirmar qualquer fato, data, número
- Para verificar informações atualizadas
- Para encontrar documentação atual

**Exemplo:**
```
web_search("última versão OpenFang framework 2025")
```

**⚠️ IMPORTANTE:** Sempre use web_search antes de confirmar fatos!

---

### 5. ticktick_add_task
**Descrição:** Cria nova tarefa no TickTick  
**Uso:** `ticktick_add_task(name: string, date: string, project_id: string, priority: string)`  
**Quando usar:**
- Quando usuário pede para "lembrar" algo
- Para criar ações a partir de conversas
- Para delegar ao Synchronizer (preferencial)

**Exemplo:**
```
ticktick_add_task(
  name="Revisar código do endpoint",
  date="2025-03-18T15:00:00-03:00",
  project_id="p_WappTV",
  priority="high"
)
```

---

### 6. ticktick_get_today
**Descrição:** Recupera tarefas do dia  
**Uso:** `ticktick_get_today()`  
**Quando usar:**
- Para sumário matinal
- Para verificar agenda antes de agendar novo item
- Para responder "o que tenho hoje?"

---

### 7. telegram_send_message
**Descrição:** Envia mensagem via Telegram  
**Uso:** `telegram_send_message(chat_id: string, message: string, format: string = "markdown")`  
**Quando usar:**
- Para responder ao usuário
- Para enviar notificações
- Para reportar status de tarefas

**Exemplo:**
```
telegram_send_message(
  chat_id="user_id",
  message="✅ Tarefa criada com sucesso!"
)
```

## Orquestração de Ferramentas

### Workflow Padrão
1. Recebe request do usuário
2. Usa `openviking_read_abstract` para contexto
3. Se precisa de dados atualizados → `web_search`
4. Decide: resolver ou delegar
5. Se delegar → `spawn_hand` com agente apropriado
6. Retorna resultado ao usuário via `telegram_send_message`

### Fallbacks
- Se `web_search` falhar: informar que dados podem estar desatualizados
- Se `spawn_hand` falhar: tentar resolver localmente ou informar erro
- Se `openviking_read` falhar: operar sem contexto histórico
