import sqlite3

#### A função «sqlite3.connect» cria uma conexão com o banco de dados chamado db.sqlite3
conexao = sqlite3.connect('db.sqlite3')
#### Após criar a variável «conexao», nós precisamos criar um cursor para executar comandos SQL
cursor = conexao.cursor()
cursor.execute('CREATE TABLE fornecedores (id INT, nome VARCHAR(100), endereco VARCHAR(250));')
conexao.commit()
#### Fechar a conexão é importante caso tenha algo a mais para ser executado no seu programa Python.
conexao.close()