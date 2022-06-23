import mysql.connector
from fastapi import FastAPI

app = FastAPI()

def connectDB(dbName):
    myDb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="KataSandi",
        database=dbName
    )
    
    return myDb

def getData(cursor, query):
    cursor.execute(query)
    data = cursor.fetchall()
    return data

@app.get("/getKontak")
def getKontak():
    db = connectDB("tes_db")
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM tbl_kontak LIMIT 50000"
    dataKontak = getData(cursor,query)
    return dataKontak
