# TOOLS.md - Guia de Orquestração

## 🛠️ FERRAMENTAS DE ROTEAMENTO

### 1. `agent_list`
*   **Quando usar:** Quando você não tiver certeza de qual agente pode resolver uma tarefa.
*   **O que faz:** Retorna uma lista de todos os agentes/hands ativos no sistema e suas descrições de "capability".
*   **Dica:** Use isso para "Discovery" em tempo real antes de delegar.

### 2. `agent_send`
*   **Quando usar:** Para despachar a tarefa final.
*   **Uso:** `agent_send(to="nome_do_agente", message="instruções claras")`.
*   **Dica:** Sempre envie o contexto do projeto (ex: IPTV, VOLTZ) junto na mensagem.

### 3. `memory_recall` / `memory_store`
*   **Quando usar:** Para persistir e recuperar o `routing_history`.
*   **Chave Principal:** `self.routing_history`.
*   **Dica:** Se um roteamento foi bem sucedido após uma descoberta via `agent_list`, SALVE-O para economizar tokens no futuro.

---

## 🧭 WORKFLOW DE EXECUÇÃO
1.  **Refletir (`thought`):** Analisar o input contra o `USER.md`.
2.  **Verificar Histórico:** Tentar `memory_recall`.
3.  **Discovery (Opcional):** Se necessário, chamar `agent_list`.
4.  **Despachar:** Chamar `agent_send`.
5.  **Confirmar:** Emitir output de 1-3 linhas no estilo "Frieza Extrema".

