import MySQLdb

db = MySQLdb.connect("localhost", "root", "1234", "test")
cursor = db.cursor()
query = "SELECT * FROM arthur"
cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print(row)

db.close()

