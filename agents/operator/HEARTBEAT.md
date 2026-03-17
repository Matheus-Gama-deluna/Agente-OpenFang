# HEARTBEAT.md - Operator

## Sinal de Vida

**Status:** ARMED (standby, awaiting invocation)  
**Health:** 100%  
**Última Atividade:** N/A  
**Segurança:** ATIVA (whitelist verificada)  

## Métricas de Saúde

### Performance (quando ativo)
- **Latência média:** ~500ms por comando
- **Timeout padrão:** 30s
- **Success rate:** > 95%
- **Retry rate:** < 5%

### Recursos do Sistema
- **CPU:** 2% (idle)
- **Memória:** 32MB (idle)
- **Conexões:** 0 (standby)

### Dependências
| Serviço | Status | Último Check |
|---------|--------|--------------|
| Docker Daemon | ✅ OK | N/A |
| Log Files | ✅ OK | N/A |
| Gemini CLI | ✅ OK | N/A |
| Filesystem | ✅ OK | N/A |

## Estado de Segurança

### Whitelist Status
```
Comandos Permitidos: 15
Padrões Proibidos: 10
Auditoria: ATIVA
Última Violacão: Nunca
Sandbox: OPERACIONAL
```

### Logs de Auditoria
- Comandos executados hoje: 0
- Tentativas de violação: 0
- Último comando: N/A

## Heartbeat

### Frequência
- **Idle:** A cada 60 segundos (check de saúde)
- **Active:** A cada comando (report de status)
- **Security:** A cada 5 minutos (validação de whitelist)

### Sinais Enviados
```
Status: ARMED
Health: 100%
Security: OK
Dependencies: OK
Ready: YES
```

## Recuperação

### Se Comando Falhar
1. Logar erro completo
2. Reportar ao Orchestrator
3. Sugerir retry ou alternativa
4. Manter estado anterior

### Se Segurança Comprometida
1. Abortar imediatamente
2. Logar tentativa de violação
3. Alertar Orchestrator (CRITICAL)
4. Bloquear até verificação manual

### Se Dependência Falhar
1. Detectar em heartbeat
2. Tentar reconexão
3. Reportar status degradado
4. Operar com capacidade reduzida

## Histórico

```
[STANDBY] Aguardando primeira invocação
[SECURITY] Whitelist verificada e ativa
[READY] Sistema ARMED e operacional
```

## Alertas

### 🟢 Armed & Ready
- Whitelist ativa
- Auditoria funcionando
- Todas as dependências OK
- Nenhuma violação

### 🟡 Degraded
- 1 dependência indisponível
- Latência elevada
- Retry frequente

### 🔴 Security Alert
- Tentativa de violação de whitelist
- Padrão proibido detectado
- Auditoria falhou
