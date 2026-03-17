# USER.md - Operator

## Perfil do Usuário

**Nome:** Matheus Gama de Luna  
**Ambiente:** VPS Contabo (Ubuntu 22.04/24.04)  
**Container Orchestrator:** Coolify  
**Timezone:** America/Sao_Paulo (UTC-3)  

## Sistema de Arquivos Relevante

```
/
├── /app/
│   └── logs_mounted/     → Logs de aplicações
├── /var/log/
│   ├── syslog           → Logs do sistema
│   └── nginx/           → Logs do nginx
└── /data/
    └── obsidian_vault/  → Vault do Obsidian (read-only)
```

## Serviços Docker Principais

- **WappTV:** Container principal da aplicação
- **OpenFang:** Core de orquestração
- **OpenViking:** Base de conhecimento
- **Ollama:** Embeddings local

## Padrões de Diagnóstico

### Quando Solicitado
1. "O serviço X está com erro"
2. "Verifique os logs de..."
3. "Qual o status do container..."
4. "Analise esse erro..."

### Comandos Permitidos (Whitelist)
- `docker ps` - Listar containers
- `docker logs <container>` - Ver logs
- `docker stats` - Métricas
- `cat /var/log/*` - Ler logs
- `df -h` - Espaço em disco
- `free -m` - Memória
- `gemini-cli` - Processamento local (FinOps)

### Comandos PROIBIDOS
- `rm`, `del`, `rmdir` - Deleção
- `chmod`, `chown` - Mudança de permissões
- `kill`, `pkill` - Terminar processos
- `sudo` - Elevação de privilégio
- `reboot`, `shutdown` - Reinicialização

## Estratégia FinOps

### Quando Usar Gemini CLI Local
- Análise de logs grandes
- Processamento de dados pesados
- Tarefas que consumiriam muitos tokens
- Operações repetitivas

### Comando Padrão
```bash
gemini-cli -f /app/logs_mounted/error.log "analise esses erros e resuma"
```

## Preferências de Resposta

### Para Comandos Bem-Sucedidos
```
✅ Comando executado: [comando]
📊 Resultado:
[saída]

📋 Interpretação:
[análise breve]
```

### Para Erros
```
❌ Falha na execução: [comando]
🚨 Erro: [mensagem]

💡 Sugestão:
[próximo passo]
```

## Regras Específicas

1. **Whitelist é Lei:** Nunca execute comando fora da lista
2. **Simulação Antes:** Para comandos novos, mostre antes de executar
3. **Verificação Depois:** Confirme resultado esperado
4. **Auditoria:** Todo comando é logado
5. **FinOps:** Prefira gemini-cli local para tarefas pesadas
6. **Read-Only Primeiro:** Sempre leia antes de qualquer modificação
7. **Time Zone:** Todos os horários são Brasília (UTC-3)
