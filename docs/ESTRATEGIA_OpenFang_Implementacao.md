# Análise Estratégica: OpenFang vs Nosso Plano
## Hands Personalizados, Economia de Tokens e Implementação Prática

---

## 1. 🎯 COMPREENSÃO DO OPENFANG

### 1.1 O Que é Realmente o OpenFang

O OpenFang **não é apenas um framework** — é um **Sistema Operacional de Agentes** completo:

```
┌─────────────────────────────────────────────────────────────┐
│                    OPENFANG ARCHITECTURE                  │
├─────────────────────────────────────────────────────────────┤
│  Kernel (Rust) → 137K LOC, 14 crates, 1 binário (~32MB)    │
│  ├── Orchestration: Workflows, RBAC, Scheduler, Budget     │
│  ├── Runtime: Agent loop, 3 LLM drivers, 53 tools        │
│  ├── API: 140+ REST/WebSocket/SSE endpoints                │
│  ├── Channels: 40 adapters (Telegram, WhatsApp, Email...)  │
│  ├── Memory: SQLite + Vetores + Embeddings                 │
│  └── Security: 16 camadas de defesa                         │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Hands: O Conceito Central

**"Hands são agentes que trabalham para você, não esperam você digitar"**

```
┌─────────────────────────────────────────────────────────────┐
│  HAND = Capability Package Autônomo                         │
├─────────────────────────────────────────────────────────────┤
│  HAND.toml → Manifesto (tools, settings, triggers)        │
│  System Prompt → Playbook operacional (500+ palavras)     │
│  SKILL.md → Conhecimento de domínio injetado em runtime   │
│  Guardrails → Gates de aprovação para ações sensíveis       │
└─────────────────────────────────────────────────────────────┘
```

### 1.3 Como o OpenFang Funciona na Prática

```bash
# 1. Inicialização (único binário ~32MB)
curl -fsSL https://openfang.sh/install | sh
openfang init
openfang start

# 2. Dashboard acessível em http://localhost:4200

# 3. Ativar Hands (agentes autônomos)
openfang hand activate researcher    # Pesquisa autônoma
openfang hand activate lead          # Geração de leads diária
openfang hand activate monitoring    # Monitoramento 24/7

# 4. Criar Hand personalizado
openfang hand create --template custom --name obsidian-bridge
```

---

## 2. 🔍 ANÁLISE CRÍTICA: NOSSO PLANO vs OPENFANG REAL

### 2.1 Mapeamento de Conceitos

| Nosso Conceito (Plano) | OpenFang Real | Alinhamento | Gap |
|------------------------|---------------|-------------|-----|
| `HAND.toml` | `HAND.toml` ✅ | 100% | Nenhum |
| `agent.toml` | Não existe nativamente | ❌ | Nome errado |
| `orchestrator` | Hand de Supervisor | 80% | Faltam triggers |
| `archivist` | Hand de Researcher | 60% | Não é background |
| `operator` | Hand de Executor | 70% | Sem FinOps nativo |
| `synchronizer` | Não existe similar | 30% | Precisa criar |
| OpenViking | Integração via MCP | 50% | Não é nativo |
| TickTick | Via MCP custom | 40% | Requer desenvolvimento |

### 2.2 Erros Críticos Identificados

#### ERRO 1: Nomenclatura
```toml
# ❌ ERRADO (nosso atual)
[agent]
name = "orchestrator"

# ✅ CORRETO (OpenFang nativo)
[hand]
name = "orchestrator"
description = "..."
version = "1.0.0"
```

#### ERRO 2: Estrutura de Seções
```toml
# ❌ NOSSO (inventado)
[agent]
[model]
[schedule]
[resources]
[capabilities]

# ✅ OPENFANG (documentado)
[hand]           # Metadata
[model]          # LLM config
[triggers]       # Eventos de ativação
[tools]          # Ferramentas habilitadas
[behavior]       # Comportamento
[memory]         # Config de memória
[security]       # Whitelist/blacklist
```

#### ERRO 3: Ferramentas Não-Existentes
```toml
# ❌ NOSSO (inventado)
tools = [
    "web_fetch",
    "agent_spawn",
    "agent_send",
    "memory_store",
    "memory_recall"
]

