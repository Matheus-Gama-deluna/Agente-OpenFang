# Plano de Integração: Sistema Nervoso Pessoal (Obsidian + TickTick)

A base do "Fricção Zero" no **Maestro Agent OS** consiste em unir a memória semântica e perene (Obsidian) à gestão executiva de tempo e tarefas (TickTick), sem exigir que você abra múltiplos aplicativos para atualizar status de projetos.

Abaixo, a arquitetura detalhada e práticas de como construiremos esse Segundo Cérebro assistido por IA:

## 1. O Componente de Banco de Conhecimento (Obsidian / OpenViking)

O Obsidian não será penas um repositório passivo de notas Markdown; ele atuará como o banco de dados (OpenViking Context DB) no qual os Agentes ganham "vida" (Memória). O Obsidian local rodará na máquina desktop, enquanto os arquivos sincronizam bidirecionalmente com a VPS (Dropbox, GDrive ou Syncthing).

### 1.1 Metodologia e Estrutura de Cofre (Vault)
Para que o `nomic-embed-text` e o OpenViking consigam varrer o Obsidian rápido, adotaremos um padrão semi-rígido inspirado no método *PARA* adaptado ao Zettelkasten:

- `/01-Inbox`: Onde o Maestro Líder joga rapidamente ideias cruas e fatos capturados por voz ou texto (Telegram).
- `/02-Projetos`: Notas estritamente temporárias e acionáveis (ex: `WappTV_API.md`). Projetos *sempre* têm tarefas no TickTick.
- `/03-Zettelkasten (KB)`: O "Segundo Cérebro" real. Notas atômicas permanentemente formatadas pelo Agente *Arquivista*.
- `/99-Config`: A pasta mais crítica para os agentes. Onde residirá o arquivo mestre (ex: `viking://user/preferences.md`) que dita seus interesses na semana (para o agente *Curador* agir) e o seu "Personal Operating Procedure".

### 1.2 Ferramentas (Obsidian Pluggins Pessoais)
Apesar do OpenFang ler de fora, para sua UX visual, recomendamos o uso de plugins não obstrutivos:
- **Dataview:** O OpenFang/Arquivista gerará blocos metadados (YAML frontmatter) nos Markdowns para gerar Dashboards automáticos.
- **Smart Connections:** (Opcional, lado cliente) Para você descobrir visualmente conexões na interface, similar ao que o OpenViking faz em *backend*.

## 2. O Módulo de Execução (O Sincronizador & TickTick)

O TickTick é um dos poucos gerenciadores com uma API Rest robusta para tarefas e calendário. Aqui, o Maestro e o TickTick criarão um laço fechado.

### 2.1 A Ferramenta: `mcp_ticktick_bridge`
Será desenvolvido ou acoplado um **MCP Server (Model Context Protocol)** específico para a API não oficial (ou oficial, havendo request) do TickTick. 

O servidor proverá 4 Tools Críticas para a equipe de agentes:
1. `ticktick_add_task(name, date, project_id, priority)`
2. `ticktick_get_today()`
3. `ticktick_complete_task(task_id)`
4. `ticktick_read_summary(project_name)`

### 2.2 O Agente: Sincronizador (`synchronizer.toml`)
Este agente em específico roda em cronjobs temporizados (Schedule do OpenFang) e possui as credenciais do TickTick. Ele preenche a ponte (Bridge) entre intenção livre (Obsidian/Telegram) e a execução metrificada (TickTick).

## 3. Playbook Prático de Workflow (Fricção Zero)

A verdadeira "Mágica" na integração ocorre na sinergia entre o Maestro-Líder, a Memória e as Tarefas.

**Cenário 1: Reunião / Áudio Rápido (Inbox -> Tarefa)**
1. Você manda um áudio de 15s no Telegram: *"Lembre de revisar o endpoint de rotas da WappTV com o Pedro amanhã à tarde."*
2. Maestro-Líder (via *Whisper*) escuta, entende a intenção de agendamento/projeto e classifica como ação.
3. Líder chama a Tool: `ticktick_add_task("Revisar rotas (WappTV)", "amanhã 15:00", p_WappTV, High)`.
4. Paralelamente, chama a Tool da API OpenViking e grava em `/01-Inbox` de forma atômica para contexto futuro.

**Cenário 2: Planejamento Profundo (TickTick -> Arquiteto -> Obsidian)**
1. Você solicita ao Líder: *"Maestro, inicie o planejamento de arquitetura dos Agentes, analise as minhas tarefas pendentes disso e gere um roadmap estrutural baseado no que discutimos na semana passada."*
2. O Maestro-Líder terceiriza: chama o `Sincronizador` para trazer a lista atualizada do TickTick do Folder do projeto.
3. Líder envia o histórico de tarefas abertas para o `Maestro-Arquiteto`.
4. Arquiteto invoca `openviking_search_deep("Agent OS Architecture")` minerando o Zettelkasten `/KB` extraindo ideias.
5. Arquiteto "Raciocina" sobre como unir o estado do TickTick com o ideal do Zettel e produz o Plano Massivo Markdown.
6. Líder salva as notas refinadas na pasta `/02-Projetos` nativamente sem que você abra um editor de texto.

**Cenário 3: Sumário Matinal (Daily Fricção Zero)**
1. Às 07:00H, via Cronjob da VPS, o Maestro acorda.
2. O Líder faz pooling no TickTick (`ticktick_get_today`).
3. O Arquivista lê o `viking://user/preferences.md` e os arquivos Recentes do Obsidian.
4. Você recebe no Telegram um briefing direto e caloroso: 
*"Bom dia! Hoje temos 3 gargalos críticos da WappTV no TickTick. Baseado nas anotações que você fez no fds, quer que eu já escreva o boilerplate no repositório com o Maestro-Arquiteto?"*

## 4. Próximos Passos (Infraestrutura Prática)
A parte crítica para fazer isso funcionar é estabilizar o sync do Obsidian *Headless* no Coolify para que a API consiga agir sobre ele.

1. Escolher a via de sincronicidade: **Syncthing (Bare-Metal) vs. Github Private Repo (Git Sync)**. O GitHub costuma ser mais performático em servidores Linux via webhook/cron git pull do que clientes P2P pesados no *Docker*.
2. Registrarmos uma App (Client ID) no Portal Dev do TickTick.
