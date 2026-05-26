# 🥊 Fighthouse Chatbot

Um sistema de chatbot inteligente para a **Fight House Academy**, desenvolvido com Python e React/Vite. O chatbot automatiza o processo de atendimento, captura de leads e matrículas para a academia de artes marciais.

---

## 📋 Sumário

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias (Stack)](#tecnologias-stack)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Fluxo da Aplicação](#fluxo-da-aplicação)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Painel Admin](#painel-admin)
- [Arquitetura](#arquitetura)
- [Roadmap Futuro](#roadmap-futuro)
- [Contribuindo](#contribuindo)

---

## 🎯 Visão Geral

O **Fighthouse Chatbot** é uma solução de automação de atendimento para academias de artes marciais. Sistema capaz de:

- ✅ Manter conversas interativas com clientes
- ✅ Gerenciar múltiplos usuários de forma simultânea
- ✅ Capturar informações de leads (nome, telefone, modalidade)
- ✅ Armazenar dados em JSON (temporário)
- ✅ Fornecer painel administrativo para gestão de leads

O projeto foi projetado com **escalabilidade em mente**, permitindo futuras integrações com WhatsApp, banco de dados e inteligência artificial.

---

## ✨ Funcionalidades

### Funcionalidades Atuais

- **Menu Automático**: Sistema de navegação intuitivo com menus e submenus
- **Horários**: Consulta de horários das aulas por modalidade
- **Modalidades**: Informações sobre modalidades disponíveis (Kickboxing, Boxe, Jiu-Jitsu, Taekwondo)
- **Valores**: Tabela de preços das modalidades
- **Fluxo de Matrícula**: Captura estruturada de:
  - Nome do cliente
  - Número de telefone (com DDD)
  - Modalidade desejada
- **Gestão de Leads**: Sistema de armazenamento e rastreamento de leads
- **Painel Admin**: Interface para gerenciar status dos leads
- **Gerenciamento de Usuários**: Mantém o estado de cada usuário durante a conversa

### Funcionalidades Planejadas

- 🔜 Integração com **WhatsApp**
- 🔜 Painel Web em **React**
- 🔜 Integração com **Banco de Dados** (PostgreSQL/MySQL)
- 🔜 Sistema de **IA para Dúvidas Livres**
- 🔜 Notificações por email/SMS
- 🔜 Dashboard de análises e relatórios

---

## 🛠 Tecnologias (Stack)

### Backend
- **Python 3.8+**: Linguagem principal
- **JSON**: Armazenamento temporário de dados
- **Arquitetura Modular**: Separação clara de responsabilidades

### Frontend (Em Desenvolvimento)
- **React 19.2.6**: Biblioteca UI
- **Vite 8.0.12**: Build tool ultrarrápido
- **ESLint**: Qualidade de código
- **JavaScript/CSS/HTML**

### Linguagens do Projeto
```
Python:      49.5%
CSS:         25.5%
JavaScript:  23.2%
HTML:        1.8%
```

---

## 📁 Estrutura de Diretórios

```
fighthouse-chatbot/
│
├── 📄 main.py                 # Ponto de entrada da aplicação CLI
├── 📄 admin.py                # Painel administrativo para gestão de leads
├── 📄 package-lock.json       # Lock file do npm (raiz)
├── 📄 .gitignore              # Configuração git
│
├── 📂 core/                   # Núcleo da aplicação
│   ├── 📄 chatbot.py          # Lógica principal do chatbot
│   └── 🗂️ __pycache__/        # Cache Python (ignorado)
│
├── 📂 flow/                   # Fluxos de conversação
│   ├── 📄 menu.py             # Menu principal
│   ├── 📄 horarios_flow.py    # Fluxo de horários
│   ├── 📄 valores_flow.py     # Fluxo de preços
│   ├── 📄 matricula_flow.py   # Fluxo de matrícula
│   ├── 📄 __init__.py         # Inicialização do módulo
│   └── 🗂️ __pycache__/        # Cache Python (ignorado)
│
├── 📂 messages/               # Mensagens e conteúdo
│   ├── 📄 horarios.py         # Mensagens de horários
│   ├── 📄 valores.py          # Mensagens de preços
│   ├── 📄 modalidades.py      # Mensagens de modalidades
│   ├── 📄 __init__.py         # Inicialização do módulo
│   └── 🗂️ __pycache__/        # Cache Python (ignorado)
│
├── 📂 data/                   # Armazenamento de dados
│   ├── 📄 leads.json          # Leads capturados
│   ├── 📄 usuarios.json       # Estado dos usuários
│   └── 📄 leads.txt           # Logs adicionais (opcional)
│
└── 📂 chatbot/                # Frontend React + Vite
    ├── 📄 package.json        # Dependências React
    ├── 📄 package-lock.json   # Lock file npm
    ├── 📄 vite.config.js      # Configuração Vite
    ├── 📄 eslint.config.js    # Configuração ESLint
    ├── 📄 index.html          # HTML principal
    ├── 📂 public/             # Arquivos estáticos
    ├── 📂 src/                # Código fonte React
    └── 📂 node_modules/       # Dependências (ignorado)
```

---

## 🔄 Fluxo da Aplicação

### Fluxo Principal do Chatbot

```
┌─────────────────────────────────────────────────────────────┐
│                    CHATBOT FIGHTHOUSE                       │
└─────────────────────────────────────────────────────────────┘

1️⃣ MENU PRINCIPAL
   │
   ├─→ [1] HORÁRIOS
   │   └─→ Selecionar Modalidade
   │       └─→ Ver Detalhes
   │           └─→ Voltar (opção 0)
   │
   ├─→ [2] MODALIDADES
   │   └─→ Ver Informações
   │       └─→ Voltar (opção 0)
   │
   ├─→ [3] VALORES
   │   ├─→ [1] Kickboxing
   │   ├─→ [2] Boxe
   │   ├─→ [3] Jiu-Jitsu
   │   └─→ [4] Taekwondo
   │       └─→ Ver Detalhes/Voltar
   │
   └─→ [4] MATRÍCULA
       ├─→ Inserir Nome
       ├─→ Inserir Telefone
       ├─→ Selecionar Modalidade
       └─→ ✅ Lead Salvo
           └─→ Voltar ao Menu
```

### Estados da Conversa

O sistema mantém o **estado de cada usuário** em máquina de estados:

| Estado | Ação | Próximo Estado |
|--------|------|--------|
| `menu` | Mostrar menu principal | horarios/modalidades/valores/matricula_nome |
| `horarios` | Mostrar horários | horarios_detalhe |
| `horarios_detalhe` | Mostrar detalhes | horarios |
| `valores` | Mostrar valores | valores_detalhe |
| `valores_detalhe` | Mostrar detalhes | valores |
| `matricula_nome` | Capturar nome | matricula_telefone |
| `matricula_telefone` | Capturar telefone | matricula_modalidade |
| `matricula_modalidade` | Capturar modalidade | menu (lead salvo) |

### Fluxo de Dados

```
Mensagem do Usuário
        ↓
    main.py
        ↓
core/chatbot.py (processar_mensagem)
        ↓
flow/*.py (Lógica de fluxo)
        ↓
messages/*.py (Conteúdo)
        ↓
data/usuarios.json (Estado persistido)
data/leads.json (Lead salvo)
        ↓
    Resposta do Bot
```

---

## 📦 Requisitos

### Requisitos do Sistema
- **Python**: 3.8 ou superior
- **Node.js**: 14+ (para o frontend)
- **npm**: 6+ (gerenciador de pacotes Node)
- **pip**: Gerenciador de pacotes Python

### Verificar Versões
```bash
python --version
node --version
npm --version
```

---

## 🚀 Instalação

### 1. Clonar Repositório

```bash
git clone https://github.com/joaoamorinz0/fighthouse-chatbot.git
cd fighthouse-chatbot
```

### 2. Configurar Backend (Python)

```bash
# Criar ambiente virtual (opcional, mas recomendado)
python -m venv venv

# Ativar ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

# Instalar dependências (se houver requirements.txt)
# pip install -r requirements.txt
# Atualmente, o projeto usa apenas módulos padrão do Python
```

### 3. Configurar Frontend (React)

```bash
cd chatbot

# Instalar dependências
npm install

# Voltar ao diretório raiz
cd ..
```

---

## 💻 Como Usar

### Executar o Chatbot (CLI)

```bash
python main.py
```

**Exemplo de Interação:**

```
Cliente: 1
Bot: 🕐 HORÁRIOS

1 - Kickboxing
2 - Boxe
3 - Jiu-Jitsu
4 - Taekwondo
0 - Voltar

Cliente: 1
Bot: ⏰ KICKBOXING
Segunda a sexta: 18:00 - 19:00
Sábado: 10:00 - 11:00
Domingo: Fechado

Cliente: 4
Bot: ✅ MATRÍCULA INICIADA
👤 Qual é o seu nome?

Cliente: João Silva
Bot: 📱 Qual é o seu número de telefone?
Digite com DDD.
Exemplo: 61999999999

Cliente: 61999999999
Bot: 🥊 Qual modalidade deseja fazer?
1 - Kickboxing
2 - Boxe
3 - Jiu-Jitsu
4 - Taekwondo

Cliente: 1
Bot: ✅ MATRÍCULA INICIADA

Nome: João Silva
Telefone: 61999999999
Modalidade: Kickboxing

Em breve entraremos em contato!
```

### Usar o Painel Admin

```bash
python admin.py
```

**Menu Admin:**

```
⚙️ PAINEL ADMIN - FIGHT HOUSE

1 - Listar leads
2 - Marcar como contatado
3 - Marcar como matriculado
4 - Marcar como perdido
0 - Sair

Escolha: 1
```

**Saída:**

```
📋 LISTA DE LEADS

ID: 1
Nome: João Silva
Telefone: 61999999999
Modalidade: Kickboxing
Status: novo
Criado em: 26/05/2026 14:30
------------------------------
```

### Executar o Frontend (React)

```bash
cd chatbot

# Desenvolvimento (com hot reload)
npm run dev

# Build para produção
npm run build

# Preview do build
npm run preview

# Verificar qualidade de código
npm run lint
```

---

## 🔐 Painel Admin

O painel administrativo permite gerenciar leads capturados:

### Funcionalidades

1. **Listar Leads**: Visualizar todos os leads com informações completas
2. **Marcar como Contatado**: Atualizar status para "contatado"
3. **Marcar como Matriculado**: Atualizar status para "matriculado"
4. **Marcar como Perdido**: Atualizar status para "perdido"

### Estrutura de um Lead

```json
{
  "id": 1,
  "nome": "João Silva",
  "telefone": "61999999999",
  "modalidade": "Kickboxing",
  "status": "novo",
  "criado_em": "26/05/2026 14:30"
}
```

### Status Possíveis

- `novo` - Lead recém-capturado
- `contatado` - Cliente já foi contatado
- `matriculado` - Cliente finalizou matrícula
- `perdido` - Cliente não compareceu/desistiu

---

## 🏗 Arquitetura

### Padrão de Código

O projeto segue uma **arquitetura modular e escalável**:

```
Responsabilidade de cada camada:

├─ main.py           → Entrada e loop de mensagens
├─ core/chatbot.py   → Lógica de estados e orquestração
├─ flow/*.py         → Fluxos específicos (negócio)
├─ messages/*.py     → Conteúdo/Mensagens
└─ admin.py          → Interface administrativa
```

### Gerenciamento de Estado

Cada usuário possui um estado mantido em `data/usuarios.json`:

```json
{
  "joao": {
    "estado": "matricula_telefone",
    "dados": {
      "nome": "João Silva",
      "telefone": "61999999999"
    }
  }
}
```

### Estrutura de Leads

Leads são armazenados em `data/leads.json`:

```json
[
  {
    "id": 1,
    "nome": "João Silva",
    "telefone": "61999999999",
    "modalidade": "Kickboxing",
    "status": "novo",
    "criado_em": "26/05/2026 14:30"
  }
]
```

---

## 🚦 Roadmap Futuro

### Fase 2: Integração WhatsApp
- [ ] Conectar com API do WhatsApp
- [ ] Suportar mídia (imagens, vídeos)
- [ ] Notificações de confirmação

### Fase 3: Painel Web
- [ ] Dashboard em React (na pasta `/chatbot`)
- [ ] Visualização de métricas
- [ ] Gerenciamento de leads via web
- [ ] Relatórios e análises

### Fase 4: Banco de Dados
- [ ] Migrar de JSON para PostgreSQL
- [ ] Implementar ORM (SQLAlchemy)
- [ ] Sistema de backups automáticos

### Fase 5: IA e Automação
- [ ] Integrar IA para responder dúvidas livres
- [ ] NLP para entender intenção do usuário
- [ ] Machine Learning para prever conversões

### Fase 6: DevOps
- [ ] Containerizar com Docker
- [ ] CI/CD com GitHub Actions
- [ ] Deploy em cloud (AWS/Azure/GCP)
- [ ] Monitoramento e logs

---

## 📊 Documentação Adicional

### Variáveis de Ambiente (Futuro)
```bash
CHATBOT_MODE=production
DATABASE_URL=postgresql://user:password@localhost/fighthouse
WHATSAPP_TOKEN=your_token_here
```

### Logs
- Atualmente, os logs são salvos em `data/leads.json`
- Futuro: Sistema de logging estruturado com arquivos `.log`

---

## 🤝 Contribuindo

### Como Contribuir

1. **Fork** o repositório
2. **Crie uma branch** para sua feature (`git checkout -b feature/amazing-feature`)
3. **Commit** suas mudanças (`git commit -m 'Add amazing feature'`)
4. **Push** para a branch (`git push origin feature/amazing-feature`)
5. **Abra um Pull Request**

### Padrões de Código

- **Python**: Seguir PEP 8
- **JavaScript/React**: ESLint (configurado no projeto)
- **Commits**: Usar mensagens descritivas em inglês

### Testes

```bash
# Executar testes (quando implementados)
pytest

# Verificar qualidade de código
eslint chatbot/src/**
```

---

## 📄 Licença

Este projeto é de código aberto. Verifique o arquivo `LICENSE` para detalhes.

---

## 👨‍💻 Autor

**João Amorim**  
- GitHub: [@joaoamorinz0](https://github.com/joaoamorinz0)
- Repositório: [fighthouse-chatbot](https://github.com/joaoamorinz0/fighthouse-chatbot)

---

## 📞 Suporte

Encontrou um bug? Tem uma sugestão?

- **Issues**: [Abrir uma issue](https://github.com/joaoamorinz0/fighthouse-chatbot/issues)
- **Discussions**: [Discussões](https://github.com/joaoamorinz0/fighthouse-chatbot/discussions)

---

## 🎓 Aprendizados

Este projeto demonstra:

- ✅ Arquitetura modular em Python
- ✅ Máquina de estados para fluxos conversacionais
- ✅ Persistência de dados em JSON
- ✅ Integração Python + React/Vite
- ✅ Gestão de múltiplos usuários simultâneos
- ✅ Boas práticas de organização de código

---

**Última atualização**: 26 de maio de 2026  
**Status**: Em desenvolvimento ativo
