# MEMORY.md - Architect

## Estrutura de Memória

### Short-Term Memory (Context Window)
**Tipo:** Contexto da análise atual  
**Retenção:** Duração da sessão  
**Limite:** ~128k tokens (gemini-2.5-pro)  

**O que armazena:**
- Código lido durante análise
- Notas de análise em andamento
- Contexto do request
- Descobertas intermediárias

---

### Long-Term Memory (OpenViking)
**Tipo:** Base vetorial de arquitetura  
**Retenção:** Permanente  
**Acesso:** Via `openviking_search_deep`  

**O que armazena:**
- Decisões arquiteturais passadas (ADRs)
- Análises anteriores de projetos
- Padrões identificados
- Recomendações históricas

**Namespace:** `architect/knowledge`  

**Exemplo de query:**
```python
openviking_search_deep(
  query="decisão arquitetural microsserviços WappTV 2024",
  namespace="architect/knowledge"
)
```

---

## Ciclo de Vida da Análise

### 1. Captura
- Código é lido e processado
- Padrões são identificados
- Code smells são catalogados

### 2. Análise
- Análise profunda em tempo real
- Comparação com padrões conhecidos
- Identificação de trade-offs

### 3. Persistência (via Archivist)
- Relatório é formatado
- ADRs são documentados
- Conhecimento é arquivado em OpenViking

### 4. Recuperação
- Análises futuras consultam histórico
- Evolução arquitetural é rastreada
- Decisões são contextualizadas

## Contexto Retido

### Sessão Atual
- Código completo do projeto analisado
- Notas de análise intermediárias
- Descobertas e insights

### Permanente
- ADRs (Architecture Decision Records)
- Relatórios de análise passados
- Padrões de arquitetura documentados
- Decisões e suas justificativas

## Padrões de Acesso

### Antes de Analisar
```
1. Buscar análises anteriores do mesmo projeto
2. Recuperar ADRs relacionados
3. Entender contexto histórico
4. Iniciar análise informada
```

### Durante Análise
```
1. Manter código em contexto
2. Acumular insights
3. Documentar descobertas
```

### Após Análise
```
1. Formatar relatório completo
2. Enviar para Archivist persistir
3. Atualizar base de conhecimento
```

## Namespace Específico

```
architect/
├── knowledge/          # Decisões e padrões
├── analyses/          # Relatórios de análise
├── adrs/             # Architecture Decision Records
└── patterns/         # Padrões identificados
```
