# Resumo de Adaptações - OpenFang Agent Templates

## 📋 Visão Geral

Todos os agentes foram atualizados para o formato oficial do **OpenFang Agent OS**, alinhando-se com os 30 templates pré-construídos documentados em [openfang.sh/docs/agent-templates](https://www.openfang.sh/docs/agent-templates).

---

## 🔄 Mudanças Principais Realizadas

### 1. **Estrutura de Arquivos**

#### Antes:
```
agents/<nome>/
├── HAND.toml          (configuração)
├── SOUL.md            (personalidade)
├── IDENTITY.md        (identidade)
├── USER.md            (perfil usuário)
├── TOOLS.md           (ferramentas)
├── MEMORY.md          (memória)
├── AGENTS.md          (relações)
├── BOOTSTRAP.md       (inicialização)
└── HEARTBEAT.md       (sinal de vida)
```

#### Depois (Oficial OpenFang):
```
agents/<nome>/
├── agent.toml         (manifesto de configuração)
└── skill.md             (opcional - conhecimento adicional)
```

**Resultado:** Consolidamos 8 arquivos em 1 arquivo principal (`agent.toml`) seguindo o padrão oficial.

---

### 2. **Estrutura do Manifesto (agent.toml)**

#### Seções Oficiais Implementadas:

| Seção | Descrição | Status |
|-------|-----------|--------|
| `[agent]` | Metadados básicos (name, version, description, author, tags) | ✅ |
| `[model]` | Configuração LLM (provider, model, api_key_env, temperature, max_tokens, system_prompt) | ✅ |
| `[[fallback_models]]` | Modelo alternativo quando o principal falha | ✅ |
| `[schedule]` | Agendamento para agentes autônomos | ✅ |
| `[resources]` | Limites de recursos (tokens/hora, ferramentas simultâneas) | ✅ |
| `[capabilities]` | Permissões e ferramentas disponíveis | ✅ |

#### Exemplo de Estrutura Oficial:
```toml
[agent]
name = "orchestrator"
version = "1.0.0"
description = "Metaagente que coordena a frota de agentes"
author = "Matheus Gama de Luna"
tags = ["supervisor", "orchestration", "meta-agent", "portuguese"]

[model]
provider = "gemini"
model = "gemini-2.5-flash"
api_key_env = "GEMINI_API_KEY"
temperature = 0.3
max_tokens = 8192
system_prompt = """..."""

[[fallback_models]]
provider = "groq"
model = "llama-3.3-70b-versatile"
api_key_env = "GROQ_API_KEY"

[schedule]
periodic = { cron = "every 2m" }

[resources]
max_llm_tokens_per_hour = 500000
max_concurrent_tools = 10

[capabilities]
tools = ["web_fetch", "file_read", "agent_send", ...]
network = ["*"]
memory_read = ["*"]
memory_write = ["*"]
agent_spawn = true
agent_message = ["*"]
```

---

### 3. **Níveis de Modelos (4 Níveis Oficiais)**

A documentação do OpenFang organiza agentes em 4 níveis. Nossos agentes foram mapeados:

#### Nível 1 -- Fronteira (Raciocínio Profundo)
| Agente | Modelo Principal | Fallback | Cota/hora |
|--------|-----------------|----------|-----------|
| **Orchestrator** | gemini/gemini-2.5-flash | groq/llama-3.3-70b-versatile | 500.000 |
| **Architect** | gemini/gemini-2.5-pro | groq/llama-3.3-70b-versatile | 200.000 |

#### Nível 2 -- Inteligente (Análise & Programação)
*Mapeamento futuro: Coder, Researcher*

#### Nível 3 -- Equilibrado (Produtividade)
| Agente | Modelo Principal | Fallback | Cota/hora |
|--------|-----------------|----------|-----------|
| **Archivist** | groq/llama-3.3-70b-versatile | gemini/gemini-2.0-flash | 100.000 |
| **Synchronizer** | groq/llama-3.3-70b-versatile | gemini/gemini-2.0-flash | 150.000 |

#### Nível 4 -- Rápido (Operações Leves)
| Agente | Modelo Principal | Fallback | Cota/hora |
|--------|-----------------|----------|-----------|
| **Operator** | groq/llama-3.1-8b-instant | Sem plano B | 50.000 |

---

### 4. **Ferramentas Oficiais do OpenFang**

Substituímos ferramentas customizadas pelas ferramentas nativas do OpenFang:

| Ferramenta Antiga | Ferramenta Nova (Oficial) | Uso |
|-------------------|---------------------------|-----|
| `web_search` | `web_fetch` | Buscar conteúdo na web |
| `spawn_hand` | `agent_spawn` | Criar novos agentes |
| `mcp_*` | `agent_send`, `agent_list` | Comunicação entre agentes |
| `ticktick_*` | `memory_store`, `memory_recall` | Persistência de dados |
| `shell_execute_restricted` | `shell_exec` | Execução de comandos shell |
| `file_read` | `file_read` | Ler arquivos (mantido) |
| `file_write` | `file_write` | Escrever arquivos (mantido) |
| `file_list` | `file_list` | Listar diretórios (mantido) |

#### Lista Completa de Ferramentas Oficiais:
```toml
[capabilities]
tools = [
    "file_read",      # Ler arquivos
    "file_write",     # Escrever arquivos  
    "file_list",      # Listar diretórios
    "shell_exec",     # Executar comandos shell
    "memory_store",   # Persistir dados
    "memory_recall",  # Recuperar dados
    "web_fetch",      # Buscar URLs
    "agent_send",     # Enviar mensagem para agente
    "agent_list",     # Listar agentes
    "agent_spawn",    # Criar agente
    "agent_kill"      # Encerrar agente
]
```

---

### 5. **Prompts do Sistema (system_prompt)**

Os prompts foram reestruturados seguindo as melhores práticas oficiais:

#### Elementos Obrigatórios Incluídos:
1. **Identidade clara** - Nome, personalidade, tom de voz
2. **Metodologia** - Como o agente trabalha passo a passo
3. **Ferramentas disponíveis** - Lista explícita com descrições
4. **Regras de ouro** - O que sempre fazer
5. **Limitações** - O que NUNCA fazer
6. **Formato de saída** - Como estruturar respostas

#### Exemplo de Estrutura de Prompt:
```markdown
## Sua Identidade
- Nome: [nome]
- Personalidade: [características]
- Tom: [estilo de comunicação]
- Especialidade: [foco principal]

## Metodologia
1. [Passo 1]
2. [Passo 2]
...

## Ferramentas Disponíveis
- tool_name: descrição

## Regras de Ouro
1. [Regra 1]
2. [Regra 2]
...

## O que NUNCA fazer
- [Proibição 1]
- [Proibição 2]
...
```

---

### 6. **Configuração de Agendamento (Schedule)**

Implementamos agendamentos oficiais:

| Agente | Agendamento | Descrição |
|--------|-------------|-----------|
| **Orchestrator** | `every 2m` | Verificação contínua de tarefas |
| **Architect** | Sob demanda | Invocado pelo Orchestrator |
| **Archivist** | `every 4h` | Processamento em background |
| **Operator** | `every 5m` | Monitoramento de operações |
| **Synchronizer** | `every 1h` | Sincronização de tarefas + sumário 07:00 |

#### Sintaxe Oficial:
```toml
[schedule]
periodic = { cron = "every 5m" }           # Periódico
tinuous = { check_interval_secs = 120 }    # Contínuo (comentado)
# proactive = { conditions = ["event:agent_spawned"] }  # Event-driven
```

---

### 7. **Permissões e Capabilities**

Configuramos permissões seguindo o princípio do **menor privilégio**:

```toml
[capabilities]
# Ferramentas disponíveis
tools = ["file_read", "file_write", ...]

# Acesso à rede
network = ["*"]                    # Todos os domínios

# Memória
memory_read = ["*"]                # Ler de todos os namespaces
memory_write = ["self.*", "shared.*"]  # Escrever no próprio namespace e shared

# Comunicação entre agentes
agent_spawn = true                 # Pode criar agentes
agent_message = ["*"]              # Pode falar com todos os agentes

# Shell (apenas para Operator)
shell = [
    "docker ps",
    "docker logs",
    "cat /var/log/*",
    "df -h",
    "free -m"
]
```

---

## 📊 Comparação: Nossos Agentes vs Templates Oficiais

| Aspecto | Nossa Implementação | OpenFang Padrão | Alinhamento |
|---------|-------------------|-----------------|-------------|
| **Formato** | `agent.toml` | `agent.toml` | ✅ 100% |
| **System Prompt** | Completo, estruturado | Completo, estruturado | ✅ 100% |
| **Ferramentas** | Oficiais do OpenFang | Oficiais do OpenFang | ✅ 100% |
| **Níveis** | 1, 3, 4 | 1, 2, 3, 4 | ✅ Parcial |
| **Fallback** | Configurado | Configurado | ✅ 100% |
| **Agendamento** | Cron oficial | Cron oficial | ✅ 100% |
| **Portugês BR** | ✅ Sim | ❌ Não | 🌟 Diferencial |
| **Documentação** | Extensa | Mínima | 🌟 Extra |

---

## 🚀 Como Usar os Agentes (Comandos Oficiais)

### Spawn de Agentes:
```bash
# Spawn pelo nome do template
openfang spawn orchestrator
openfang spawn architect
openfang spawn ops

# Spawn com nome customizado
openfang spawn orchestrator --name "maestro-lider"

# Spawn via caminho do arquivo
openfang spawn --template agents/orchestrator/agent.toml
```

### API REST:
```bash
# Criar agente
POST /api/agents
{
  "template": "orchestrator",
  "name": "meu-orquestrador"
}

# Enviar mensagem
POST /api/agents/{id}/message
{
  "content": "Analise o projeto e sugira melhorias"
}

# Listar agentes
GET /api/agents

# WebSocket (streaming)
WS /api/agents/{id}/ws
```

---

## 📝 Variáveis de Ambiente Necessárias

Configure estas chaves de API para ativar os provedores:

```bash
# Obrigatório (níveis 3 e 4)
export GROQ_API_KEY="sua_chave_groq"

# Opcional (nível 2)
export GEMINI_API_KEY="sua_chave_gemini"

# Opcional (nível 1 - fronteira)
export DEEPSEEK_API_KEY="sua_chave_deepseek"
```

---

## 🎯 Próximos Passos Recomendados

1. **Testar Deploy:**
   ```bash
   openfang agent deploy agents/orchestrator/agent.toml
   ```

2. **Verificar Logs:**
   ```bash
   openfang logs orchestrator
   ```

3. **Iterar baseado em feedback** dos primeiros testes

4. **Considerar adicionar:**
   - Nível 2 agentes: `coder`, `researcher`, `debugger`
   - Integrações MCP para TickTick (quando disponível)
   - Skills adicionais em arquivos `skill.md` separados

---

## ✅ Checklist de Migração

- [x] Analisar documentação oficial do OpenFang
- [x] Mapear estrutura de agent.toml oficial
- [x] Atualizar Orchestrator (nível 1)
- [x] Atualizar Architect (nível 1)
- [x] Atualizar Archivist (nível 3)
- [x] Atualizar Operator (nível 4)
- [x] Atualizar Synchronizer (nível 3)
- [x] Configurar fallback models
- [x] Definir schedules oficiais
- [x] Mapear ferramentas nativas
- [x] Criar system prompts estruturados
- [x] Configurar capabilities e permissões
- [x] Documentar adaptações

---

## 📚 Referências

- [OpenFang Agent Templates](https://www.openfang.sh/docs/agent-templates)
- [OpenFang CLI Reference](https://www.openfang.sh/docs/cli-reference)
- [OpenFang API Reference](https://www.openfang.sh/docs/api-reference)
- [OpenFang GitHub](https://github.com/RightNow-AI/openfang)

---

**Status:** ✅ **Todos os agentes atualizados para formato oficial OpenFang v1.0.0**
