import mysql.connector
import sys

# Configuração do banco de dados

def getDB():
    try:
        db_conexao = mysql.connector.connect(
            host='mysql-352ac4ff-hos1r1s-5fad.a.aivencloud.com',
            port='27307',
            user='avnadmin',
            password='AVNS_PF9iTXRQUVHotQVEs75',
            database='defaultdb',
        )
        return db_conexao
    
    except mysql.connector.Error as erro:
        print(f'Erro connection com o BANCO DE DADOS: {erro}')
        sys.exit(1)
