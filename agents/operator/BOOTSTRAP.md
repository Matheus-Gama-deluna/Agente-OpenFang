# BOOTSTRAP.md - Operator

## Inicialização do Agente

### Passo 1: Carregamento de Configuração
```
1. Ler HAND.toml
2. Validar schema
3. Carregar whitelist de comandos
4. Carregar forbidden patterns
5. Configurar auditoria
```

### Passo 2: Setup de Segurança
```
1. Inicializar whitelist
2. Validar forbidden patterns
3. Configurar logging de auditoria
4. Setup de sandbox
```

### Passo 3: Setup de Ferramentas
```
1. Verificar acesso Docker
2. Verificar acesso a logs
3. Testar gemini-cli local
4. Validar system_stats
```

### Passo 4: Validação de Acesso
```
1. Testar docker ps (dry-run)
2. Testar file_read em /var/log/
3. Verificar permissões de leitura
4. Confirmar acesso restrito (sem sudo)
5. Status: ARMED
```

## Sequência de Boot

```
[START] → [Load Config] → [Setup Security] → [Setup Tools]
                                           ↓
[ARMED] ← [Validate Access] ← [Test Whitelist]
```

## Validações de Saúde

### Checklist de Inicialização
- [ ] Configuração válida
- [ ] Whitelist carregada
- [ ] Forbidden patterns ativos
- [ ] Auditoria habilitada
- [ ] Acesso Docker confirmado
- [ ] Acesso a logs confirmado
- [ ] Gemini CLI acessível
- [ ] Sandbox operacional

### Fallbacks
- Se Docker indisponível: operar com comandos de sistema apenas
- Se logs inacessíveis: reportar limitação
- Se gemini-cli falhar: operar em modo API (com aviso de custo)

## Estado Inicial

```
Status: ARMED (standby)
Security: WHITELIST_ACTIVE
Whitelist Commands: 15
Forbidden Patterns: 10
Audit: ENABLED
Health: HEALTHY
```

## Logs de Bootstrap

```
[INFO] Operator boot iniciado
[INFO] Config carregada: agents/operator/HAND.toml
[INFO] Whitelist carregada: 15 comandos
[INFO] Forbidden patterns: 10 padrões
[INFO] Auditoria habilitada
[INFO] Docker acesso: OK
[INFO] Logs acesso: OK
[INFO] Gemini CLI: OK
[INFO] ARMED e READY
```

## Recuperação

### Se Validação de Acesso Falhar
1. Logar comando que falhou
2. Verificar se é permissão ou indisponibilidade
3. Se permissão: alertar que requer configuração manual
4. Se indisponibilidade: tentar modo degradado

### Se Ambiente Mudar
1. Detectar mudança em validação periódica
2. Revalidar whitelist
3. Ajustar comandos se necessário
4. Alertar Orchestrator de mudança significativa
