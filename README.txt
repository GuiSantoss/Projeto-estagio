# Instruções para Rodar o Projeto

## 1️⃣ Instalar dependências
Execute o seguinte comando para instalar todas as dependências necessárias:
```
pip install -r requirements.txt
```

## 2️⃣ Configurar o banco de dados
- Certifique-se de que o PostgreSQL está rodando.
- O arquivo `.env` já está configurado com as credenciais padrão:
  ```
  DATABASE_URL=postgresql://postgres:161220@localhost/db
  ```
- Caso o banco de dados `db` não exista, crie-o manualmente ou altere o nome no `.env` para um existente.

## 3️⃣ Criar as tabelas no banco
Execute o seguinte comando para aplicar as migrações e criar as tabelas no banco de dados:
```
alembic upgrade head
```

## 4️⃣ Rodar a API
Inicie a API com:
```
uvicorn main:app --reload
```
A API estará disponível em `http://127.0.0.1:8000/docs` (Swagger UI).

## 5️⃣ Testar a API
Execute os testes unitários para validar a aplicação:
```
pytest tests.py
```

## 🔹 Possíveis ajustes
👉 **Se o banco de dados não conectar**  
- Confirme que o PostgreSQL está rodando e que o banco `db` existe.
- Se estiver usando Docker, pode ser necessário mudar `localhost` para `host.docker.internal` no `.env`.

👉 **Se precisar modificar o modelo**  
- Altere os arquivos `models.py` e `schemas.py`.
- Gere uma nova migração com:
  ```
  alembic revision --autogenerate -m "update"
  ```
- Aplique a nova migração:
  ```
  alembic upgrade head
  ```

Tudo pronto! 🚀
