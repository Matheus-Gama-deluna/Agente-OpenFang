# MEMORY.md - Operator

## Estrutura de Memória

### Short-Term Memory (Context Window)
**Tipo:** Estado de execução atual  
**Retenção:** Duração da sessão  
**Limite:** ~128k tokens  

**O que armazena:**
- Comandos executados na sessão
- Resultados recentes
- Estado de diagnóstico
- Contexto do problema

---

### Long-Term Memory (OpenViking)
**Tipo:** Logs de auditoria e histórico de comandos  
**Retenção:** 30 dias  
**Acesso:** Via `openviking_read` (logs)  

**O que armazena:**
- Histórico de comandos executados
- Resultados de diagnósticos
- Erros encontrados
- Soluções aplicadas

**Namespace:** `operator/logs`  

---

## Ciclo de Vida da Execução

### 1. Recebimento
- Request do Orchestrator
- Identificação do problema
- Contexto carregado

### 2. Execução
- Validação de comando (whitelist)
- Execução com timeout
- Captura de resultado

### 3. Análise
- Interpretação do output
- Identificação de padrões
- Determinação de próximos passos

### 4. Reporte
- Retorno ao Orchestrator
- Log de auditoria
- Se necessário, persistir solução

### 5. Auditoria (persistência)
- Comando, timestamp, resultado
- Retenção por 30 dias
- Acessível para diagnósticos futuros

## Padrões de Execução

### Diagnóstico de Erro
```
Contexto: [serviço, tipo de erro]
Comando: [comando executado]
Resultado: [output]
Interpretação: [análise]
Próximo Passo: [recomendação]
```

### Verificação de Recursos
```
Timestamp: [data/hora]
Recursos: [cpu, mem, disco]
Alertas: [se houver]
Tendência: [comparado com baseline]
```

## Retenção de Contexto

### 1 Hora
- Detalhes de comandos específicos
- Outputs completos
- Estado de diagnóstico

### 30 Dias (via OpenViking)
- Comandos executados
- Erros encontrados
- Soluções aplicadas
- Padrões de problemas

### Permanente (via Archivist)
- Decisões de arquitetura operacional
- Mudanças significativas
- Documentação de procedimentos

## Auditoria

### Log de Comandos
```
[YYYY-MM-DD HH:MM:SS] USER: orchestrator
[YYYY-MM-DD HH:MM:SS] COMMAND: docker logs wapp-tv --tail 50
[YYYY-MM-DD HH:MM:SS] RESULT: success (exit code 0)
[YYYY-MM-DD HH:MM:SS] OUTPUT_HASH: sha256:abc123
```

### Histórico de Diagnósticos
- Problema identificado
- Comandos usados para diagnosticar
- Causa raiz encontrada
- Solução aplicada

## Cache de Sistema

### Informações de Status
- `docker ps`: Cache de 30 segundos
- `system_stats`: Cache de 1 minuto
- Logs recentes: Cache de 5 minutos

### Invalidação
- Após execução de comando modificador
- Por timeout (definido por tipo)
- Manual (via flag)

## Segurança

### Não Persistir
- Senhas ou tokens
- Dados sensíveis de logs
- Informações PII

### Sanitização
- Logs são filtrados antes de persistir
- Tokens removidos automaticamente
- Paths sensíveis ofuscados

## Recuperação

### Se Contexto Perdido
- Recuperar do log de auditoria
- Reconstruir estado a partir de comandos
- Consultar OpenViking para histórico

### Se Sessão Falhar
- Logar estado atual
- Permitir retry pelo Orchestrator
- Manter atomicidade de comandos
