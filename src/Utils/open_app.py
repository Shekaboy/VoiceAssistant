#Opens specified app by user

from asyncio.log import logger
from concurrent.futures import thread
import os
import sys
sys.path.append("../")
import platform
from src.Utils.comm import Message
from src.db.Database import DB
import subprocess

class App:
    def __init__(self) -> None:
        self.os_type = platform.system()
        self.db = DB("src/db/app.db")
        print(self.os_type)
    def open_app(self, app_name):
            print(app_name)
            try:
                #Error opening using system variable
                subprocess.Popen(app_name)
            except:
                print("Opening with db path")
                #check if installation dir exixts in db
                query = """SELECT INSTALL_DIR FROM APPS_DIR WHERE """+"""app_name like """+ "'"+app_name + "'" 
                print(query)
                res =  self.db.query_db(query)
                print(res.value)
                if res.value is True:
                    path = res.msg.fetchone()
                    print(path)
                    try:
                        subprocess.Popen(path)
                    except:
                        print("Invalid or no path entered , would you like to changr it now (Y/n)?")
                        if(input().lower == "y"):
                            path = input()
                            self.db.update_db(query)
                        else:
                            print("Invalid argument or n entered exiting ")
                else:
                    print("No directory found , would you like to add it to db (Y/n)?")
                    if(input().lower == "n"):
                        return
                    elif(input().lower == "y"):
                        dir = input()
                        query = """INSERT INTO APPS_DIR (INSTALL_DIR,app_name) values("""+dir + ""","""+app_name+""" )"""
                        self.db.update_db(query)
                    else:
                        print("Invlid argument entered , exiting ")

        

if __name__ == "__main__":
    a = App()
    a.open_app("chrome")