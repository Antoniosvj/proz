#NESTE ARQUIVO ESTA SENDO CRIADO E ADICIONADO DADOS NO BANCO DE EDADOS

import psycopg2

# Conectar ao PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="123",
    host="localhost"
)
conn.autocommit = True
cur = conn.cursor()

# Criar a base de dados
cur.execute("CREATE DATABASE escola;")
conn.close()

# Conectar à nova base de dados
conn = psycopg2.connect(
    dbname="escola",
    user="postgres",
    password="123",
    host="localhost"
)
cur = conn.cursor()

# Criar as tabelas
cur.execute("""
CREATE TABLE estudantes (
    id_estudante SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    endereco VARCHAR(255)
);
""")

cur.execute("""
CREATE TABLE cursos (
    id_curso SERIAL PRIMARY KEY,
    nome_curso VARCHAR(100),
    duracao INT
);
""")

cur.execute("""
CREATE TABLE inscricoes (
    id_inscricao SERIAL PRIMARY KEY,
    id_estudante INT REFERENCES estudantes(id_estudante),
    id_curso INT REFERENCES cursos(id_curso),
    data_inscricao DATE
);
""")

# Inserir dados nas tabelas
cur.execute("""
INSERT INTO estudantes (nome, idade, endereco) VALUES
('João Silva', 20, 'Rua A, 123'),
('Maria Aparecida', 36, 'Rua B, 456'),
('Pedro Lucas', 28, 'Rua C, 789');
""")

cur.execute("""
INSERT INTO cursos (nome_curso, duracao) VALUES
('Python', 12),
('JavaScript', 10),
('Banco de dados', 15);
""")

cur.execute("""
INSERT INTO inscricoes (id_estudante, id_curso, data_inscricao) VALUES
(1, 1, '2024-08-01'),
(2, 2, '2024-08-03'),
(3, 3, '2024-08-05'),
(1, 2, '2024-08-07');
""")

conn.commit()
cur.close()
conn.close()
