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

# Criar o banco de dados "loja" (caso não exista)
cur.execute("DROP DATABASE IF EXISTS loja;")
cur.execute("CREATE DATABASE loja;")
conn.close()

# Conectar ao banco de dados "loja"
conn = psycopg2.connect(
    dbname="loja",
    user="postgres",
    password="123",
    host="localhost"
)
cur = conn.cursor()

# Criar a tabela de clientes
cur.execute("""
CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    data_cadastro DATE
);
""")

# Inserir alguns dados de exemplo na tabela de clientes
cur.execute("""
INSERT INTO clientes (nome, email, data_cadastro) VALUES
('João Silva', 'joao.silva@example.com', '2024-08-12'),
('Maria Aparecida', 'maria.aparecida@example.com', '2024-08-12'),
('Pedro Lucas', 'pedro.lucas@example.com', '2024-08-13'),
('Ana Clara', 'ana.clara@example.com', '2024-08-13'),
('Carlos Souza', 'carlos.souza@example.com', '2024-08-12');
""")

# Criar a função para contar os clientes cadastrados num dia
cur.execute("""
CREATE OR REPLACE FUNCTION contar_clientes_cadastrados(data DATE)
RETURNS INT AS $$
DECLARE
    total_clientes INT;
BEGIN
    SELECT COUNT(*) INTO total_clientes
    FROM clientes
    WHERE data_cadastro = data;

    RETURN total_clientes;
END;
$$ LANGUAGE plpgsql;
""")

# Executar a função para uma data específica
cur.execute("SELECT contar_clientes_cadastrados('2024-08-12');")
resultado = cur.fetchone()[0]
print(f"Total de clientes cadastrados em 2024-08-12: {resultado}")

cur.close()
conn.close()
