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

# Criar a base de dados "empresa_vendas"
cur.execute("DROP DATABASE IF EXISTS empresa_vendas;")
cur.execute("CREATE DATABASE empresa_vendas;")
conn.close()

# Conectar à nova base de dados
conn = psycopg2.connect(
    dbname="empresa_vendas",
    user="postgres",
    password="123",
    host="localhost"
)
cur = conn.cursor()

# Criar as tabelas
cur.execute("""
CREATE TABLE produtos (
    id_produto SERIAL PRIMARY KEY,
    nome_produto VARCHAR(100),
    preco DECIMAL(10, 2)
);
""")

cur.execute("""
CREATE TABLE compras (
    id_compra SERIAL PRIMARY KEY,
    id_produto INT REFERENCES produtos(id_produto),
    quantidade INT,
    data_compra DATE
);
""")

cur.execute("""
CREATE TABLE relatorio_diario (
    id_relatorio SERIAL PRIMARY KEY,
    data_relatorio DATE,
    id_produto INT REFERENCES produtos(id_produto),
    nome_produto VARCHAR(100),
    quantidade_vendida INT
);
""")

# Inserir dados nas tabelas
cur.execute("""
INSERT INTO produtos (nome_produto, preco) VALUES
('Produto A', 10.00),
('Produto B', 20.00),
('Produto C', 15.50);
""")

cur.execute("""
INSERT INTO compras (id_produto, quantidade, data_compra) VALUES
(1, 5, '2024-08-12'),
(2, 3, '2024-08-12'),
(1, 2, '2024-08-13'),
(3, 7, '2024-08-12'),
(2, 4, '2024-08-13');
""")

# Criar a stored procedure para gerar o relatório diário
cur.execute("""
CREATE OR REPLACE PROCEDURE gerar_relatorio_diario(IN data DATE)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Apagar relatórios anteriores para o dia especificado, caso existam
    DELETE FROM relatorio_diario WHERE data_relatorio = data;

    -- Inserir o resumo diário das vendas na tabela de relatórios
    INSERT INTO relatorio_diario (data_relatorio, id_produto, nome_produto, quantidade_vendida)
    SELECT 
        data_compra AS data_relatorio,
        p.id_produto,
        p.nome_produto,
        SUM(c.quantidade) AS quantidade_vendida
    FROM 
        compras c
    JOIN 
        produtos p ON c.id_produto = p.id_produto
    WHERE 
        c.data_compra = data
    GROUP BY 
        p.id_produto, p.nome_produto, c.data_compra;
END;
$$;
""")

# Executar a procedure para uma data específica
cur.execute("CALL gerar_relatorio_diario('2024-08-12');")

# Consultar o relatório gerado
cur.execute("SELECT * FROM relatorio_diario WHERE data_relatorio = '2024-08-12';")
relatorio_resultados = cur.fetchall()
for registro in relatorio_resultados:
    print(registro)

# Fechar a conexão
cur.close()
conn.close()
