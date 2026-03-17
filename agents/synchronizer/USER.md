# USER.md - Synchronizer

## Perfil do Usuário

**Nome:** Matheus Gama de Luna  
**Gerenciador de Tarefas:** TickTick  
**Sistema de Notas:** Obsidian  
**Preferência de Idioma:** Português Brasileiro (pt-BR)  
**Timezone:** America/Sao_Paulo (UTC-3)  

## Projetos no TickTick

| ID | Nome | Descrição |
|----|------|-----------|
| p_WappTV | WappTV | Aplicativo de streaming |
| p_VOLTZ | VOLTZ | Plataforma de serviços |
| p_DEK | DEK | Projeto adicional |
| p_Pessoal | Pessoal | Tarefas pessoais |
| p_Maestro | Maestro System | Este sistema de agentes |

## Interpretação de Datas

### Linguagem Natural → Data Absoluta
- "hoje" → Data atual (HH:00 padrão)
- "amanhã" → Data atual + 1 dia
- "próxima segunda" → Próxima ocorrência de segunda
- "daqui a 3 dias" → Data atual + 3 dias
- "esta semana" → Dentro de 7 dias
- "próximo mês" → Primeiro dia do mês seguinte
- "tarde" → 15:00 (padrão)
- "manhã" → 09:00 (padrão)

### Formato de Data
```
ISO 8601 com timezone: 2025-03-17T15:00:00-03:00
```

## Padrões de Tarefas

### Prioridade
- **High:** Tarefas urgentes, deadlines próximos
- **Medium:** Tarefas normais
- **Low:** Tarefas flexíveis

### Tags Comuns
- `reunião` - Compromissos síncronos
- `revisão` - Code review, análise
- `implementação` - Desenvolvimento
- `documentação` - Docs, ADRs
- `bug` - Correções

## Workflow Preferido

### Captura de Intenção
1. Usuário envia mensagem (áudio ou texto)
2. Orchestrator entende intenção
3. Delega ao Synchronizer
4. Synchronizer cria tarefa estruturada

### Estrutura da Tarefa
```json
{
  "name": "Ação clara e específica",
  "date": "2025-03-17T15:00:00-03:00",
  "project_id": "p_WappTV",
  "priority": "high",
  "tags": ["revisão", "backend"]
}
```

### Backup no Obsidian
- Tarefa criada no TickTick
- Contexto salvo em `/01-Inbox/`
- Formato atômico, linkável

## Sumário Matinal

### Conteúdo (07:00)
1. Tarefas do dia (do TickTick)
2. Prazos críticos
3. Reuniões agendadas
4. Contexto do Obsidian
5. Sugestões proativas

### Formato
```
Bom dia! 🌅

**Hoje você tem:**
- 3 tarefas no projeto WappTV
- 1 reunião às 14h
- 1 deadline para revisão de código

**Contexto:**
Baseado nas suas anotações de ontem sobre [tópico], 
quer que eu prepare algo para a reunião?
```

## Regras Específicas

1. **Claridade:** Nome da tarefa deve ser auto-explicativa
2. **Contexto:** Sempre incluir projeto e prioridade
3. **Backup:** Sempre salvar contexto no Obsidian
4. **Confirmação:** Confirmar antes de completar tarefas
5. **Time Zone:** Sempre usar Brasília UTC-3
6. **Duplicatas:** Verificar existência antes de criar
7. **Persistência:** Manter histórico no Obsidian
