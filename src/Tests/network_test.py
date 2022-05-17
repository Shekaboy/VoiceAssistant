#Check if connected to the internet
import socket
import sys
sys.path.append("..")
from src.Utils.comm import Message 

class NetworkTest:
    base_url = ""
    def __init__(self,url="www.ismyinternetworking.com") -> None:
        self.base_url = url
    
    def check_conn(self ,timeout=80)->Message:
        try:
            host = socket.gethostbyname(self.base_url)               
            s = socket.create_connection((host, timeout), 2)
            s.close()
            return Message(True,"","") 
        except Exception as e:
            return Message(False,"Cant Connect to the Internet",e)

if __name__ == "__main__":
    temp = NetworkTest()
    print(temp.check_conn(80).value)