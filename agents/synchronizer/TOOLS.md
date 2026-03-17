# TOOLS.md - Synchronizer

## Ferramentas Disponíveis

### 1. ticktick_add_task
**Descrição:** Criar nova tarefa no TickTick  
**Uso:** `ticktick_add_task(name: string, date: string, project_id: string, priority: string, tags: list)`  
**Quando usar:**
- Transformar mensagens em tarefas
- Criar ações a partir de conversas
- Registrar compromissos

**Exemplo:**
```python
ticktick_add_task(
  name="Revisar endpoint de autenticação",
  date="2025-03-18T15:00:00-03:00",
  project_id="p_WappTV",
  priority="high",
  tags=["revisão", "backend", "auth"]
)
```

---

### 2. ticktick_get_today
**Descrição:** Recuperar tarefas do dia  
**Uso:** `ticktick_get_today()`  
**Quando usar:**
- Gerar sumário matinal
- Responder "o que tenho hoje?"
- Verificar agenda antes de agendar novo item

**Exemplo:**
```python
ticktick_get_today()
```

---

### 3. ticktick_get_project_tasks
**Descrição:** Ler tarefas de projeto específico  
**Uso:** `ticktick_get_project_tasks(project_id: string, status: string = "all")`  
**Quando usar:**
- Análise de projeto
- Relatório de status
- Planejamento

**Exemplo:**
```python
ticktick_get_project_tasks(
  project_id="p_WappTV",
  status="pending"
)
```

---

### 4. ticktick_complete_task
**Descrição:** Marcar tarefa como concluída  
**Uso:** `ticktick_complete_task(task_id: string, confirm: bool = true)`  
**Quando usar:**
- Após confirmação do usuário
- Tarefas automatizadas completadas

**⚠️ IMPORTANTE:** Sempre confirme com usuário antes de completar!

**Exemplo:**
```python
ticktick_complete_task(
  task_id="123456789",
  confirm=True  # Verificar se usuário confirmou
)
```

---

### 5. ticktick_read_summary
**Descrição:** Gerar resumo de projeto  
**Uso:** `ticktick_read_summary(project_name: string, period: string = "week")`  
**Quando usar:**
- Relatórios de status
- Análise de progresso
- Planejamento estratégico

**Exemplo:**
```python
ticktick_read_summary(
  project_name="WappTV",
  period="week"
)
```

---

### 6. openviking_write
**Descrição:** Salvar nota de contexto no Obsidian  
**Uso:** `openviking_write(path: string, content: string)`  
**Quando usar:**
- Backup de contexto de tarefas
- Salvar decisões relacionadas
- Manter histórico no Obsidian

**Exemplo:**
```python
openviking_write(
  path="/01-Inbox/20250317120000-tarefa-revisao.md",
  content="# Contexto: Revisão de endpoint..."
)
```

---

### 7. date_parser
**Descrição:** Interpretar datas em linguagem natural  
**Uso:** `date_parser(text: string, timezone: string = "America/Sao_Paulo")`  
**Quando usar:**
- Converter "amanhã" em data absoluta
- Interpretar "próxima segunda"
- Normalizar datas do usuário

**Exemplo:**
```python
date_parser("amanhã à tarde")
# Retorna: "2025-03-18T15:00:00-03:00"

date_parser("próxima segunda-feira")
# Retorna: "2025-03-24T09:00:00-03:00"
```

---

## Workflow Padrão

### Criar Tarefa de Mensagem
```
1. Receber intenção do Orchestrator
2. Analisar: ação, projeto, data, prioridade
3. Usar date_parser para normalizar data
4. Chamar ticktick_add_task
5. Salvar contexto via openviking_write
6. Retornar confirmação ao Orchestrator
```

### Sumário Matinal (Cron)
```
1. Executar às 07:00
2. Chamar ticktick_get_today()
3. Consultar contexto do usuário no Obsidian
4. Gerar resumo em linguagem natural
5. Retornar ao Orchestrator para envio ao usuário
```

### Consultar Projeto
```
1. Receber request de análise
2. Identificar project_id
3. Chamar ticktick_get_project_tasks
4. Formatar lista de tarefas
5. Retornar estruturado
```

## Mapeamento de Projetos

| Nome do Projeto | ID TickTick | Descrição |
|-----------------|-------------|-----------|
| WappTV | p_WappTV | Aplicativo streaming |
| VOLTZ | p_VOLTZ | Plataforma serviços |
| DEK | p_DEK | Projeto adicional |
| Pessoal | p_Pessoal | Tarefas pessoais |
| Maestro | p_Maestro | Este sistema |

## Interpretação de Datas

### Padrões Suportados
- "hoje" → Data atual, hora padrão
- "amanhã" → +1 dia
- "depois de amanhã" → +2 dias
- "próxima [dia da semana]" → Próxima ocorrência
- "daqui a [N] dias" → +N dias
- "esta semana" → Próximo dia útil
- "próxima semana" → Segunda da próxima semana
- "em [N] semanas" → +N semanas

### Hora Padrão
- "manhã" → 09:00
- "tarde" → 15:00
- "fim de tarde" → 17:00
- "noite" → 19:00
- Sem especificação → 09:00

## Estrutura de Backup no Obsidian

### Pasta: /01-Inbox/
- Notas rápidas sobre tarefas criadas
- Contexto capturado
- Formato atômico

### Template
```markdown
---
id: "YYYYMMDDHHMMSS"
date_created: "YYYY-MM-DD"
tags: ["tarefa", "ticktick", "projeto"]
---

# Contexto: [Nome da Tarefa]

## Tarefa Criada
- **Nome:** [nome]
- **Data:** [data]
- **Projeto:** [projeto]
- **Priority:** [priority]
- **TickTick ID:** [id]

## Contexto Original
[Texto original da mensagem/intenção]

## Notas
[Adicionais se necessário]
```

## Fallbacks

- Se TickTick API falhar: salvar apenas no Obsidian e notificar
- Se date_parser ambíguo: confirmar com usuário
- Se projeto não encontrado: usar "p_Pessoal" como padrão
- Se openviking_write falhar: tarefa criada, mas sem backup

## Sincronização Bidirecional

### Obsidian → TickTick
- Tarefas criadas no Obsidian com tag `#ticktick` são sincronizadas
- Padrão YAML com `ticktick: true` dispara criação

### TickTick → Obsidian
- Tarefas completadas são registradas no Obsidian
- Contexto é atualizado automaticamente
