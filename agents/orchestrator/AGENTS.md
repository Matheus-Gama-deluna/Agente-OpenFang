# AGENTS.md - Orchestrator

## Agentes Subordinados

O Orchestrator pode spawnar e delegar para os seguintes agentes especializados:

---

### Architect (Maestro-Arquiteto)
**Arquivo:** `agents/architect/HAND.toml`  
**Modelo:** gemini-2.5-pro  
**Função:** Pensamento profundo, análise de código, arquitetura

**Quando invocar:**
- Análise de código complexo
- Refatoração de serviços
- Planejamento arquitetural
- Documentação técnica detalhada

**Como invocar:**
```
spawn_hand("architect", "Analisar arquitetura WappTV", context)
```

---

### Archivist (Arquivista)
**Arquivo:** `agents/archivist/HAND.toml`  
**Modelo:** gemini-2.5-flash-lite  
**Função:** Processamento de conhecimento, Zettelkasten

**Quando invocar:**
- Formatar interações para notas
- Criar entradas Zettelkasten
- Processar conhecimento em background

**Como invocar:**
```
spawn_hand("archivist", "Processar resumo da reunião", context)
```

---

### Operator (Operador)
**Arquivo:** `agents/operator/HAND.toml`  
**Modelo:** gemini-2.5-flash  
**Função:** Execução de comandos CLI, diagnóstico de logs

**Quando invocar:**
- Verificar logs de serviço
- Executar comandos Docker
- Diagnóstico de infraestrutura

**Como invocar:**
```
spawn_hand("operator", "Verificar logs WappTV", context)
```

---

### Synchronizer (Sincronizador)
**Arquivo:** `agents/synchronizer/HAND.toml`  
**Modelo:** gemini-2.5-flash  
**Função:** Integração TickTick, gestão de tarefas

**Quando invocar:**
- Criar tarefas no TickTick
- Consultar agenda
- Sincronizar Obsidian-TickTick

**Como invocar:**
```
spawn_hand("synchronizer", "Criar tarefa revisão código", context)
```

## Hierarquia de Delegação

```
Orchestrator (Supervisor)
├── Architect (Tarefas complexas/análise)
├── Archivist (Processamento de conhecimento)
├── Operator (Execução/infraestrutura)
└── Synchronizer (Gestão de tarefas)
```

## Regras de Delegação

1. **Tarefas triviais:** Orchestrator resolve diretamente
2. **Código/Arquitetura:** Sempre delega ao Architect
3. **Comandos CLI:** Sempre delega ao Operator
4. **Tarefas/Agenda:** Sempre delega ao Synchronizer
5. **Processamento de notas:** Sempre delega ao Archivist
6. **Múltiplas tarefas:** Pode spawnar múltiplos agentes em paralelo

## Estado dos Agentes

| Agente | Status | Último Ping | Carga |
|--------|--------|-------------|-------|
| architect | IDLE | - | 0% |
| archivist | IDLE | - | 0% |
| operator | IDLE | - | 0% |
| synchronizer | IDLE | - | 0% |
