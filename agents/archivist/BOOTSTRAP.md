# BOOTSTRAP.md - Archivist

## Inicialização do Agente

### Passo 1: Carregamento de Configuração
```
1. Ler HAND.toml
2. Validar schema
3. Carregar configurações de cron
4. Verificar conexão OpenViking
```

### Passo 2: Setup de Memória
```
1. Conectar ao OpenViking
2. Verificar namespaces de pastas
3. Validar estrutura Zettelkasten
4. Carregar índices de busca
```

### Passo 3: Setup de Ferramentas
```
1. Registrar ferramentas openviking_*
2. Validar acesso de escrita
3. Configurar geradores de YAML/JSON
4. Setup de embedding generator
```

### Passo 4: Inicialização do Cron
```
1. Registrar schedule (0 */4 * * *)
2. Verificar fila de resumos pendentes
3. Inicializar batch processor
4. Status: READY
```

## Sequência de Boot

```
[START] → [Load Config] → [Setup Memory] → [Setup Tools]
                                           ↓
[READY] ← [Init Cron] ← [Validate Access]
```

## Validações de Saúde

### Checklist de Inicialização
- [ ] Configuração válida
- [ ] Conexão OpenViking OK
- [ ] Permissão de escrita confirmada
- [ ] Estrutura de pastas válida
- [ ] Índices de busca carregados
- [ ] Cron registrado

### Fallbacks
- Se OpenViking indisponível: retry a cada 30s, alertar após 5 tentativas
- Se estrutura inválida: criar pastas padrão automaticamente
- Se permissão negada: logar erro crítico, abortar

## Estado Inicial

```
Status: ACTIVE (background)
Mode: CRON_ENABLED
Last Run: N/A
Next Run: Calculando...
Queue Size: 0
Health: HEALTHY
```

## Logs de Bootstrap

```
[INFO] Archivist boot iniciado
[INFO] Config carregada: agents/archivist/HAND.toml
[INFO] OpenViking conectado
[INFO] Namespaces validados: /01-Inbox/, /02-Projetos/, /03-Zettelkasten/, /99-Config/
[INFO] Índices de busca carregados
[INFO] Cron schedule registrado: 0 */4 * * *
[INFO] READY para processar resumos
```

## Recuperação

### Se Falha na Inicialização
1. Logar estado atual
2. Tentar retry com backoff exponencial
3. Se persistente: alertar Orchestrator
4. Modo degradado: processar sob demanda apenas

### Se OpenViking Falhar Durante Execução
1. Buffer resumos em memória local
2. Retry a cada 5 minutos
3. Após 3 tentativas: alertar Orchestrator
4. Manter fila até recuperação
