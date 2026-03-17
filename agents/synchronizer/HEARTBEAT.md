# HEARTBEAT.md - Synchronizer

## Sinal de Vida

**Status:** ACTIVE  
**Cron:** ENABLED (próximo: 07:00)  
**Health:** 100%  
**Última Sincronização:** N/A  
**Timezone:** America/Sao_Paulo (UTC-3)  

## Métricas de Saúde

### Performance
- **Latência TickTick API:** ~200ms
- **Latência OpenViking:** ~50ms
- **Tempo de criação:** ~1s por tarefa
- **Success rate:** > 95%

### Recursos
- **CPU:** 3% (idle)
- **Memória:** 48MB
- **Queue:** 0

### Dependências
| Serviço | Status | Latência |
|---------|--------|----------|
| TickTick API | ✅ OK | 180ms |
| OpenViking | ✅ OK | 45ms |
| Date Parser | ✅ OK | Local |
| Timezone DB | ✅ OK | Local |

## Cron Job Status

### Sumário Matinal
```
Schedule: 0 7 * * *
Status: ACTIVE
Última Execução: N/A
Próxima Execução: Amanhã 07:00
Timezone: America/Sao_Paulo
Estado: AGENDADO
```

### Contador
- **Execuções hoje:** 0
- **Execuções esta semana:** 0
- **Tarefas criadas hoje:** 0
- **Tarefas criadas esta semana:** 0

## Heartbeat

### Frequência
- **Idle:** A cada 60 segundos
- **Durante sync:** A cada operação
- **Cron check:** A cada 5 minutos

### Sinais
```
Status: ACTIVE
Cron: ENABLED
Next Run: 07:00
API Status: OK
Backup Status: OK
Ready: YES
```

## Recuperação

### Se TickTick Falhar
1. Tentar retry (3x com backoff)
2. Salvar no Obsidian como "pending"
3. Reportar status degradado
4. Tentar reconexão a cada 10 min

### Se Data Ambígua
1. Usar interpretação mais provável
2. Logar ambiguidade
3. Incluir data original na nota
4. Permitir correção manual

### Se Projeto Inválido
1. Usar "p_Pessoal" como fallback
2. Logar erro de mapeamento
3. Notificar no contexto
4. Sugerir correção

## Histórico de Sincronização

```
[N/A] Aguardando primeira execução
[INFO] Cron ativo para 07:00
```

## Alertas

### 🟢 Healthy
- TickTick API respondendo
- Cron ativo
- Backups funcionando
- Projetos mapeados

### 🟡 Warning
- Latência API > 500ms
- 1 falha de backup
- Projetos não mapeados

### 🔴 Critical
- TickTick API indisponível > 10 min
- Múltiplas falhas consecutivas
- Timezone mismatch detectado
