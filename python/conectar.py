import mariadb;
import sys;

try:
    conn = mariadb.connect(
        user = "root",
        password = "",
        host = "localhost",
        port = "3306",
        database = "noslq"
    )

except Exception as erro:
    print(f"Erro ao se conectar com o banco de dados => ");