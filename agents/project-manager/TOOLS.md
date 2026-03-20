# TOOLS.md - Guia de Ferramentas Linear

## 🛠️ LINEAR CLI (`scripts/linear-cli.js`)

### 1. `createIssue`
*   **Ação:** Cria um ticket no Linear.
*   **Parâmetros:** "Título", "Descrição", "TeamID", JSON de Opções.
*   **Regra:** Sempre inclua o link para a nota do Obsidian na descrição.

### 2. `teams` / `projects` / `states`
*   **Ação:** Descoberta de estrutura.
*   **Uso:** Use para mapear onde as tarefas devem ser criadas e quais os status disponíveis (Todo, In Progress, Done).

### 3. `updateIssue`
*   **Ação:** Mudar status ou prioridade.
*   **Uso:** Para sincronizar progresso reportado ou detectado.

---

## 🤝 COMUNICAÇÃO AGÊNTICA

### 4. `agent_send` (`organizer`)
*   **Uso:** Enviar o ID da issue criada (`linear_id`) para que o `organizer` atualize o YAML da nota no Obsidian.
