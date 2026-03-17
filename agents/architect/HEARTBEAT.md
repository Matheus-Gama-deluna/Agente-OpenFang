# HEARTBEAT.md - Architect

## Sinal de Vida

**Status:** STANDBY (aguardando invocação)  
**Health:** 100%  
**Última Atividade:** N/A  

## Estado Atual

Como agente sob demanda, não mantém heartbeat contínuo.
Heartbeat é reportado apenas durante ativação:

### Durante Análise
```
Status: ANALYZING
Progress: {current_phase}
Health: HEALTHY
Time Active: {elapsed_time}
```

## Métricas de Performance

### Quando Ativo
- **Latência de boot:** < 2s
- **Tempo médio de análise:** 5-15 min
- **Memória utilizada:** 256MB (análise de médio porte)
- **Taxa de sucesso:** > 95%

### Ciclos de Vida
- **Ativações hoje:** 0
- **Ativações esta semana:** 0
- **Tempo total ativo (7d):** 0 min

## Dependências

| Serviço | Status | Usado em |
|---------|--------|----------|
| OpenViking | ✅ Disponível | Consulta histórico |
| GitHub API | ✅ Disponível | Leitura de repos |
| Web Search | ✅ Disponível | Pesquisa padrões |
| OpenFang Core | ✅ Disponível | Spawn/Execução |

## Sinais de Vida

### Para Orchestrator
- Durante análise: heartbeat a cada 60s
- Se análise > 10 min: progress update a cada 5 min
- Em caso de erro: report imediato

### Checkpoints
1. **Início:** "Architect iniciado, carregando contexto..."
2. **Codebase:** "Codebase lido, analisando..."
3. **Research:** "Pesquisando padrões modernos..."
4. **Synthesis:** "Compilando insights..."
5. **Document:** "Gerando relatório..."
6. **Complete:** "Análise completa, retornando..."

## Recuperação

### Se Falhar Durante Análise
1. Logar estado atual
2. Reportar ao Orchestrator com contexto parcial
3. Sugerir retry ou análise parcial

### Timeouts
- **Máximo de análise:** 30 minutos
- **Se exceder:** Reportar progresso parcial
- **Retry:** Orchestrator pode reinvocar com contexto ajustado

## Histórico

```
[STANDBY] Aguardando primeira invocação
```
