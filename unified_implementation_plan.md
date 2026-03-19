# Plano Mestre de Implementação (Arquitetura, OpenFang & Produtividade)

Este documento unifica e adapta as diretrizes de Orquestração de Agentes (OpenFang) e o Sistema de Produtividade (Obsidian + TickTick) em um roteiro prático e focado na **criação e estruturação dos arquivos necessários** para reerguer o Maestro Agent OS.

## Visão Estrutural: O Repositório Base

Abaixo está o organograma dos arquivos que precisaremos construir e configurar durante a fase de execução para o sistema funcionar no Coolify/VPS.

```text
maestro-agent-os/
│
├── 📂 infra/                        # Setup Bare-Metal (Docker/Coolify)
│   ├── docker-compose.yml           # Serviço OpenFang, OpenViking, Ollama
│   └── setup-coolify.sh             # Script inicial de pastas e permissões
│
├── 📂 agents/                       # Manifestos OpenFang (Configuração das Mãos)
│   ├── orchestrator.toml            # Maestro-Líder (Gemini 2.5 Flash)
│   ├── architect.toml               # Maestro-Arquiteto (Gemini 3.1 Pro Preview)
│   ├── archivist.toml               # Arquivista Zettelkasten (Gemini 2.5 Flash-Lite)
│   ├── synchronizer.toml            # Sincronizador TickTick (Leve/Cron)
│   └── operator.toml                # Operador FinOps (Gemini 2.5 Flash)
│
├── 📂 capabilities/                 # Ferramentas Customizadas (Tools Code)
│   ├── openviking_bridge.js         # Interface com a API de Contexto do Obsidian
│   ├── finops_cli_delegator.sh      # Shell wrapper para o gemini-cli local
│   └── mcp_gateway.ts               # Servidor MCP unificador (TickTick, YouTube, Calendar)
│
└── 📂 data/                         # Volumes Montados (Estado e Memória)
    ├── 📂 obsidian_vault/           # Cofre do usuário persistido via Git Sync
    │   ├── 01-Inbox/
    │   ├── 02-Projetos/
    │   ├── 03-Zettelkasten/
    │   └── 99-Config/
    └── 📂 openfang_db/              # Memória de orquestração interna (SQLite)
```

---

## 1. Implementação dos Agentes (Arquivos `.toml`)

Teremos 5 *Hands* no OpenFang, cada uma com sua responsabilidade estrita. O `orchestrator.toml` atua como o **Supervisor** principal reagindo ao Telegram/eventos, enquanto os outros são acionados sob demanda ou via *crontab* (Schedule).

### A. Maestro-Líder (`orchestrator.toml`)
- **Papel:** Recepcionista, tomador de decisão (Triador).
- **Triggers:** Telegram Webhook.
- **Ferramentas (`tools`):** `openviking_read_abstract`, `spawn_architect`, `spawn_operator`, `ticktick_add_task`.
- **Implementação:** Arquivo toml contendo a *system prompt* focada na persona do Maestro, com regras rígidas para ler primeiro as preferências globais (`viking://user/preferences.md`).

### B. Maestro-Arquiteto (`architect.toml`)
- **Papel:** Engenheiro sênior para fluxos demorados.
- **Triggers:** Apenas via instrução do *Orchestrator* (`spawn_architect`).
- **Ferramentas (`tools`):** `openviking_search_deep`, `read_codebase`, `mcp_github`.
- **Implementação:** O prompt aqui forçará formatação Markdown profunda e a ausência de diálogos curtos (Chain-of-Thought focado em projetos / VOLTZ / WappTV).

### C. O Arquivista (`archivist.toml`)
- **Papel:** Zettelkasten Master.
- **Triggers:** Scheduler interno (ex: a cada 6h).
- **Ferramentas (`tools`):** `json_formatter`, `openviking_write`, `openviking_merge_knowledge`.
- **Implementação:** Tarefa muda. Ele acordará, lerá `01-Inbox`, estruturará o texto como Nota Permanente, enviará para `03-Zettelkasten` usando a Tool do OpenViking, apagará do Inbox e morrerá silenciosamente.

