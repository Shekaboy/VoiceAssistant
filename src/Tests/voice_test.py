#Check if voice driver is enabled 
import sys 
sys.path.append("..")
from src.Utils.comm import Message 
import sounddevice as sd

class MicTest:
    def __init__(self) -> None:
        pass

    def check_mic(self)->Message:
        if "Microphone".casefold() in sd.query_devices(kind='input')['name'].casefold():
            return Message(True,"","")
        else:
            return Message(False,"Check Microphone","")
