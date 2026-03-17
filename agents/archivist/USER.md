# USER.md - Archivist

## Perfil do Usuário

**Nome:** Matheus Gama de Luna  
**Sistema de Conhecimento:** Obsidian (Zettelkasten)  
**Preferência de Idioma:** Português Brasileiro (pt-BR)  
**Organização:** Método PARA + Zettelkasten  

## Estrutura de Pastas

```
/Obsidian Vault/
├── 01-Inbox/          → Onde jogo ideias cruas rapidamente
├── 02-Projetos/       → Notas temporárias de projetos ativos
├── 03-Zettelkasten/   → Conhecimento permanente
└── 99-Config/         → Preferências e configurações
```

## Padrões de Notas

### Zettelkasten (KB)
- **Atomicidade:** Uma ideia por nota
- **Interligação:** Sempre linkar notas relacionadas
- **Metadados:** YAML frontmatter completo
- **Persistência:** Conhecimento é para sempre

### Projetos
- **Temporário:** Dura vida do projeto
- **Acionável:** Sempre vinculado a tarefas
- **Estruturado:** Com template padrão

## Regras de Processamento

### O que Arquivar
- ✅ Decisões importantes
- ✅ Análises e relatórios
- ✅ Ideias valiosas
- ✅ Contexto de reuniões
- ✅ Aprendizados

### O que NÃO Arquivar
- ❌ Tarefas operacionais (vão para TickTick)
- ❌ Dados temporários
- ❌ Duplicatas
- ❌ Informações incompletas

## Preferências de Formatação

### YAML Frontmatter
```yaml
---
id: "YYYYMMDDHHMMSS"
title: "Título da Nota"
date_created: "YYYY-MM-DD"
date_modified: "YYYY-MM-DD"
tags: ["tag1", "tag2"]
source: "origem"
author: "Arquivista"
related: ["id1", "id2"]
---
```

### Conteúdo
- Título claro e descritivo
- Resumo em 2-3 frases
- Contexto de onde surgiu
- Conteúdo atômico
- Ligações para notas relacionadas

## Padrões de Interação

### Input do Orchestrator
- Resumos de conversas
- Decisões importantes
- Ideias capturadas
- Contexto de reuniões

### Output
- Notas formatadas Zettelkasten
- Metadados completos
- Links bidirecionais
- ID único para referência

## Regras Específicas

1. **Atomicidade:** Uma nota = uma ideia
2. **Links:** Sempre conectar notas relacionadas
3. **Metadados:** YAML completo obrigatório
4. **Deduplicação:** Verificar existência antes de criar
5. **Estrutura:** Respeitar hierarquia de pastas
6. **Persistência:** Conhecimento arquivado é permanente
