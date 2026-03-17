# AGENTS.md - Orchestrator (Atualizado para Hands 2.0)

## 🆕 HANDS DE PRODUTIVIDADE (NOVOS - 2026)

Sistema GTD + Obsidian + Gestão de Projetos integrado

### Maestro-Supervisor
**Arquivo:** `hands/maestro-supervisor/HAND.toml`  
**Função:** Orquestrador principal de produtividade

### Inbox-Collector
**Arquivo:** `hands/inbox-collector/HAND.toml`  
**Função:** Captura rápida de tarefas/ideias (Telegram, áudio, email)

### GTD-Processor
**Arquivo:** `hands/gtd-processor/HAND.toml`  
**Função:** Processamento GTD puro - clarificar, organizar, revisar

### Project-Manager
**Arquivo:** `hands/project-manager/HAND.toml`  
**Função:** Gestão de projetos com outcomes e progresso

### Obsidian-Bridge
**Arquivo:** `hands/obsidian-bridge/HAND.toml`  
**Função:** Memória vetorial local (95% economia de tokens)

📖 **Documentação completa:** Ver seção "Hands de Produtividade" abaixo

---

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
Maestro-Supervisor (Orquestrador Principal)
├── Hands de Produtividade
│   ├── inbox-collector (Captura)
│   ├── gtd-processor (Processamento GTD)
│   ├── project-manager (Gestão de Projetos)
│   └── obsidian-bridge (Memória Vetorial)
└── Agents Técnicos
    ├── architect (Arquitetura/Código)
    ├── archivist (Conhecimento Técnico)
    ├── operator (Operações CLI)
    └── synchronizer (Integrações Externas)
```

## 🔄 NOVA ÁRVORE DE DECISÃO

```
Input do Usuário
├── Produtividade/Organização?
│   ├── Captura → inbox-collector
│   ├── Processamento GTD → gtd-processor
│   ├── Projetos → project-manager
│   ├── Busca/Contexto → obsidian-bridge
│   └── Revisões → gtd-processor
├── Técnico/Código?
│   ├── Análise complexa → architect (+ obsidian-bridge)
│   ├── Conhecimento → archivist (+ obsidian-bridge)
│   ├── CLI/Infra → operator
│   └── Integrações → synchronizer
└── Misto/Complexo?
    └── Maestro-Supervisor orquestra múltiplos
```

## Regras de Delegação

### 🎯 Hands de Produtividade (NOVOS - Prioridade 1)

1. **Captura rápida (qualquer input):** → `inbox-collector` (sempre)
2. **Processamento GTD (inbox, organização):** → `gtd-processor` (sempre)
3. **Gestão de projetos:** → `project-manager` (sempre)
4. **Busca de conhecimento/contexto:** → `obsidian-bridge` (sempre, zero tokens)
5. **Revisões GTD (daily/weekly):** → `gtd-processor` (agendado)

### 🔧 Agents Técnicos (Prioridade 2)

6. **Análise de código/arquitetura:** → `architect` (+ obsidian-bridge para contexto)
7. **Conhecimento técnico:** → `archivist` (+ obsidian-bridge para referências)
8. **Execução CLI/infra:** → `operator`
9. **Integrações externas:** → `synchronizer`

### ⚡ Gerais

10. **Tarefas triviais:** Maestro-Supervisor resolve diretamente
11. **Múltiplas tarefas:** Orquestração paralela via Maestro-Supervisor
12. **Economia de tokens:** Usar obsidian-bridge antes de qualquer LLM caro

## Estado dos Hands/Agents

| Hand/Agent | Tipo | Status | Economia Tokens |
|------------|------|--------|-----------------|
| **maestro-supervisor** | Hand Produtividade | 🟢 ACTIVE | 70% |
| **inbox-collector** | Hand Produtividade | 🟢 ACTIVE | 90% |
| **gtd-processor** | Hand Produtividade | 🟢 ACTIVE | 60% |
| **project-manager** | Hand Produtividade | 🟢 ACTIVE | 50% |
| **obsidian-bridge** | Hand Produtividade | 🟢 ACTIVE | **95%** |
| architect | Agent Técnico | 🟡 IDLE | - |
| archivist | Agent Técnico | 🟡 IDLE | - |
| operator | Agent Técnico | 🟡 IDLE | - |
| synchronizer | Agent Técnico | 🟡 IDLE | - |

**Legenda:** 🟢 = Pronto para uso | 🟡 = Aguardando integração

---

## 🚀 PRÓXIMOS PASSOS

### Ativação do Sistema
1. Configurar Ollama com `nomic-embed-text`
2. Ativar hands de produtividade:
   ```bash
   openfang hand activate maestro-supervisor
   openfang hand activate inbox-collector
   openfang hand activate gtd-processor
   openfang hand activate project-manager
   openfang hand activate obsidian-bridge
   ```
3. Testar fluxo completo: Captura → Processamento → Busca
4. Migrar agents técnicos para usar obsidian-bridge

### Documentação
- Ver `ESTRATEGIA_OpenFang_Implementacao.md` para detalhes completos
- Cada hand tem seu próprio SKILL.md em `hands/<nome>/SKILL.md`

---

*Atualizado em: 2026-03-17 | Versão: 2.0 (Sistema Hands + Agents)*
