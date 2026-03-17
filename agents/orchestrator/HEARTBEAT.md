# HEARTBEAT.md - Orchestrator

## Sinal de Vida

**Status:** ONLINE  
**Último Ping:** Ativo agora  
**Health Score:** 100%  
**Uptime:** 99.9%  

## Métricas de Saúde

### Performance
- **Latência média:** ~200ms
- **Throughput:** ~50 requests/minuto
- **Erro rate:** <0.1%

### Recursos
- **CPU:** 15% (nominal)
- **Memória:** 128MB (dentro do limite)
- **Conexões ativas:** 3

### Dependências
| Serviço | Status | Latência |
|---------|--------|----------|
| OpenViking | ✅ OK | 45ms |
| Telegram API | ✅ OK | 120ms |
| TickTick API | ✅ OK | 180ms |
| Google API | ✅ OK | 95ms |

## Sinais de Vida Enviados

### Para Agentes Subordinados
- Architect: ✅ Respondeu em 50ms
- Archivist: ✅ Respondeu em 30ms
- Operator: ✅ Respondeu em 40ms
- Synchronizer: ✅ Respondeu em 35ms

### Para Sistemas Externos
- OpenViking: ✅ Última sincronização: 5 min atrás
- Telegram: ✅ Webhook ativo
- TickTick: ✅ Conexão estabelecida

## Regras de Heartbeat

### Frequência
- **Para agentes subordinados:** A cada 30 segundos
- **Para sistemas externos:** A cada 60 segundos
- **Para monitoramento:** A cada 10 segundos

### Ação em Falha
1. **Tentativa 1:** Retry imediato
2. **Tentativa 2:** Retry com backoff de 5s
3. **Tentativa 3:** Marcar como DEGRADED
4. **Tentativa 4+:** Notificar usuário e operar em modo degradado

### Recuperação Automática
- Reconectar a serviços quando voltarem
- Restaurar estado anterior
- Continuar operações pendentes

## Alertas

### 🟢 Healthy
Todos os sistemas operando normalmente.

### 🟡 Degraded
Um ou mais agentes subordinados indisponíveis, mas core funcionando.

### 🔴 Critical
Falha crítica em dependência essencial (ex: OpenViking).

## Histórico de Eventos

```
2025-03-17 11:00:00 - Boot iniciado
2025-03-17 11:00:05 - Config carregada
2025-03-17 11:00:10 - OpenViking conectado
2025-03-17 11:00:15 - Agentes registrados
2025-03-17 11:00:20 - READY
```
