# Guia Completo: Criação de Agentes de IA em Português Brasileiro
## Baseado em Pesquisa de Melhores Práticas 2024-2025

---

## 1. 🎯 Padrões de Design de Agentes

### 1.1 Handoff Orchestration (Delegação Inteligente)
O padrão **handoff** (também conhecido como routing, triage, transfer) permite que um agente supervisor delegue tarefas dinamicamente para agentes especializados.

**Quando usar:**
- Quando o agente ótimo para uma tarefa não é conhecido antecipadamente
- Quando requisitos só ficam claros durante o processamento
- Para garantir que tarefas cheguem ao agente mais capacitado

**Implementação no OpenFang:**
```toml
[triggers]
type = ["invocation"]
invoked_by = ["orchestrator"]
```

### 1.2 Supervisor Pattern (Supervisor/Delegador/Executor)
Arquitetura de três camadas:
- **Supervisor (Orchestrator)**: Coordena e toma decisões de alto nível
- **Delegador**: Decide qual executor é mais adequado
- **Executor**: Executa tarefas especializadas

**Vantagens:**
- Separação clara de responsabilidades
- Escalabilidade modular
- Fallback automático entre agentes

### 1.3 Padrões de Orquestração (Microsoft/Azure)
Segundo a Microsoft, existem 5 padrões fundamentais:

1. **Sequential**: Agentes executam em sequência, output de um é input do próximo
2. **Concurrent**: Agentes trabalham em paralelo, resultados são agregados
3. **Group Chat**: Múltiplos agentes conversam para resolver problema complexo
4. **Handoff**: Controle é transferido dinamicamente entre agentes
5. **Magentic**: Um agente "magnético" atrai tarefas relacionadas

---

## 2. 🧠 Componentes Essenciais de um Agente

### 2.1 Agente (Agent Module)
- **LLM como cérebro**: Modelo de linguagem com capacidades gerais
- **Prompt Template**: Instruções detalhadas sobre como operar
- **Perfil/Persona**: Define tom, estilo e comportamento (Wang et al. 2023)

**Estratégias de definição de perfil:**
- Handcrafting (manual)
- LLM-generated (automatizado)
- Data-driven (baseado em dados)

### 2.2 Planejamento (Planning)

#### Sem Feedback:
- **Chain of Thought**: Raciocínio passo a passo (single-path)
- **Tree of Thoughts**: Explora múltiplos caminhos (multi-path)

#### Com Feedback:
- **ReAct**: Intercalação de Thought → Action → Observation
- **Reflexion**: Reflexão iterativa baseada em ações passadas

### 2.3 Memória (Memory)

**Tipos:**
- **Short-term**: Contexto atual (limitado pela janela de contexto)
- **Long-term**: Comportamentos passados (vector store externo)
- **Hybrid**: Combinação de ambos para reasoning de longo alcance

**Formatos:**
- Linguagem natural
- Embeddings
- Bancos de dados (SQLite, PostgreSQL)
- Structured lists

---

## 3. 🇧🇷 Configuração para Português Brasileiro

### 3.1 Configurações de Linguagem
```toml
[speech]
language = "pt-BR"
accent = "brazilian"
formality = "neutral"  # ou "formal" para agentes técnicos
tone = "helpful"       # ajustar por agente
```

### 3.2 Personalidade em PT-BR
**Princípios:**
- Use português brasileiro **natural**, evitando traduções literais do inglês
- Adapte formalidade ao contexto (usuário casual vs. documentação técnica)
- Considere expressões idiomáticas brasileiras quando apropriado
- Respeite o fuso horário de Brasília (UTC-3)

### 3.3 Exemplo de System Prompt em PT-BR
```markdown
Você é um assistente especializado. 
- Responda sempre em português brasileiro natural
- Seja cordial mas objetivo
- Use tom [formal/neutro] conforme contexto
- Nunca confirme fatos sem verificar dados atualizados
- Considere fuso horário de Brasília (UTC-3)
```

---

## 4. ✅ Ferramentas de Verificação de Dados/Fatos

### 4.1 Grounding com Google Search (Gemini API)
Permite que o modelo acesse informações em tempo real da web.

**Como funciona:**
1. API envia prompt com ferramenta `google_search` habilitada
2. Modelo decide se busca melhora a resposta
3. Modelo gera queries de busca automaticamente
4. Resultados são processados e sintetizados
5. Resposta inclui `groundingMetadata` com citações

**Implementação:**
```python
# O modelo decide automaticamente quando buscar
grounding_metadata = {
    "webSearchQueries": ["query 1", "query 2"],
    "groundingChunks": [
        {"web": {"uri": "https://...", "title": "Fonte"}}
    ],
    "groundingSupports": [
        {"segment": {...}, "groundingChunkIndices": [0]}
    ]
}
```

### 4.2 RAG (Retrieval-Augmented Generation)
Combine busca em base de conhecimento com geração:
- **Vertex AI Search**: Grounding em documentos empresariais
- **Check Grounding API**: Verifica se resposta está fundamentada em fatos

