import sys
import os
import re
import random
import datetime
sys.path.append(".")
sys.path.append("./")
from src.Tests.network_test import NetworkTest
from src.Tests.packages import CheckRequirements

if __name__ == "__main__":

    operators = ["+","-","*","^","/"]
    flag1,flag2,flag3 = 0,0,0
    while flag1+flag2+flag3 <= 0 :
        nc = NetworkTest()
        if(nc.check_conn().value):
            print("Network test passed")
            flag1 = 1
        else:
            print("Cant Connect to the internet")
        cr = CheckRequirements("requirements.txt")
        if(cr.check_requirements().value):
            print("Python requirements test passed")
            flag2 = 1
        else:
            print("Trying to install requirements ")
            try:
                cr.install_requirements()
            except:
                print("Cant install Requirements")
            print("Manually check the requirements") 
        from src.Tests.voice_test import MicTest
        
        mc = MicTest()           
        if (mc.check_mic()):
            print("Microphone Detected ")
            flag3 = 1
        else:
            flag3 = 1
            print("Please check microphone and restart"+
            " \n If mic is working and isnt being detected just ignore this message")

    from src.Core.recognizer import Recognnizer
    import pyjokes
    import pywhatkit
    from src.Core.FunctionMapper import FunctionMapper
    from src.Utils.open_app import App
    from src.Utils.play_music import open_music_with_yt
    from src.Utils.open_website import OpenWebsite
    from src.Utils.open_app import App
    from src.db.Database import DB
    from src.Utils.math_module import MathOps
    ow = OpenWebsite()
    mo = MathOps()
    r = Recognnizer()
    db = DB("src/db/app.db")
    app = App()
    fc = FunctionMapper()
    while True:
        text = r.Recognize()
        text = text.lower()
        text = text.strip()
        result = fc.return_function(text)
        try:
            if(result == 0):
                    li = text.split(" ")
                    res = li.index("open")
                    print(li[res+1])
                    app.open_app(li[res+1])
                
            if(result==1):

                    index = re.search("play",text).start()
                    text = text[index+4:].strip()
                    open_music_with_yt(text)

            if(result == 2):
                print("My name is Friday")
            if(result == 3):
                print(pyjokes.get_joke())
            if(result == 4):
                time = datetime.datetime.now()
                print("The time is %s hours ,%s minutes" ,time.hour,time.minute)
            if(result == 5):
                print("Heyy!!!")
            if(result == 6):
                r1 = random.randint(0,11)
                if(r1%2!=0):
                    print("Sorry im already taken")
                else:
                    print("... shy noises !! .. ")
            if(result == 7):
                #math
                text = text.replace("solve","")
                text = text.replace("plus", "+")
                text = text.replace("divide", "/")
                text = text.replace("by", "/")
                text = text.replace("power", "**")
                text = text.replace("x", "*")
                text = text.replace("minus", "-")
                text = mo.parse_int(text)
                text = text.strip()
                if(text[0] in operators):
                    res = mo.solve(text)
                else:
                    mo = MathOps()
                    res = mo.solve(text)
                if res.value:
                    print("The result is {}".format(res.msg))
                else:
                    print("Unknown Error Occured {}".format(res.error))
            if(result==8):
                    index = re.search("surf",text).start()
                    text = text[index+4:].strip()   
                    ow.open_browser_with_url("www."+text+".com")        
            if(result == 9):
                    ow.open_browser_with_query(text)
            if(result == 10):
                    pywhatkit.info(text,lines=10)
                    print("Person specified is not famous / cant find him/her")
        except:
                pass