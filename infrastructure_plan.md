# Plano Detalhado de Infraestrutura: Agent OS (VPS)

Este documento destrincha o setup técnico esperado para erguer o ecossistema do *Maestro Agent OS* em uma arquitetura limpa, visando altíssima tolerância a falhas na infraestrutura bare-metal.

## 1. Ambiente Principal: Servidor Contabo
- **SO Recomendado:** Ubuntu 22.04 LTS ou 24.04 LTS (limpo).
- **Gerenciador de Container:** Coolify (v4+).
  - O Coolify atuará como nosso *PaaS local*, roteando subdomínios, gerenciando certificados SSL (Let’s Encrypt nativo) e entregando CI/CD automático do repositório.

## 2. Topologia de Serviços no Coolify (Docker Compose)

Teremos um stack principal orquestrado pelo *Coolify*.
Os seguintes serviços devem subir na mesma rede privada (`coolify-network`):

### 2.1 Módulo de Core / Orquestração (OpenFang)
- **Imagem Oficial:** `rightnowai/openfang:latest` (ou compilação local Rust)
- **Recursos Alocados:** Mínimos. Rust exige <100MB RAM no boot.
- **Armazenamento:** Volume montado para banco de dados local (SQLite) onde os *logs de orquestração* e dados transientes das *Hands* residem.
- **Segurança (AppArmor/Privileged):** O *container* do OpenFang pode precisar rodar capacidades especiais caso invoque o `shell_execute` para ferramentas como `docker` host ou `gemini-cli`. Isso requer planejamento de diretórios montados limitados (`/app/workspace`).

### 2.2 Módulo de Memória de Longo Prazo (OpenViking)
- O **OpenViking** requer uma base vetorial acoplada em conjunto com o suporte do SQLite/Postgres.
- Ele deve injetar dados da pasta crua do seu *Zettelkasten*.
- **Volumes:** É impreterível que seu repositório de notas (Obsidian) seja clonado ou sincado para uma pasta na VPS (`/data/obsidian_vault/`) montada como *Read-Only* para o OpenViking fazer a *ingestão* contínua.

### 2.3 Módulo de Embeddings e Transcrição Local
*Para quebrar custos de indexação e processamento de fala:*
1. **Ollama (CPU Mode):**
   - Rodando como serviço no Coolify focado em fornecer a API compatível com OpenAI.
   - Modelo carregado no *warm-up*: `nomic-embed-text` ou equivalente para transformar as notas do Obsidian em vetores sem gastar 1 centavo via API.
2. **Whisper.cpp (Micro-serviço API):**
   - Setup construído via `whisper.cpp` com servidor *FastAPI* ou Go acoplado rodando o modelo (ex.: `ggml-small.bin`). Fornecerá um *endpoint* HTTP `/transcribe` acionado exclusivamente pelo gateway do Telegram no *Maestro*.

## 3. Integração com Gemini CLI (Arbitragem de Custo - FinOps)
Para processos super densos (como mandar um log inteiro do Node.js de erro WappTV), evitaremos o tráfego da API REST para ignorar as métricas de token *Pay-As-You-Go*.

**Passo a passo da CLI na Infraestrutura:**
1. A **Gemini CLI** será instalada no SO *host* (Ubuntu) via npm ou Go.
2. Configuração do `gcloud auth login` estático usando a cota da sua assinatura *Google AI Pro* existente.
3. Compartilhar os executáveis binários via volume (ou usar Dood - *Docker Out of Docker*) com o *container* do OpenFang. Assim, a instrução `shell_execute("gemini-cli -prompt 'Analise esse log' -f error.log")` delegará a computação base sem que o Agente Operador gaste context window no pipeline primário.

---
## Considerações Críticas (Segurança)
1. **Firewall (UFW):** Como temos serviços locais (Ollama e OpenViking API), o UFW deve bloquear severamente o tráfego entrante nas portas 11434 (Ollama) e correlatas. O trafego deve ser estritamente roteado pelo *Coolify Proxy / Traefik*.
2. **Backups Diários:** O SQLite do OpenViking que cruza os vetores deve ter *backup* de snapshot usando o nativo do Coolify ou um agente *Cron* para o S3/Google Drive.