### D. O Sincronizador (`synchronizer.toml`)
- **Papel:** Ponte entre o status humano (TickTick) e as metas.
- **Triggers:** Scheduler Interno Diario (06:00 AM).
- **Ferramentas (`tools`):** `ticktick_get_today`, `ticktick_read_summary`.
- **Implementação:** Ele pega a lista de tarefas "Hoje" e falhas de ontem, sintetiza um JSON ou texto simples e cruza com os interesses do Maestro Líder gerar o "Sumário Matinal".

### E. Operador / FinOps (`operator.toml`)
- **Papel:** Arbitragem de Custos via Shell.
- **Ferramentas (`tools`):** `finops_cli_delegator` (encapsula shell do host).
- **Implementação:** Sempre que surgir um log de erro do `/var/log` de uma aplicação (ex: Coolify API), ele delega a leitura custosa ao `gemini-cli` local da máquina.

---

## 2. Implementação das Tools Customizadas (Capabilities)

### 2.1 O "MCP Gateway" Central (`capabilities/mcp_gateway.ts`)
Para mantermos o código limpo, em vez de criarmos várias tools fragmentadas, desenvolveremos um (1) Servidor MCP em TypeScript que agregará as integrações de APIs externas para o OpenFang:
- **`ticktick_add_task` / `ticktick_get_today`**: Comunicação OAuth com o TickTick, fechando o loop da Produtividade (Cenário de atalho no Telegram: "Lembre-me de revisar a api amanhã").
- **`youtube_search` / `gcalendar`**: Acesso à curadoria matinal e agenda.

### 2.2 OpenViking Bridge (`capabilities/openviking_bridge.js`)
Pequeno wrapper que transforma as URIs `viking://` na chamada REST POST padrão da API do container OpenViking.
- *Função 1:* `read_path(path)` - Retorna L1 (sumário) ou L2 (completo).
- *Função 2:* `write_knowledge(path, content, tags)` - Usado exclusivamente pelo *Arquivista*.

### 2.3 FinOps CLI Delegator (`capabilities/finops_cli_delegator.sh`)
Um script bash *safe-guarded* (bloqueia vazamento de escape de comando). O Agente envia apenas a string da pergunta e o path relativo de um arquivo de log na pasta permitida. 
O *wrapper* injeta na cota Pro: `gemini-cli -p "$PROMPT" -f "/app/safelogs/$ARQUIVO"`.

---

## 3. Implementação da Infraestrutura & Memória

### 3.1 Sincronização do "Segundo Cérebro"
1. **GitHub Sync (Recomendado):** O Obsidian local da sua máquina usa o *Obsidian Git* para dar *push* em um repositório privado a cada 15m.
2. Na VPS (Coolify), um *Webhook* ou *Cron git-pull* puxa isso para o diretório `/data/obsidian_vault/`.
3. O OpenViking (via Docker Compose) monta essa pasta como Read/Write e observa alterações, executando seus próprios Embeddings Local-CPU (`nomic-embed-text` via Ollama).

### 3.2 O Docker Compose Mestre (`infra/docker-compose.yml`)
O arquivo deverá unir na network privada do Coolify:
- `openfang` (Core OS e Handlers) com acesso ao socket Docker (se necessário para o Operador) via proxy blindado.
- `openviking` (Context DB & API Layer).
- `ollama` (Motor em CPU Mode para embeddings).
- `mcp-gateway-node` (Onde nosso código TS das bridges rodará como serviço contínuo de IPC/HTTP para o OpenFang).

---

## Próximo Passo Lógico
A documentação agora está taticamente aglutinada. 
Se concordar com este *Plano Mestre de Arquivos*, nosso próximo passo em `EXECUTION` é iniciar a construção efetiva gerando o boilerplate na raiz do seu servidor ou diretório local, começando pelo `docker-compose.yml` (`infra/*`) para viabilizar o ambiente base, ou pelos manifests `*.toml` dos agentes.
