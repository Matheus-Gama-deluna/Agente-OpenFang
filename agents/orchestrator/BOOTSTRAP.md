# BOOTSTRAP.md - Orchestrator

## Inicialização do Agente

### Passo 1: Carregamento de Configuração
```
1. Ler HAND.toml
2. Validar schema
3. Carregar variáveis de ambiente
4. Inicializar conexões
```

### Passo 2: Setup de Memória
```
1. Verificar integridade do obsidian-bridge
2. Ping em http://localhost:11434 (Ollama)
3. Carregar cache de contexto recente
4. Validar integridade
```

### Passo 3: Setup de Ferramentas
```
1. Registrar ferramentas disponíveis
2. Validar credenciais MCP
3. Testar conectividade (ping leve)
4. Configurar timeouts
```

### Passo 4: Setup de Triggers
```
1. Registrar webhooks (se aplicável)
2. Configurar listeners Telegram
3. Ativar modo "mention detection"
4. Inicializar fila de mensagens
```

### Passo 5: Registro de Agentes Subordinados
```
1. Verificar existência de HAND.toml em:
   - agents/architect/HAND.toml
   - agents/archivist/HAND.toml
   - agents/operator/HAND.toml
   - agents/synchronizer/HAND.toml
2. Validar schemas
3. Pré-carregar configurações
4. Status: READY
```

## Sequência de Boot

```
[START] → [Load Config] → [Setup Memory] → [Setup Tools]
                                           ↓
[READY] ← [Register Agents] ← [Setup Triggers]
```

## Validações de Saúde

### Checklist de Inicialização
- [ ] Configuração válida
- [ ] Conexão local Ollama/Bridge OK
- [ ] Credenciais válidas (Gemini, Groq)
- [ ] Webhooks respondendo
- [ ] Agentes subordinados detectados
- [ ] Memória acessível

### Fallbacks
- Se Obsidian-Bridge indisponível: operar sem recuperação de longo prazo, relying só no contexto
- Se webhook falhar: operar em modo polling
- Se agente subordinado não encontrado: ignorar, não falhar

## Logs de Bootstrap

```
[INFO] Orchestrator boot iniciado
[INFO] Config carregada: agents/orchestrator/agent.toml
[INFO] Obsidian-Bridge inicializado
[INFO] 4 agentes e 4 hands de produtividade detectados
[INFO] Webhooks ativos
[INFO] READY para processar requests
```