### 4.3 Checklist de Verificação no System Prompt
```markdown
## 🚫 O que NUNCA fazer
- Não confirme datas sem verificar calendário atual
- Não afirme números/nomes sem buscar fontes
- Não especule sem deixar claro que é especulação
- Não ignore o groundingMetadata quando disponível

## ✅ O que SEMPRE fazer
- Use web_search antes de confirmar fatos
- Cite fontes quando usar dados da web
- Diferencie "confirmado" de "estimado"
- Inclua timestamp da verificação quando relevante
```

---

## 5. 📋 Checklist para Criar Bons Agentes

### 5.1 Definição de Identidade
- [ ] Nome claro e memorável
- [ ] Descrição concisa da função
- [ ] Personalidade definida (tom, estilo, formalidade)
- [ ] Propósito claro e focado

### 5.2 Configuração Técnica
- [ ] Modelo adequado (Flash para velocidade, Pro para complexidade)
- [ ] Temperature apropriada (baixa para precisão, alta para criatividade)
- [ ] Max tokens suficiente para o tipo de output
- [ ] Triggers/gatilhos bem definidos

### 5.3 System Prompt Efetivo
- [ ] Identidade clara nas primeiras linhas
- [ ] Responsabilidades listadas explicitamente
- [ ] Ferramentas disponíveis documentadas
- [ ] Regras de ouro destacadas
- [ ] Exemplos de workflow incluídos
- [ ] O que NUNCA fazer explicitado
- [ ] Idioma configurado (pt-BR)

### 5.4 Ferramentas e Integrações
- [ ] Ferramentas essenciais mapeadas
- [ ] Whitelist de comandos (se aplicável)
- [ ] Integrações externas configuradas
- [ ] Fallbacks definidos

### 5.5 Comportamento e Memória
- [ ] Short-term memory configurada
- [ ] Long-term memory habilitada (OpenViking)
- [ ] Retenção de contexto definida
- [ ] Logging adequado

### 5.6 Segurança e Confiabilidade
- [ ] Whitelist de comandos restrita
- [ ] Padrões proibidos definidos
- [ ] Auditoria habilitada
- [ ] Confirmação para ações destrutivas

---

## 6. 🎯 Framework OpenFang - Especificidades

### 6.1 Estrutura HAND.toml
Todo agente OpenFang precisa de:
```toml
[agent]          # Identidade básica
[model]          # Configuração LLM
[speech]         # Configuração de voz/idioma
[prompt]         # System prompt completo
[triggers]       # Como é ativado
[tools]          # Ferramentas disponíveis
[behavior]       # Comportamento especializado
[memory]         # Configuração de memória
[logging]        # Logs e auditoria
```

### 6.2 Manifesto SOUL.md
Cada agente deve ter um SOUL.md com:
- **Essência**: Quem é este agente
- **Propósito**: Por que existe
- **Personalidade**: Como se comporta
- **Princípios**: Regras internas
- **Relacionamentos**: Como interage com outros
- **Rituais**: Padrões de comportamento
- **Medos**: O que evita
- **Alegrias**: O que valoriza

### 6.3 Modelos Recomendados por Função
| Agente | Modelo | Justificativa |
|--------|--------|---------------|
| Orchestrator | gemini-2.5-flash | Velocidade para decisões rápidas |
| Architect | gemini-2.5-pro | Raciocínio profundo complexo |
| Archivist | gemini-2.5-flash-lite | Velocidade para processamento batch |
| Operator | gemini-2.5-flash | Balance de velocidade e capacidade |
| Synchronizer | gemini-2.5-flash | Eficiência em tarefas rotineiras |

---

## 7. 📚 Referências

1. **Microsoft Learn**: AI Agent Orchestration Patterns - https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
2. **Google AI**: Grounding with Google Search - https://ai.google.dev/gemini-api/docs/google-search
3. **Prompt Engineering Guide**: LLM Agents - https://www.promptingguide.ai/research/llm-agents
4. **OpenFang Framework**: https://github.com/RightNow-AI/openfang
5. **Databricks**: Agent System Design Patterns - https://docs.databricks.com/aws/en/generative-ai/guide/agent-system-design-patterns
6. **Wang et al. 2023**: A Survey on Large Language Model based Autonomous Agents

---

## 8. 💡 Dicas Finais

1. **Comece simples**: Um agente bem feito é melhor que cinco mal feitos
2. **Itere com logs**: Use logs para identificar onde agentes falham
3. **Teste edge cases**: Agentes devem lidar bem com inputs inesperados
4. **Monitore custos**: Use delegação para ferramentas locais quando possível
5. **Documente decisões**: Arquitetura de agentes evolui; mantenha ADRs

---

**Documento gerado em**: Março 2025  
**Baseado em**: Pesquisa de frameworks OpenFang, Microsoft Azure, Google AI e melhores práticas de LLM Agents
