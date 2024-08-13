import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('ECommerceDB.db')
cursor = conn.cursor()

# Consulta de todos os produtos
cursor.execute('SELECT * FROM Products')
products = cursor.fetchall()
for product in products:
    print(product)

# Consulta de todos os clientes
cursor.execute('SELECT * FROM Customers')
customers = cursor.fetchall()
for customer in customers:
    print(customer)

# Fechar a conexão
conn.close()
