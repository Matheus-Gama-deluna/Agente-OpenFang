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

### Long-Term Memory (OpenViking)
**Tipo:** Base vetorial persistente  
**Retenção:** Permanente  
**Acesso:** Via `openviking_read_abstract`  

**O que armazena:**
- Preferências do usuário
- Histórico de decisões importantes
- Padrões de interação
- Configurações de projetos
- Resumos de análises anteriores

**Namespace:** `orchestrator/context`  

**Exemplo de query:**
```python
openviking_read_abstract(
  query="preferências usuário sobre comunicação",
  namespace="orchestrator/context"
)
```

---

## Ciclo de Vida da Memória

### 1. Captura
- Interações são processadas em tempo real
- Fatos importantes são extraídos automaticamente
- Contexto é mantido na janela de contexto

### 2. Processamento
- Agente Archivist processa a cada 4 horas
- Formata em Zettelkasten
- Salva em OpenViking com embeddings

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
2. Se insuficiente, buscar em OpenViking (long-term)
3. Combinar contextos para decisão informada
```

### Escrita (via Archivist)
```
1. Enviar resumo para Archivist
2. Archivist formata como Zettelkasten
3. Persiste em OpenViking
4. Retorna ID da nota
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

### Cache de Consultas
- Resultados de `openviking_read` são cacheados por 5 min
- Evita múltiplas consultas idênticas
- Invalidado quando Archivist escreve nova nota