# ✅ OPENFANG (53 ferramentas nativas)
tools = [
    "web_search",
    "web_fetch", 
    "file_read",
    "file_write",
    "shell_exec",
    "telegram_send",
    "discord_send",
    "sqlite_query",
    "vector_search",
    "embedding_generate",
    ...  # 43 mais
]
```

### 2.3 O Que o OpenFang Realmente Oferece

#### 7 Hands Bundled (Pré-construídos):
1. **researcher** → Pesquisa profunda e knowledge graphs
2. **lead** → Geração de leads e prospecção
3. **content** → Criação de conteúdo autônomo
4. **monitoring** → Monitoramento de targets 24/7
5. **social** → Gestão de mídias sociais
6. **browser** → Automação de browser com guardrails
7. **code** → Análise e geração de código

#### 40 Channel Adapters:
```
Core: Telegram, Discord, Slack, WhatsApp, Email
Enterprise: Teams, Webex, Google Chat
Social: LINE, Messenger, Mastodon, LinkedIn
Privacy: Signal, Threema, Nostr
```

#### Sistema de Memória Nativo:
```
openfang-memory:
├── SQLite persistence
├── Vector embeddings (nomic-embed-text)
├── Canonical sessions
├── Compaction automática
└── Cache inteligente
```

---

## 3. 🎨 ESTRATÉGIAS PARA HANDS PERSONALIZADOS

### 3.1 Hand: Obsidian Bridge (Segundo Cérebro)

```toml
# HAND.toml - Obsidian Bridge
[hand]
name = "obsidian-bridge"
description = "Ponte entre Obsidian Vault e OpenFang. Indexa notas, extrai conhecimento, mantém grafo de relacionamentos."
version = "1.0.0"
author = "Matheus Gama de Luna"
tags = ["knowledge", "obsidian", "zettelkasten", "portuguese"]

[model]
provider = "groq"
model = "llama-3.3-70b-versatile"
api_key_env = "GROQ_API_KEY"
temperature = 0.1  # Baixo para precisão
max_tokens = 4096

[triggers]
# Gatilhos de ativação
type = ["cron", "file_change", "invocation"]
cron_schedule = "0 */4 * * *"  # A cada 4 horas
watch_paths = ["/data/obsidian_vault/**/*.md"]

[tools]
# Ferramentas nativas OpenFang
enabled = [
    "file_read",
    "file_list", 
    "file_watcher",
    "embedding_generate",
    "vector_search",
    "sqlite_query",
    "markdown_parse",
    "yaml_frontmatter_extract",
    "telegram_send"
]

[behavior]
# Comportamento otimizado para economia
cache_embeddings = true          # Cache de vetores
batch_processing = true          # Processamento em lote
max_notes_per_run = 50           # Limitar processamento
deduplicate = true               # Evitar reprocessamento
incremental_indexing = true      # Só indexar mudanças

[memory]
# Usar memória nativa do OpenFang
short_term = "context_window"
long_term = "openfang_memory"    # Nativo, não OpenViking
context_retention = "permanent"

[logging]
level = "info"
format = "structured"
output = ["console", "sqlite"]
```

#### SKILL.md - Obsidian Bridge:
```markdown
# SKILL.md - Obsidian Bridge

## Conhecimento de Domínio: Zettelkasten

### Estrutura de Vault
- `/01-Inbox/` → Notas cruas, capturas rápidas
- `/02-Projects/` → Notas temporárias de projetos
- `/03-Zettelkasten/` → Notas atômicas permanentes
- `/99-Config/` → Preferências e configurações

### Metodologia de Indexação
1. **Extração**: Ler YAML frontmatter de cada nota
2. **Embedding**: Gerar vetor com nomic-embed-text
3. **Linking**: Identificar [[wikilinks]] e #tags
4. **Storage**: Persistir em SQLite vetorial nativo
5. **Retrieval**: Busca semântica via cosine similarity

### Otimizações de Custo
- **Incremental**: Hash de arquivo para detectar mudanças
- **Batch**: Processar 10 notas por batch
- **Cache**: Manter embeddings em memória por 1h
- **Lazy**: Só indexar quando vault modificado

### Formatos Suportados
- Notas Markdown padrão
- YAML frontmatter completo
- Wikilinks [[note_id]]
- Tags #tag ou #tag/subtag
- Dataview blocks (read-only)
```

---

### 3.2 Hand: TickTick Sync (Produtividade)

```toml
# HAND.toml - TickTick Sync
[hand]
name = "ticktick-sync"
description = "Sincronização bidirecional entre OpenFang e TickTick. Gestão de tarefas inteligente."
version = "1.0.0"

