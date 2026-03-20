# TOOLS.md - Guia de Ferramentas de Ingestão

## 📥 TICKTICK CLI (`scripts/ticktick.js`)

### 1. `tasks --json`
*   **Uso:** Varredura periódica para buscar "lixo digital" na lista Inbox.
*   **Filtro:** Ignorar tarefas com a tag `captured`.

### 2. `task "Título" --list "ID" --content "Descrição"`
*   **Uso:** Criar lembretes físicos no TickTick após o Sensemaking, se o Matheus aprovar.

### 3. `complete <taskId>`
*   **Uso:** Marcar como concluído no TickTick após a ideia ser enviada ao `organizer` e salva no Obsidian.

---

## 🤝 COMUNICAÇÃO SUPERVISIONADA

### 4. `agent_send` (`organizer`)
*   **Uso:** Enviar o pacote final (Markdown + YAML) para o supervisor salvar após aprovação do Matheus.
