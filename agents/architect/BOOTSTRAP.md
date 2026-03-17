# BOOTSTRAP.md - Architect

## Inicialização do Agente

Como agente sob demanda, o Architect não mantém estado persistente entre invocações.

### Passo 1: Recebimento de Invocação
```
1. Orchestrator chama spawn_hand("architect", task, context)
2. Contexto é carregado na janela de contexto
3. Configurações são aplicadas
```

### Passo 2: Setup de Contexto
```
1. Receber repository/path do contexto
2. Receber foco da análise
3. Receber restrições conhecidas
```

### Passo 3: Consulta de Memória
```
1. Buscar análises anteriores do projeto
2. Recuperar ADRs relacionados
3. Carregar padrões de arquitetura conhecidos
```

### Passo 4: Início de Análise
```
1. Validar acesso ao repositório
2. Confirmar ferramentas disponíveis
3. Iniciar leitura do código
4. Status: ANALYZING
```

## Sequência de Boot

```
[INVOKED] → [Load Context] → [Query Memory] → [Start Analysis]
                                              ↓
[READY] ← [Return Report] ← [Generate Documentation]
```

## Estado durante Análise

```
Status: ANALYZING
Progress: [reading codebase] → [identifying patterns] → [researching] → [synthesizing] → [documenting]
Time Elapsed: {timestamp}
```

## Validações

### Checklist de Inicialização
- [ ] Contexto recebido do Orchestrator
- [ ] Repositório acessível
- [ ] Memória consultada
- [ ] Ferramentas disponíveis

### Fallbacks
- Se repositório indisponível: solicitar ao Orchestrator
- Se OpenViking indisponível: analisar sem contexto histórico
- Se web_search indisponível: usar conhecimento prévio

## Logs

```
[INFO] Architect invocado pelo Orchestrator
[INFO] Contexto carregado: projeto=WappTV, foco=performance
[INFO] Análises históricas recuperadas: 3
[INFO] Iniciando leitura do codebase
[INFO] Código lido: 47 arquivos, 12k linhas
[INFO] Identificando padrões...
[INFO] Gerando relatório...
[INFO] Relatório completo, retornando ao Orchestrator
```
