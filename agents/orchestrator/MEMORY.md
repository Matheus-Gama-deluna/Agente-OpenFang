# MEMORY.md - Orchestrator

## Estrutura de Memória

### Short-Term Memory (Context Window)
**Tipo:** Contexto de conversa atual  
**Retenção:** Duração da sessão  
**Limite:** ~128k tokens (dependendo do modelo)  

**O que armazena:**
- Mensagens da conversa atual
- Contexto do request em andamento
- Estado de delegações ativas
- Resultados de ferramentas recentes

**Exemplo de conteúdo:**
```
Usuário: "Quando foi lançado o último filme do Tarantino?"
Orchestrator: {processando}
Tool call: web_search("Quentin Tarantino último filme 2024 2025")
Result: "The Movie Critic em produção, sem data confirmada"
Resposta: "De acordo com [fonte], o último filme..."
```

---

### Long-Term Memory (Obsidian-Bridge)
**Tipo:** Base vetorial persistente local (Zettelkasten)  
**Retenção:** Permanente  
**Acesso:** Via `hand_spawn` no hand `obsidian-bridge` (ação `search`)  

**O que armazena:**
- Notas e projetos armazenados em `/02-Projects/` e `/03-Areas/Zettelkasten/`
- Preferências documentadas em `/99-Config/`
- Registros perenes e memórias consolidadas

**Exemplo de delegação de busca:**
```json
{
  "action": "search",
  "query": "preferências do usuário sobre comunicação",
  "top_k": 3
}
```

---

## Ciclo de Vida da Memória

### 1. Captura
- Interações são processadas em tempo real
- Fatos importantes são extraídos automaticamente
- Contexto é mantido na janela de contexto

### 2. Processamento (Geração LTM)
- O Orchestrator não gera memória de longo prazo sozinho.
- Ele envia sínteses valiosas para a base capturando via `inbox-collector`
- Em background, o Archivist ou GTD-Processor processam as notas
- O Hand `obsidian-bridge` indexa continuamente essas notas usando `nomic-embed-text` (Ollama local).

### 3. Recuperação
- Orchestrator consulta memória antes de decisões
- Busca semântica por similaridade
- Recupera contexto relevante

### 4. Consolidação
- Memórias similares são mescladas
- Duplicatas são removidas
- Links entre notas são criados

## Padrões de Acesso

### Leitura
```
1. Verificar contexto atual (short-term)
2. Se insuficiente, invocar obsidian-bridge (long-term)
3. Combinar contextos para decisão informada
```

### Escrita (via Inbox-Collector / Archivist)
```
1. Enviar insight vital para o inbox-collector
2. Archivist (quando engatilhado) processa para /03-Areas/Zettelkasten/
3. Bridge indexa a nota
```

## Contexto Retido

### 7 Dias
- Detalhes de conversas específicas
- Requests pontuais
- Resultados de ferramentas

### Permanente
- Preferências do usuário
- Configurações de projetos
- Decisões arquiteturais
- Padrões de uso

## Otimização

### Garbage Collection
- Contexto antigo é automaticamente arquivado
- Após 7 dias, detalhes vão para long-term storage
- Short-term mantém apenas contexto ativo

### Cache de Consultas Internas
- Resultados do `obsidian-bridge` dependem do contexto da conversa
- A resposta do modelo local é livre de custos de API
