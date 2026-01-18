# ms-memory

Este projeto é uma API para gerenciamento de memoria/mensagens doa agentes de IA.

## Pré-requisitos
- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (gerenciador de dependências)
- MongoDB (configurar URL no arquivo `.env`)

## Instalação

1. Clone o repositório e acesse a pasta do projeto:
   ```bash
   git clone <url-do-repositorio>
   cd ms-memory
   ```

2. Crie o arquivo `.env` com base no `.env.example` e configure as variáveis:
   ```bash
   cp .env.example .env
   # Edite o arquivo .env conforme necessário
   ```

3. Instale as dependências:
   ```bash
   make install
   ```

## Executando o servidor

- Para iniciar o servidor em modo produção:
  ```bash
  make run
  ```
  O servidor estará disponível em `http://localhost:8000`.

- Para modo desenvolvimento (hot reload):
  ```bash
  make run_dev
  ```

## Endpoints

Acesse a documentação automática em `http://localhost:8000/ms-memory/docs` após iniciar o servidor.
