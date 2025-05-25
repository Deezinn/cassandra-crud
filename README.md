# CRUD com Cassandra em Python 🐍⚙️

Este projeto implementa uma aplicação de **CRUD (Create, Read, Update, Delete)** utilizando o banco de dados **Apache Cassandra**, com a aplicação escrita em **Python**. O Cassandra roda localmente em um container Docker separado e é acessado pela aplicação via `localhost:9042`.

---

## 🧰 Tecnologias Utilizadas

- Python 3.10+
- Apache Cassandra
- Docker
- Biblioteca `cassandra-driver` (DataStax)

---

## 🐳 Rodando o Cassandra com Docker

Para iniciar o Cassandra localmente, execute:

```bash
docker run --name cassandra -p 9042:9042 -d cassandra:latest

A primeira inicialização pode levar alguns minutos.

Verifique os logs para saber quando o serviço estiver pronto:

docker logs -f cassandra

Você pode acessar o terminal interativo do Cassandra dentro do container com:

docker exec -it cassandra cqlsh

    Isso abrirá o shell do Cassandra (cqlsh) para executar comandos diretamente no banco.

🐍 Criando e ativando o ambiente virtual

Para isolar as dependências Python do projeto:

python -m venv venv
source venv/bin/activate  # No Linux/macOS
venv\Scripts\activate     # No Windows

Instale as dependências:

pip install cassandra-driver

📁 Estrutura do Projeto

crud_cassandra/
├── crud/
│   └── crud.py             # Classe com as operações CRUD
├── db/
│   └── connect_db.py       # Conexão e criação de keyspace e tabela
├── main.py                 # Execução do CRUD
└── README.md               # Documentação do projeto

✅ Testando o Projeto

    Certifique-se que o Cassandra está rodando via Docker.

    Ative seu ambiente virtual.

    Execute a aplicação:

python main.py

📌 Observações

    O projeto se conecta ao Cassandra via 127.0.0.1:9042.

    A aplicação cria o keyspace e a tabela automaticamente se não existirem.

    Ideal para aprendizado e testes locais com Python e Cassandra.
