# TOOLS.md - Operator

## Ferramentas Disponíveis

### 1. shell_execute_restricted
**Descrição:** Executar comandos CLI (whitelist apenas)  
**Uso:** `shell_execute_restricted(command: string, timeout: int = 30)`  
**Quando usar:**
- Diagnosticar problemas de sistema
- Verificar status de serviços
- Analisar logs

**Exemplo:**
```python
shell_execute_restricted("docker ps", timeout=10)
```

**⚠️ SEGURANÇA:** Apenas comandos na whitelist são permitidos!

---

### 2. docker_ps
**Descrição:** Listar containers Docker  
**Uso:** `docker_ps(filters: dict = {})`  
**Quando usar:**
- Verificar quais serviços estão rodando
- Identificar containers parados
- Checar status geral

**Exemplo:**
```python
docker_ps(filters={"status": "running"})
```

---

### 3. docker_logs
**Descrição:** Ler logs de containers  
**Uso:** `docker_logs(container: string, tail: int = 100, since: string = "1h")`  
**Quando usar:**
- Diagnosticar erros em serviços
- Analisar comportamento
- Verificar saúde

**Exemplo:**
```python
docker_logs(
  container="wapp-tv-api",
  tail=50,
  since="30m"
)
```

---

### 4. file_read
**Descrição:** Ler arquivos de configuração e logs  
**Uso:** `file_read(path: string, limit: int = 1000)`  
**Quando usar:**
- Ler logs de aplicações
- Consultar configurações
- Analisar arquivos de erro

**Exemplo:**
```python
file_read(
  path="/app/logs_mounted/wapp-error.log",
  limit=500
)
```

---

### 5. gemini_cli_delegator
**Descrição:** Delegar análise para gemini-cli local (FinOps)  
**Uso:** `gemini_cli_delegator(prompt: string, file_path: string = "")`  
**Quando usar:**
- Análise de logs grandes (economia de tokens)
- Processamento pesado
- Tarefas repetitivas

**Exemplo:**
```python
gemini_cli_delegator(
  prompt="Analise esses erros e categorize por severidade",
  file_path="/app/logs_mounted/error.log"
)
```

---

### 6. system_stats
**Descrição:** Verificar recursos do sistema  
**Uso:** `system_stats(type: string = "all")`  
**Quando usar:**
- Diagnosticar problemas de performance
- Verificar recursos disponíveis
- Monitorar saúde

**Exemplo:**
```python
system_stats(type="memory")
system_stats(type="disk")
system_stats(type="all")
```

---

## Workflow Padrão

### Diagnóstico de Erro
```
1. Receber request do Orchestrator
2. Identificar serviço afetado
3. Verificar status (docker_ps)
4. Ler logs recentes (docker_logs)
5. Se logs grandes → delegar para gemini-cli
6. Analisar resultado
7. Retornar diagnóstico
```

### Verificação de Recursos
```
1. Executar system_stats("all")
2. Identificar gargalos
3. Verificar logs de sistema se necessário
4. Reportar estado
```

## Whitelist de Comandos

### Docker
- `docker ps` - Listar containers
- `docker logs <container>` - Ver logs
- `docker stats` - Métricas
- `docker inspect <container>` - Detalhes

### Logs
- `cat /var/log/syslog` - Logs do sistema
- `cat /var/log/nginx/*.log` - Logs nginx
- `cat /app/logs_mounted/*.log` - Logs apps
- `tail -n 100 <arquivo>` - Últimas linhas

### Sistema
- `df -h` - Espaço em disco
- `free -m` - Memória
- `uptime` - Tempo de atividade
- `ps aux | grep <serviço>` - Processos

### Gemini CLI
- `gemini-cli <prompt> <anexo>` - Processamento local

## Comandos PROIBIDOS

**NUNCA execute:**
- ❌ `rm`, `del`, `rmdir` - Deleção
- ❌ `chmod`, `chown` - Permissões
- ❌ `kill`, `pkill` - Terminar processos
- ❌ `sudo` - Elevação de privilégio
- ❌ `reboot`, `shutdown` - Reinicialização
- ❌ Comandos com `>` (redirecionamento de escrita)
- ❌ Pipes para `xargs rm` ou similar

## Fallbacks

- Se docker indisponível: usar comandos de sistema
- Se arquivo não encontrado: reportar path tentado
- Se gemini-cli falhar: processar via API (com aviso de custo)
- Se timeout: retornar output parcial

## Auditoria

Todo comando é logado:
```
[TIMESTAMP] COMMAND: [comando]
[TIMESTAMP] USER: [orchestrator/user]
[TIMESTAMP] RESULT: [success/error]
[TIMESTAMP] OUTPUT: [hash do output]
```
