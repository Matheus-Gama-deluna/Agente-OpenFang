# MEMORY.md - Synchronizer

## Estrutura de Memória

### Short-Term Memory (Context Window)
**Tipo:** Tarefas sendo criadas/consultadas  
**Retenção:** Duração da sessão  
**Limite:** ~128k tokens  

**O que armazena:**
- Intenção sendo processada
- Datas interpretadas
- Tarefas criadas na sessão
- Resultados de consultas

---

### Long-Term Memory (OpenViking)
**Tipo:** Histórico de sincronizações e contexto de tarefas  
**Retenção:** 90 dias  
**Acesso:** Via `openviking_read/write`  

**O que armazena:**
- Tarefas criadas (contexto e metadados)
- Sincronizações realizadas
- Padrões de agendamento do usuário
- Preferências de projetos

**Namespace:** `synchronizer/tasks`  

---

## Ciclo de Vida da Sincronização

### 1. Recebimento
- Intenção do Orchestrator
- Mensagem do usuário
- Request de sumário

### 2. Interpretação
- Análise de linguagem natural
- Extração de: ação, projeto, data, prioridade
- Normalização de datas

### 3. Execução
- Chamada à API TickTick
- Criação/consulta de tarefa
- Captura de resultado

### 4. Backup
- Salvar contexto no Obsidian
- Criar nota em /01-Inbox/
- Linkar com projeto se relevante

### 5. Retorno
- Resultado ao Orchestrator
- Confirmação de sucesso
- Ou relatório de erro

## Padrões de Armazenamento

### Nota de Contexto (Obsidian)
```markdown
---
id: "YYYYMMDDHHMMSS"
date_created: "YYYY-MM-DD"
tags: ["tarefa", "ticktick", "projeto"]
ticktick_task_id: "123456789"
---

# Contexto: [Nome da Tarefa]

## Tarefa Criada
- **Nome:** [nome]
- **Data:** [data formatada]
- **Projeto:** [projeto]
- **Priority:** [priority]
- **Tags:** [tags]

## Contexto Original
> [Texto original da mensagem]

## Interpretação
- Ação identificada: [ação]
- Data interpretada: [data original → data normalizada]
- Projeto mapeado: [nome → id]

## Criado em
[TIMESTAMP]
```

### Histórico de Sincronização
```json
{
  "sync_id": "sync_001",
  "timestamp": "2025-03-17T12:00:00-03:00",
  "type": "create_task",
  "source": "telegram_message",
  "task": {
    "name": "...",
    "project_id": "p_WappTV",
    "date": "..."
  },
  "obsidian_note": "/01-Inbox/20250317120000-...",
  "status": "success"
}
```

## Retenção

### Sessão Atual
- Intenções sendo processadas
- Tarefas criadas na conversa
- Resultados de consultas

### 90 Dias
- Histórico de tarefas criadas
- Padrões de agendamento
- Preferências de projetos
- Taxa de sucesso de sincronização

### Permanente (via Archivist)
- Decisões sobre integração
- Mudanças em procedimentos
- Documentação de workflows

## Cache de Sistema

### TickTick API
- Lista de projetos: Cache de 1 hora
- Tarefas do dia: Cache de 5 minutos
- Estrutura de projetos: Cache de 24 horas

### Date Parser
- Padrões de data comuns: Cache de sessão
- Fuso horário: Cache permanente (Brasília)

### OpenViking
- Notas de contexto recentes: Cache de 10 minutos
- Estrutura de pastas: Cache de 1 hora

## Recuperação

### Se TickTick Falhar
1. Salvar no Obsidian como "pending_sync"
2. Tentar retry em 5 minutos
3. Notificar Orchestrator do delay
4. Marcar para sincronização manual posterior

### Se Data for Ambígua
1. Registrar interpretação escolhida
2. Incluir data original na nota
3. Permitir correção pelo usuário
4. Aprender para próximas interpretações

## Padrões de Usuário

### Aprendizado
- Horários preferidos de tarefas
- Frequência de projetos
- Padrões de priorização
- Estilo de nomenclatura

### Adaptação
- Sugerir horários baseados em histórico
- Propor projetos baseados em contexto
- Antecipar padrões de recorrência

## Namespace Específico

```
synchronizer/
├── tasks/              # Histórico de tarefas
├── patterns/          # Padrões de usuário
├── projects/          # Cache de projetos
└── sync_logs/         # Logs de sincronização
```
