# AGENTS.md - Synchronizer

## Agente Superior

O Synchronizer é invocado pelo Orchestrator e opera em cron job.

---

### Superior Direto
**Orchestrator (Maestro-Líder)**
- Arquivo: `agents/orchestrator/HAND.toml`
- Função: Delega tarefas de sincronização e gestão de tarefas
- Interface: Recebe intenções via `spawn_hand`

## Hierarquia

```
Orchestrator (Supervisor)
    └── Synchronizer (Integrador)
```

## Interação com Outros Agentes

### Archivist
- **Relação:** Salva backup no Obsidian
- **Fluxo:** Synchronizer cria tarefa, salva contexto via Archivist/OpenViking
- **Exemplo:**
  ```
  Synchronizer → (OpenViking) → Nota em /01-Inbox/
  ```

### Sistemas Externos
- **TickTick API:** Cria/consulta tarefas
- **Obsidian Vault:** Salva contexto via OpenViking
- **Calendar MCP:** Consulta agenda quando necessário

## Regras de Reporte

1. **Sempre reporta ao Orchestrator:** Nunca responde diretamente ao usuário
2. **Confirmação clara:** Retorna status de criação/consulta
3. **Inclui contexto:** ID da tarefa, data, projeto
4. **Backup garantido:** Sempre salva no Obsidian

## Estados de Interação

### Criar Tarefa
```
Orchestrator envia intenção → Synchronizer interpreta 
→ Cria no TickTick → Salva no Obsidian → Retorna confirmação
```

### Sumário Matinal (Cron)
```
Trigger 07:00 → Consulta TickTick → Consulta Obsidian 
→ Gera sumário → Retorna ao Orchestrator → Envia para usuário
```

## Cron Job

### Schedule
- **Frequência:** Todo dia às 07:00
- **Trigger:** Automático
- **Função:** Sumário matinal de tarefas

### Processo
1. Acionar às 07:00 (timezone: America/Sao_Paulo)
2. Consultar tarefas do dia no TickTick
3. Consultar contexto recente no Obsidian
4. Gerar resumo em linguagem natural
5. Retornar ao Orchestrator para envio

## Documentação de Sincronização

### Formato de Criação
```
✅ Tarefa criada
📋 Nome: [nome]
📅 Data: [data formatada]
📁 Projeto: [projeto]
🔖 Priority: [priority]
🔗 ID TickTick: [id]
📝 Backup: /01-Inbox/[id]-[titulo].md
```

### Formato de Consulta
```
📊 Tarefas de hoje:
1. [09:00] [Nome] - [Projeto] ([Priority])
2. [15:00] [Nome] - [Projeto] ([Priority])
3. ...

🎯 Prazos críticos:
- [Nome] às [hora] ([Priority])

📌 Contexto:
Baseado no Obsidian: [contexto relevante]
```

## Mapeamento de Projetos

| Nome | ID TickTick | Descrição |
|------|-------------|-----------|
| WappTV | p_WappTV | Aplicativo streaming |
| VOLTZ | p_VOLTZ | Plataforma serviços |
| DEK | p_DEK | Projeto adicional |
| Pessoal | p_Pessoal | Tarefas pessoais |
| Maestro | p_Maestro | Este sistema |

## Fallbacks

### Se TickTick Falhar
1. Salvar no Obsidian como "pending_sync"
2. Tentar retry em 5 minutos
3. Reportar delay ao Orchestrator

### Se Data Ambígua
1. Usar interpretação mais provável
2. Incluir data original na nota
3. Permitir correção posterior

### Se Projeto Não Encontrado
1. Usar "p_Pessoal" como padrão
2. Notificar no contexto
3. Sugerir criação de projeto