[model]
provider = "groq"
model = "llama-3.3-70b-versatile"
temperature = 0.2

[triggers]
type = ["cron", "webhook", "invocation"]
cron_schedule = "0 */2 * * *"  # A cada 2 horas
webhook_endpoint = "/ticktick/webhook"

[tools]
enabled = [
    "http_request",      # Para API TickTick
    "json_parse",
    "date_parser",
    "telegram_send",
    "file_write",        # Para logging
    "sqlite_query"       # Cache local
]

[behavior]
# Estratégia de economia
cache_tasks = true               # Cache de tarefas
batch_sync = true                # Sincronização em lote
rate_limit = "100/hour"          # Respeitar limites TickTick
retry_failed = true
max_retries = 3

# Configurações específicas
[integrations.ticktick]
api_base = "https://api.ticktick.com/open/v1"
client_id = "${TICKTICK_CLIENT_ID}"
client_secret = "${TICKTICK_CLIENT_SECRET}"
projects = [
    { id = "p_WappTV", name = "WappTV", color = "#FF6B6B" },
    { id = "p_VOLTZ", name = "VOLTZ", color = "#4ECDC4" },
    { id = "p_DEK", name = "DEK", color = "#45B7D1" },
    { id = "p_Pessoal", name = "Pessoal", color = "#96CEB4" },
    { id = "p_Maestro", name = "Maestro System", color = "#FECA57" }
]

[memory]
short_term = "context_window"
long_term = "sqlite"  # Cache local de tarefas
```

---

### 3.3 Hand: Task Receiver & Reporter

```toml
# HAND.toml - Task Receiver
[hand]
name = "task-receiver"
description = "Recebe tarefas via múltiplos canais, enriquece com contexto e reporta progresso."
version = "1.0.0"

[model]
provider = "gemini"
model = "gemini-2.0-flash-lite"  # Mais econômico
max_tokens = 2048

[triggers]
type = ["channel_message", "webhook", "email"]
channels = ["telegram", "whatsapp", "email"]

[tools]
enabled = [
    "telegram_receive",
    "whatsapp_receive", 
    "email_receive",
    "intent_classifier",
    "entity_extractor",
    "date_parser",
    "task_create",
    "task_update",
    "notification_send"
]

[behavior]
# Processamento inteligente
auto_classify = true             # Classificar intenção automaticamente
confidence_threshold = 0.8       # Só agir se confiança > 80%
confirm_destructive = true      # Confirmar antes de deletar
rich_reports = true             # Relatórios detalhados

[reporting]
# Configuração de reports
daily_digest = true             # Sumário diário
weekly_report = true            # Relatório semanal
format = "markdown"
channels = ["telegram"]
time = "07:00"
timezone = "America/Sao_Paulo"
```

---

## 4. 🧠 MELHORES PRÁTICAS PARA ORQUESTRADOR

### 4.1 Arquitetura do Supervisor (Hand Principal)

```toml
# HAND.toml - Maestro Supervisor
[hand]
name = "maestro-supervisor"
description = "Orquestrador principal. Decide, delega e monitora. Fala português brasileiro."
version = "2.0.0"

[model]
provider = "gemini"
model = "gemini-2.5-flash-lite"  # Flash-lite é mais rápido
api_key_env = "GEMINI_API_KEY"
temperature = 0.2
max_tokens = 4096

[[fallback_models]]
provider = "groq"
model = "llama-3.3-70b-versatile"
api_key_env = "GROQ_API_KEY"

[triggers]
type = ["channel_message", "webhook", "hand_completion"]
channels = ["telegram"]
priority_handling = true

[tools]
enabled = [
    "intent_classifier",
    "entity_extractor",
    "hand_spawn",
    "hand_message",
    "hand_list",
    "hand_status",
    "memory_recall",
    "memory_store",
    "telegram_send",
    "web_search",
    "date_parser"
]

[behavior]
# Otimizações críticas
cache_intent_classification = true    # Cache de classificações
reuse_context = true                   # Reusar contexto entre mensagens
batch_spawn = true                     # Spawn múltiplo quando possível
lazy_loading = true                    # Só carregar hands quando necessário

# Delegação inteligente
[delegation.rules]
"code_analysis" = "code-hand"
"research" = "researcher-hand"
"task_management" = "ticktick-sync"
"knowledge_query" = "obsidian-bridge"
"cli_operation" = "executor-hand"
"meeting_notes" = "meeting-hand"

