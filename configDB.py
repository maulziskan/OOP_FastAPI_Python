import mysql.connector

class Database:
    def __init__(self, dbName):
        self.dbName = dbName
        
    
    def connectDB(self):
        myDb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "KataSandi",
            database = self.dbName
        )
    
        return myDb