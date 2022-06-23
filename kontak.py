import json
from configDB import Database

db = Database('tes_db').connectDB()
cursor = db.cursor(dictionary=True)

cursor.execute("SELECT * FROM tbl_kontak LIMIT 5")
kontak = cursor.fetchall()

print(json.dumps(kontak))

