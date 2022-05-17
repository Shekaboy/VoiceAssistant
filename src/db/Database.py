# Database operations 
from src.Utils.comm import Message
import sqlite3

class DB:
    def __init__(self,path_to_db) -> None:
        self.conn = sqlite3.connect(path_to_db)

    def insert_db(self,query)->Message:
        try:
            self.conn.execute(query)
            self.conn.commit()
            return Message(True,"","")
        except Exception as e:
            return Message(False,"Unable to Insert into db" , e)


    def query_db(self,query)->Message:
        try:
            cursor = self.conn.execute(query)
            return Message(True,cursor,"")
        except Exception as e:
            return Message(False,"Unable to query the db" , e)


    def update_db(self,query)->Message:
        try:
            self.conn.execute(query)
            self.conn.commit()
            return Message(True,"","")
        except Exception as e:
            return Message(False,"Unable to update the db" , e)


    def delete_from_db(self,query)->Message:
        try:
            self.conn.execute(query)
            self.conn.commit()
            return Message(True,"","")
        except Exception as e:
            return Message(False,"Unable to delete from the db" , e)

    def load_db_data(self,query)->Message:
        try:
            self.conn.execute(query)
            self.conn.commit()
            return Message(True,"","")
        except Exception as e:
            return Message(False,"Unable to delete from the db" , e) 


        