# Limites de custo
[finops]
token_budget_daily = 50000            # Limite diário de tokens
warn_at_80_percent = true
hand_preference = "local_first"       # Preferir hands locais
api_fallback_threshold = 3            # Fallback após 3 falhas
```

### 4.2 Prompt do Supervisor (Estratégia de Delegação)

```markdown
## Sistema de Delegação Inteligente

Você é o Maestro. Sua função é DECIDIR, não executar.

### Árvore de Decisão

1. **Receber Mensagem**
   ├── Extrair intenção (intent_classification)
   ├── Buscar contexto histórico (memory_recall)
   └── Classificar complexidade

2. **Decisão de Execução**
   ├── Se trivial (< 5s de processamento) → Resolver direto
   ├── Se específico (domínio claro) → Delegar para Hand especialista
   └── Se complexo (múltiplos domínios) → Decompor e orquestrar

3. **Delegação**
   ├── Spawn hand apropriado (hand_spawn)
   ├── Enviar contexto completo (hand_message)
   ├── Aguardar resultado (async)
   └── Sintetizar resposta final

4. **Economia de Tokens**
   ├── Usar local/embeddings quando possível
   ├── Batch processar quando > 3 tarefas similares
   ├── Cache de respostas para queries repetidas
   └── Fallback para modelos mais baratos quando apropriado

### Exemplos de Delegação

Usuário: "Analise o código do repositório"
→ Spawn: code-hand + contexto do repo

Usuário: "Crie tarefa para revisar API amanhã"
→ Spawn: ticktick-sync + parsed date

Usuário: "O que discutimos sobre WappTV na semana passada?"
→ Spawn: obsidian-bridge + query semântica

Usuário: "Execute docker ps na VPS"
→ Spawn: executor-hand + comando validado
```

---

## 5. 💰 ESTRATÉGIAS DE ECONOMIA DE TOKENS

### 5.1 Hierarquia de Custo (Mais Barato → Mais Caro)

```
┌─────────────────────────────────────────────────────────────┐
│  HIERARQUIA DE CUSTO - Sempre preferir o mais à esquerda   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. CACHE LOCAL (Grátis)                                   │
│     ├── SQLite persistence                                 │
│     ├── Vector embeddings cache                            │
│     ├── Intent classification cache                        │
│     └── Hand result cache                                  │
│                                                             │
│  2. EMBEDDINGS LOCAIS (Grátis - Ollama)                   │
│     ├── nomic-embed-text (CPU)                             │
│     ├── Busca semântica local                              │
│     └── Similaridade de notas                              │
│                                                             │
│  3. LLM LOCAL/CLI (Muito Barato)                           │
│     ├── gemini-cli (Google AI Pro)                         │
│     ├── Ollama (llama3.1:8b)                               │
│     └── Whisper.cpp (transcrição local)                    │
│                                                             │
│  4. LLM CLOUD BARATO (Barato)                              │
│     ├── groq/llama-3.1-8b-instant                          │
│     ├── gemini-2.0-flash-lite                              │
│     └── deepseek-chat                                       │
│                                                             │
│  5. LLM CLOUD MÉDIO (Médio)                                 │
│     ├── groq/llama-3.3-70b-versatile                       │
│     ├── gemini-2.0-flash                                     │
│     └── claude-3-haiku                                       │
│                                                             │
│  6. LLM CLOUD PREMIUM (Caro) - Só quando necessário       │
│     ├── gemini-2.5-pro                                      │
│     ├── claude-3.5-sonnet                                    │
│     └── gpt-4o                                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 Tabela de Decisão por Cenário

| Cenário | Primeira Escolha | Fallback | Cache | Estimativa de Economia |
|---------|-----------------|----------|-------|----------------------|
| **Classificação de intenção** | `intent_classifier` local | `groq/llama-3.1-8b` | 24h | 90% |
| **Busca em notas** | `vector_search` local | `groq/llama-3.3-70b` | 1h | 95% |
| **Transcrição de áudio** | `whisper.cpp` local | `groq/whisper-large-v3` | N/A | 100% |
| **Resumo simples** | `gemini-cli` local | `gemini-2.0-flash-lite` | 1h | 85% |
| **Análise de código** | `gemini-2.0-flash` | `gemini-2.5-pro` | Por arquivo | 70% |
| **Pesquisa web** | `web_search` + cache | N/A | 6h | 60% |
| **Geração criativa** | `gemini-2.5-flash` | `gemini-2.5-pro` | N/A | N/A |
| **Raciocínio complexo** | `gemini-2.5-pro` | `claude-3.5-sonnet` | Contexto | N/A |

