# 🍕 API de Pizzaria - FastAPI

Este projeto consiste em uma **API Back-end para gerenciamento de pedidos de uma pizzaria**, desenvolvida utilizando **Python** e o framework FastAPI.

O sistema permite que usuários se cadastrem, realizem login e gerenciem pedidos de pizza através de endpoints REST. Também possui autenticação utilizando **JWT (Json Web Token)**.

# ⚠️ **Observação:**  
Este projeto foi desenvolvido seguindo um **curso de FastAPI**, com o objetivo de praticar e aprofundar conhecimentos em **desenvolvimento de APIs, autenticação e organização de rotas em aplicações Back-end**.

---

# 🚀 Tecnologias Utilizadas

- Python
- FastAPI
- SQLAlchemy
- Uvicorn
- Passlib
- Python-JOSE
- python-dotenv

---

# 📦 Funcionalidades

## 🔐 Autenticação
- Criar conta de usuário
- Login com email e senha
- Geração de **Access Token**
- Geração de **Refresh Token**
- Autenticação usando **JWT**

## 👤 Usuários
- Cadastro de novos usuários
- Criptografia de senha
- Controle de permissões (usuário comum ou administrador)

## 🍕 Pedidos
- Criar pedidos
- Cancelar pedidos
- Finalizar pedidos
- Listar pedidos
- Visualizar pedido específico

## 🧾 Itens do Pedido
- Adicionar itens ao pedido
- Remover itens do pedido
- Cálculo automático do valor total do pedido

## 🔒 Segurança
- Rotas protegidas com autenticação
- Verificação de permissões de usuário

---

# 📂 Estrutura do Projeto

```
project/
│
├── main.py
├── auth_routes.py
├── order_routes.py
├── models.py
├── schemas.py
├── dependencies.py
├── database.py
└── .env
```

### main.py
Arquivo principal da aplicação. Responsável por inicializar o FastAPI, carregar variáveis de ambiente e registrar as rotas.

### auth_routes.py
Contém as rotas relacionadas à autenticação:

- Criar conta
- Login
- Refresh token

### order_routes.py
Responsável pelas rotas relacionadas aos pedidos:

- Criar pedido
- Adicionar item ao pedido
- Remover item do pedido
- Cancelar pedido
- Finalizar pedido
- Listar pedidos

---

# ▶️ Como Executar o Projeto

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

---

## 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

### Ativar o ambiente


```bash
venv\Scripts\activate
```


---

## 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Criar arquivo `.env`

Exemplo:

```
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 5️⃣ Executar o servidor

```bash
uvicorn main:app --reload
```

---

# 📚 Documentação da API

O FastAPI gera automaticamente a documentação interativa da API.

Após rodar o projeto, acesse:

```
http://127.0.0.1:8000/docs
```

Interface baseada no **Swagger UI**, onde é possível testar todas as rotas da API.

---

# 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de:

- Aprender **desenvolvimento de APIs REST**
- Praticar **autenticação com JWT**
- Utilizar **FastAPI em aplicações reais**
- Praticar organização de código em projetos Back-end

---


💻 Projeto desenvolvido para **estudo e prática em desenvolvimento Back-end com Python e FastAPI**.
