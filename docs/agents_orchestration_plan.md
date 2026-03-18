# Plano de Arquitetura Roteada de Agentes (OpenFang)

O núcleo do Maestro se sustenta no design de orquestração do [OpenFang](https://github.com/rightnowai/openfang). Trabalharemos baseados em arquivos de manifestos de configuração **`HAND.toml`** para definir as responsabilidades isoladas de cada entidade no seu ciclo.

## 1. Topologia de Hands (Mãos do OpenFang)

A equipe será particionada em responsabilidades claras utilizando as boas práticas de sistemas 2026 (Supervisor / Delegador / Executors):

### 1.1 `orchestrator.toml` (O Maestro-Líder)
*O cérebro da operação. É um agente persistente e *event-driven*.*
- **LLM Engine:** `gemini-2.5-flash` (ou superior focado em rapidez).
- **Gatilhos (Triggers):** Webhooks do Telegram, Menções diretas.
- **Missão:** Entender a intenção inicial através do contexto do OpenViking, decidir e encaminhar a tarefa para uma sub-entidade ("spawn agent") ou resolver ele mesmo se for banal.
- **Tools Integradas:** `openviking_read_abstract`, `spawn_hand`, `mcp_calendar_read`.

### 1.2 `architect.toml` (O Maestro-Arquiteto)
*O pensador profundo (Long-Running).*
- **LLM Engine:** `gemini-2.5-pro` (ou `gemini-3.1-pro-preview` para extrema lógica).
- **Gatilhos:** Apenas invocação sob demanda pelo *Orchestrator*.
- **Missão:** Entrar em discussões intensas sobre estrutura de código, refatoração de serviços (WappTV, VOLTZ, DEK). Ele pensa passo-a-passo e emite relatórios *Markdowns* longos.
- **Tools Integradas:** `openviking_search_deep`, `read_codebase`, `mcp_github_read`.

### 1.3 `archivist.toml` (O Arquivista)
*Motor silencioso de *knowledge processing*.*
- **LLM Engine:** `gemini-2.5-flash-lite` (O otimizado para hipervelocidade e JSON, já que 2.0-flash-lite perde força).
- **Gatilhos:** Cron job a cada 4h (Background Schedule nativo do OpenFang).
- **Missão:** Analisar resumos das interações passadas do usuário com o Líder, varrer extrações de fatos temporários e formatar *MD/Zettelkasten* que será gravado de volta na ponta do cofre via OpenViking.
- **Tools Integradas:** `json_formatter`, `openviking_write`, `openviking_merge_knowledge`.

### 1.4 `operator.toml` (O Agente Operador / FinOps)
*Mão na massa para resolver problemas host-side.*
- **LLM Engine:** `gemini-2.5-flash`
- **Gatilhos:** Acionado pelo líder ou erro detectado no webhook.
- **Missão:** Interagir diretamente com a CLI da VPS para poupar custos de API.
- **Tools Integradas:** `shell_execute_restricted` (Com whitelist restrita: `gemini-cli`, `cat /var/log/*`, `docker ps`).

## 2. Construção Crítica de Tools Customizadas (Habilidades)

Para que as Hands conversem verdadeiramente com seu ecossistema, as seguintes ferramentas devem ser integradas/desenvolvidas como extensões WASM ou nativas do OpenFang:

### A Ferramenta: `openviking_bridge`
- **Por quê?** O OpenFang precisa tratar o OpenViking não como uma API de chat, mas como um banco de dados contextual (Filesystem Paradigm).
- **Implementação:** Desenvolveremos uma *Capability Tool* em Rust ou usaremos as extensões de scripts permitidas que encapsula as requisições para a API do OpenViking, permitindo que os agentes peçam arquivos via o pseudo-protocolo `viking://`.

### A Ferramenta:  `finops_cli_delegator`
- **Por quê?** Uma ferramenta especializada atachada ao `operator.toml`. Em vez de usar a Tool base de terminal do OpenFang indiscriminadamente, criaremos um *macro* chamado "Delegate to Gemini-CLI".
- **Implementação:** A tool empacota a pergunta do Agente, encontra o log apontado no diretório `/app/logs_mounted`, e monta silenciosamente a sintaxe `gemini-cli <prompt> <anexo>`. Retorna a resposta crua para o OpenFang. Pura arbitragem de custo de tokens.

### A Ferramenta:  `mcp_gateway`
- **Por quê?** Integrações como Calendar (agenda) e Youtube Search (Curadoria).
- **Implementação:** Acoplaremos Servidores MCP locais (TypeScript ou Python) que exponham as *tools* padrão do Google/YouTube ao core Rust do OpenFang. Assim centralizando dependências e credenciais de nuvem em poucos arquivos ambientais.

## 3. Dinâmica de Execução Diária: O Fluxo Zettelkasten

Para simular o que descrevemos, observe como um "Wake-Up" opera:
1. **(Usuário Telegram):** "Pode pegar aqueles links de arquitetura que achei ontém e criar um mapa visual?" -> Aciona o bot integrado ao Maestro-Líder.
2. **(Líder):** Executa a tool `openviking_search("user_links_yesterday")`.
3. O OpenViking usa o **Ollama/nomic-embed** para achar o fato de memória nas anotações `/Inbox` do Obsidian de ontem de maneira *Zero-Token*.
4. **(Líder):** Lê a URL e delega à task pro agente *Arquivista* gerar o markdown Zettelkasten.
5. **(Arquivista):** Formata a Zettelkasten puramente estruturada, e aciona a tool `openviking_write()` para criar uma nova nota `/KnowledgeBase/...`. Retorna o link ao Líder.
6. **(Líder Telegram):** Notifica o usuário com link da nova nota gerada. Custo minimizado. Contexto total maximizado.
