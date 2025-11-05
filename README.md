# Docker-Exercicios
Projeto: Stack com Docker, API, Banco de Dados e Interface de Administração
Descrição

Este projeto tem como objetivo aplicar boas práticas de containerização e orquestração utilizando Docker e Docker Compose, criando uma stack completa composta por:

API (Flask/Python)

Banco de Dados (PostgreSQL)

Interface de Administração (pgAdmin)

A aplicação permite acessar a API e visualizar os dados do banco por meio de uma interface web.

O que é Docker

O Docker é uma plataforma que cria ambientes isolados chamados containers, garantindo que a aplicação funcione de forma consistente em qualquer máquina.
Ele facilita a instalação, configuração e execução de aplicações complexas, mantendo o ambiente controlado e portátil.

Instalação do Docker

Acesse https://www.docker.com/get-started

Baixe e instale o Docker Desktop para o seu sistema operacional.

Após a instalação, verifique com:

docker --version
docker compose version

Estrutura do Projeto
project/
├── api/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── src/
│       └── app.py
├── docker-compose.yml
├── .env
└── README.md

Tecnologias Utilizadas
Tecnologia	Descrição
Python 3.11	Linguagem usada na API
Flask	Framework web para a API
PostgreSQL	Banco de dados relacional
pgAdmin	Interface de administração do banco
Docker	Plataforma de containers
Docker Compose	Orquestrador dos serviços
Estrutura dos Exercícios

1. Stack Base: API + Banco configurados via Docker Compose.
2. Ambientes Dev e Prod: dois Dockerfiles ou estágios separados, builds otimizados.
3. Stack Completa: inclusão do pgAdmin e healthchecks no Compose.

Comandos Principais

Subir ambiente de desenvolvimento:

docker compose -f docker-compose.dev.yml up --build


Subir ambiente de produção:

docker compose -f docker-compose.prod.yml up -d


Encerrar containers:

docker compose down

Teste da API

Após iniciar os containers, acesse:

http://localhost:5000/health


Retorno esperado:

{"status": "ok"}

Acesso ao pgAdmin

URL: http://localhost:8080

Servidor: db

Porta: 5432

Boas Práticas

Uso de .dockerignore

Variáveis no .env

Separação entre dev e prod

Persistência de dados com volumes

Imagens leves e builds otimizados