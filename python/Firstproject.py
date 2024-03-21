import pg8000

try:
    connect = pg8000.connect(
        host="localhost",
        database="V",
        user="postgres",
        password="Vishnu@2",
        port=5432
    )
    print("Connection successful!")
except pg8000.DatabaseError as e:
    print("Connection failed:", e)
    connect = None

if connect:
    cur = connect.cursor()

    # Execute your SQL queries here

    cur.close()
    connect.close()
else:
    print("Connection not established")