### 5.3 Configurações de Cache Específicas

```toml
# HAND.toml - Configurações de Cache

[cache]
# Estratégia geral
strategy = "aggressive"  # aggressive | balanced | conservative

# TTL (Time To Live) por tipo
ttl = { 
    intent = "24h",      # Classificações de intenção
    embedding = "7d",    # Vetores de embeddings
    search = "6h",       # Resultados de busca
    hand_result = "1h",  # Resultados de hands
    web = "4h",          # Conteúdo web
    file = "1h"          # Leitura de arquivos
}

# Cache warming (pré-carregamento)
warm_on_start = true
warm_patterns = [
    "viking://user/preferences.md",
    "viking://config/projects.json"
]

# Invalidação inteligente
invalidate_on_file_change = true
invalidate_on_webhook = ["ticktick", "github"]
```

---

## 6. 📊 IMPLEMENTAÇÃO PRÁTICA

### 6.1 Estrutura de Diretórios Recomendada

```
~/openfang-setup/
├── hands/
│   ├── custom/
│   │   ├── obsidian-bridge/
│   │   │   ├── HAND.toml
│   │   │   ├── SKILL.md
│   │   │   └── scripts/
│   │   │       └── index_vault.py
│   │   ├── ticktick-sync/
│   │   │   ├── HAND.toml
│   │   │   └── SKILL.md
│   │   └── maestro-supervisor/
│   │       ├── HAND.toml
│   │       └── SKILL.md
│   └── overrides/
│       └── researcher-override.toml
├── data/
│   ├── obsidian_vault/     # Mount do vault
│   ├── cache/
│   │   ├── embeddings/
│   │   ├── intent_cache.db
│   │   └── hand_results/
│   └── ticktick_cache.db
├── config/
│   ├── openfang.toml       # Config global
│   └── providers.yaml      # Chaves de API
└── docker-compose.yml      # Stack completo
```

### 6.2 Configuração Global (openfang.toml)

```toml
# openfang.toml - Configuração Global

[server]
bind = "0.0.0.0:4200"
dashboard_enabled = true
api_cors = ["http://localhost:3000"]

[providers]
# Prioridade de uso (primeiro = mais preferido)
order = ["ollama", "gemini", "groq", "openai"]

[providers.ollama]
enabled = true
base_url = "http://localhost:11434"
models = ["nomic-embed-text", "llama3.1:8b"]

[providers.gemini]
enabled = true
api_key = "${GEMINI_API_KEY}"
models = ["gemini-2.0-flash-lite", "gemini-2.0-flash", "gemini-2.5-pro"]

[providers.groq]
enabled = true
api_key = "${GROQ_API_KEY}"
models = ["llama-3.1-8b-instant", "llama-3.3-70b-versatile"]

[cache]
enabled = true
backend = "sqlite"
path = "/data/cache"
max_size = "1GB"

[channels]
enabled = ["telegram", "webhook"]

[channels.telegram]
bot_token = "${TELEGRAM_BOT_TOKEN}"
allowed_chats = ["${TELEGRAM_CHAT_ID}"]

[finops]
token_budget_daily = 100000
warn_threshold = 0.8
block_threshold = 1.2
alert_channel = "telegram"
```

### 6.3 Docker Compose (Stack Completo)

