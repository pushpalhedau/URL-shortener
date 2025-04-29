from db import get_db_connection

conn = get_db_connection()

print("URLs:")
for row in conn.execute("SELECT * FROM urls"):
    print(dict(row))

print("\nUsers:")
for row in conn.execute("SELECT * FROM users"):
    print(dict(row))

conn.close()
