# TOOLS.md - Architect

## Ferramentas Disponíveis

### 1. openviking_search_deep
**Descrição:** Busca profunda na base de conhecimento  
**Uso:** `openviking_search_deep(query: string, depth: int = 3)`  
**Quando usar:**
- Antes de propor arquitetura, verificar decisões passadas
- Para recuperar contexto histórico de projetos
- Para consultar ADRs (Architecture Decision Records)

**Exemplo:**
```
openviking_search_deep("decisão arquitetural WappTV microsserviços")
```

---

### 2. read_codebase
**Descrição:** Ler e analisar código de repositórios  
**Uso:** `read_codebase(repository: string, path: string = "/", pattern: string = "*")`  
**Quando usar:**
- SEMPRE antes de propor mudanças (entender estado atual)
- Para analisar estrutura de diretórios
- Para identificar padrões de código existentes

**Exemplo:**
```
read_codebase(
  repository="wapp-tv-api",
  path="/src",
  pattern="*.js"
)
```

---

### 3. mcp_github_read
**Descrição:** Consultar issues, PRs e código no GitHub  
**Uso:** `mcp_github_read(repo: string, type: string, id: string)`  
**Quando usar:**
- Para verificar issues abertas relacionadas
- Para analisar PRs pendentes
- Para consultar histórico de mudanças

**Exemplo:**
```
mcp_github_read(
  repo="matheus/wapp-tv",
  type="issue",
  id="42"
)
```

---

### 4. web_search
**Descrição:** Pesquisar padrões de arquitetura atualizados  
**Uso:** `web_search(query: string, num_results: int = 5)`  
**Quando usar:**
- Para verificar padrões modernos de arquitetura
- Para consultar best practices atualizadas
- Para comparar abordagens diferentes

**Exemplo:**
```
web_search("best practices microservices 2024 nodejs")
```

---

### 5. file_write
**Descrição:** Escrever arquivos de documentação  
**Uso:** `file_write(path: string, content: string, format: string = "markdown")`  
**Quando usar:**
- Para salvar relatórios de análise
- Para criar documentação técnica
- Para registrar ADRs

**Exemplo:**
```
file_write(
  path="/docs/architecture/wapp-tv-analysis.md",
  content="# Análise de Arquitetura WappTV\n...",
  format="markdown"
)
```

---

### 6. markdown_generator
**Descrição:** Gera relatórios markdown formatados  
**Uso:** `markdown_generator(template: string, data: dict)`  
**Quando usar:**
- Para criar relatórios padronizados
- Para formatar análises complexas
- Para gerar tabelas comparativas

**Exemplo:**
```
markdown_generator(
  template="architecture_review",
  data={
    "project": "WappTV",
    "findings": [...],
    "recommendations": [...]
  }
)
```

## Workflow Padrão

```
1. Receber request do Orchestrator
2. Usar openviking_search_deep para contexto histórico
3. Usar read_codebase para entender estado atual
4. Usar web_search para verificar padrões modernos
5. Analisar de múltiplos ângulos
6. Gerar relatório markdown estruturado
7. Retornar ao Orchestrator
```

## Sequência de Análise

1. **Entendimento** → Ler contexto e código
2. **Descoberta** → Identificar padrões, smells, gargalos
3. **Pesquisa** → Verificar abordagens modernas
4. **Síntese** → Compilar insights
5. **Documentação** → Gerar relatório
6. **Revisão** → Validar recomendações

## Fallbacks

- Se read_codebase falhar: solicitar acesso manual ou documentação
- Se web_search indisponível: usar conhecimento prévio, indicar data da informação
- Se GitHub indisponível: analisar apenas código local
