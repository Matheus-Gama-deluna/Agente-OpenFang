# HEARTBEAT.md - Archivist

## Sinal de Vida

**Status:** ACTIVE (background processing)  
**Health:** 100%  
**Último Processamento:** N/A  
**Próximo Processamento:** Calculando...  

## Métricas de Saúde

### Performance
- **Processamento médio:** 5-10 notas por minuto
- **Latência de escrita:** ~50ms
- **Batch size:** Máximo 50 notas
- **Success rate:** > 98%

### Recursos
- **CPU:** 5-10% durante processamento
- **Memória:** 64MB (flash-lite otimizado)
- **Queue size:** 0 (normal)

### Dependências
| Serviço | Status | Latência |
|---------|--------|----------|
| OpenViking | ✅ OK | 45ms |
| Embedding Generator | ✅ OK | 80ms |
| YAML Generator | ✅ OK | Local |
| JSON Formatter | ✅ OK | Local |

## Heartbeat do Cron

### Frequência de Execução
- **Schedule:** A cada 4 horas
- **Última execução:** N/A
- **Próxima execução:** Calculando...
- **Execuções hoje:** 0

### Estado do Cron
```
Schedule: 0 */4 * * *
Status: ACTIVE
Last Trigger: N/A
Next Trigger: HH:MM
Queue Pending: 0
```

## Sinais de Vida

### Durante Processamento
- Heartbeat a cada nota processada
- Progress report: "Processando nota X de Y"
- Status: PROCESSING

### Durante Idle
- Heartbeat a cada 5 minutos
- Status: IDLE
- Próximo trigger agendado

## Recuperação

### Se OpenViking Falhar
1. Buffer notas em memória
2. Retry a cada 5 minutos
3. Após 3 falhas: alertar Orchestrator
4. Manter fila até recuperação

### Se Processamento Falhar
1. Logar nota que falhou
2. Continuar com próxima nota
3. Reportar falhas no final do batch
4. Permitir retry manual

## Histórico de Processamento

```
[N/A] Aguardando primeira execução
```

## Alertas

### 🟢 Healthy
- Processamento normal
- Queue vazia ou dentro do limite
- Todas as dependências OK

### 🟡 Warning
- Queue > 100 notas pendentes
- Latência OpenViking > 200ms
- 1 falha de dependência

### 🔴 Critical
- OpenViking indisponível por > 15 min
- Queue > 500 notas
- Múltiplas falhas consecutivas
