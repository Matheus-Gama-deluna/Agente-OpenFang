# BOOTSTRAP.md - Synchronizer

## Inicialização do Agente

### Passo 1: Carregamento de Configuração
```
1. Ler HAND.toml
2. Validar schema
3. Carregar mapeamento de projetos
4. Carregar timezone (America/Sao_Paulo)
5. Configurar date_parser
```

### Passo 2: Setup de Integrações
```
1. Verificar conexão TickTick API
2. Carregar lista de projetos
3. Validar credenciais
4. Testar criação de tarefa (dry-run)
5. Configurar OpenViking para backup
```

### Passo 3: Setup de Cron
```
1. Registrar schedule (0 7 * * *)
2. Configurar timezone
3. Validar próximo trigger
4. Inicializar timer
```

### Passo 4: Validação
```
1. Testar date_parser
2. Testar mapeamento de projetos
3. Confirmar acesso a ambos os sistemas
4. Status: READY
```

## Sequência de Boot

```
[START] → [Load Config] → [Setup Integrations] → [Setup Cron]
                                               ↓
[READY] ← [Validate] ← [Test Mappings]
```

## Validações de Saúde

### Checklist de Inicialização
- [ ] Configuração válida
- [ ] TickTick API conectada
- [ ] Projetos mapeados (5 projetos)
- [ ] OpenViking acessível
- [ ] Date parser funcionando
- [ ] Cron registrado (07:00)
- [ ] Timezone configurado (UTC-3)
- [ ] Fallbacks definidos

### Fallbacks
- Se TickTick API falhar: operar em modo "Obsidian-only"
- Se projeto não encontrado: usar "p_Pessoal" como padrão
- Se date_parser ambíguo: usar interpretação conservadora

## Estado Inicial

```
Status: ACTIVE
Cron Schedule: 0 7 * * *
Next Run: Amanhã 07:00 (Brasília)
Timezone: America/Sao_Paulo
Projects Mapped: 5
Health: HEALTHY
```

## Logs de Bootstrap

```
[INFO] Synchronizer boot iniciado
[INFO] Config carregada: agents/synchronizer/HAND.toml
[INFO] TickTick API conectada
[INFO] Projetos mapeados: p_WappTV, p_VOLTZ, p_DEK, p_Pessoal, p_Maestro
[INFO] OpenViking acessível
[INFO] Date parser configurado (pt-BR)
[INFO] Cron registrado: 0 7 * * * (sumário matinal)
[INFO] Timezone: America/Sao_Paulo (UTC-3)
[INFO] READY para sincronização
```

## Recuperação

### Se TickTick Falhar na Inicialização
1. Retry com backoff (3 tentativas)
2. Se persistente: iniciar em modo "Obsidian-only"
3. Alertar Orchestrator da limitação
4. Tentar reconexão a cada 10 minutos

### Se Projetos Não Encontrados
1. Logar projetos esperados vs encontrados
2. Criar mapeamento parcial se possível
3. Usar "p_Pessoal" para projetos não mapeados
4. Alertar Orchestrator para verificação manual
