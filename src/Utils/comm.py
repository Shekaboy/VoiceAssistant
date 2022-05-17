#Class used to communicate bw various parts of the assistant

class Message:
    value = True
    msg = ""
    Error=""
    def __init__(self , val:bool,error:str,e:Exception) -> None:
        self.value = val
        self.msg = error
        self.error = e