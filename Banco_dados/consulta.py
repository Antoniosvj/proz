#CONSULTA USANDO O JOIN
import psycopg2

# Conectar à base de dados
conn = psycopg2.connect(
    dbname="escola",
    user="postgres",
    password="123",
    host="localhost"
)
cur = conn.cursor()

# Exemplo de consulta com JOIN
cur.execute("""
SELECT 
    estudantes.nome AS Nome_Estudante, 
    cursos.nome_curso AS Curso 
FROM inscricoes
JOIN estudantes ON inscricoes.id_estudante = estudantes.id_estudante
JOIN cursos ON inscricoes.id_curso = cursos.id_curso;
""")

resultados = cur.fetchall()
for resultado in resultados:
    print(resultado)

cur.close()
conn.close()