```yaml
# docker-compose.yml
version: '3.8'

services:
  openfang:
    image: rightnowai/openfang:latest
    container_name: openfang-core
    restart: unless-stopped
    ports:
      - "4200:4200"
    volumes:
      - ./config:/app/config
      - ./data:/app/data
      - ./hands:/app/hands/custom
      - /var/run/docker.sock:/var/run/docker.sock  # Para shell_exec
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - GROQ_API_KEY=${GROQ_API_KEY}
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
      - OPENFANG_LOG_LEVEL=info
    networks:
      - openfang-network
    depends_on:
      - ollama
      - obsidian-volume

  ollama:
    image: ollama/ollama:latest
    container_name: ollama-local
    restart: unless-stopped
    volumes:
      - ollama-data:/root/.ollama
    environment:
      - OLLAMA_HOST=0.0.0.0:11434
    networks:
      - openfang-network
    # NÃO expor porta 11434 externamente!
    # Só acessível via network interna

  obsidian-volume:
    image: alpine:latest
    container_name: obsidian-data
    restart: unless-stopped
    volumes:
      - obsidian-vault:/data/obsidian_vault:ro
      # Ou sync via syncthing/git
    command: tail -f /dev/null
    networks:
      - openfang-network

  # Opcional: Whisper.cpp para transcrição local
  whisper:
    image: aldanial/whisper.cpp:latest
    container_name: whisper-local
    restart: unless-stopped
    volumes:
      - ./data/audio:/audio:ro
    environment:
      - WHISPER_MODEL=small
    command: server --host 0.0.0.0 --port 8080
    networks:
      - openfang-network

volumes:
  ollama-data:
  obsidian-vault:
    # Pode ser bind mount para diretório local
    # driver: local
    # driver_opts:
    #   type: none
    #   o: bind
    #   device: /path/to/obsidian

networks:
  openfang-network:
    driver: bridge
```

---

## 7. 🎯 PLANO DE IMPLEMENTAÇÃO

### Fase 1: Setup Core (Semana 1)
- [ ] Instalar OpenFang binário nativo
- [ ] Configurar providers (Groq, Gemini)
- [ ] Setup Ollama local com nomic-embed-text
- [ ] Testar hands bundled (researcher, lead)

### Fase 2: Hands Personalizados (Semana 2)
- [ ] Criar Obsidian Bridge Hand
- [ ] Implementar indexação incremental
- [ ] Criar TickTick Sync Hand
- [ ] Integrar API TickTick

### Fase 3: Supervisor Inteligente (Semana 3)
- [ ] Configurar Maestro Supervisor
- [ ] Implementar árvore de decisão
- [ ] Setup cache de intenções
- [ ] Testar delegação entre hands

### Fase 4: Otimização (Semana 4)
- [ ] Medir consumo de tokens
- [ ] Ajustar estratégias de cache
- [ ] Implementar FinOps dashboard
- [ ] Documentar runbook

### Fase 5: Integrações (Semanas 5-6)
- [ ] Telegram bot completo
- [ ] Webhook endpoints
- [ ] MCP servers customizados
- [ ] Backup automático

---

## 8. 📈 METAS DE ECONOMIA

| Métrica | Atual | Meta OpenFang | Economia |
|---------|-------|---------------|----------|
| **Tokens/dia** | ~50.000 | ~15.000 | **70%** |
| **Custo mensal** | ~$30 | ~$8 | **73%** |
| **Latência média** | 2.5s | 0.8s | **68%** |
| **Cache hit rate** | 0% | 65% | **N/A** |
| **Hands ativos** | 0 | 5+ | **N/A** |

---

## 9. 🚨 RISCOS E MITIGAÇÕES

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| API Rate Limits | Média | Alto | Retry com backoff, cache agressivo |
| Token Budget exceeded | Média | Alto | Fallback models, daily quotas |
| Ollama CPU lento | Baixa | Médio | Warmup automático, GPU opcional |
| Vault desync | Baixa | Alto | Git sync, checksum validation |
| Hand mal configurado | Média | Alto | Validação HAND.toml, dry-run mode |

---

## 10. ✅ CHECKLIST FINAL

### Pre-Deploy
- [ ] Revisar HAND.toml com `openfang hand validate`
- [ ] Testar cada hand em modo dry-run
- [ ] Configurar alertas de orçamento
- [ ] Backup da configuração

### Deploy
- [ ] Start com `openfang start --dry-run`
- [ ] Verificar logs: `openfang logs -f`
- [ ] Testar cada canal (Telegram, Webhook)
- [ ] Confirmar hands ativos: `openfang hand list`

### Post-Deploy
- [ ] Monitorar dashboard em localhost:4200
- [ ] Verificar métricas de tokens
- [ ] Testar cenário end-to-end
- [ ] Documentar incidentes

---

**Conclusão:** O OpenFang oferece infraestrutura completa para nosso objetivo. A chave é:
1. Usar **HAND.toml** (não agent.toml)
2. Implementar **cache agressivo** desde o início
3. Preferir **embeddings locais** (Ollama)
4. Criar **hands específicos** para cada domínio
5. Configurar **supervisor inteligente** com delegação automática

**Próximo passo imediato:** Corrigir nomenclatura e estrutura dos nossos arquivos para alinhar com OpenFang nativo.
