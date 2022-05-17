#Math module
#Math functions contained in a container class
#more complicated math queries will be sent to 
#wolfram alpha via api

import sys

from numpy import number
sys.path.append(".")
sys.path.append("./")
sys.path.append("../")
from src.Utils.comm import Message

class MathOps:
    def __init__(self) -> None:
        self.ans = 0
    def solve(self,eqn):
        print("Equation recieved is {}".format(eqn))
        operators = ["+","-","*","^","/"]
        try:
            if(eqn[0] in operators):
                eqn = str(self.ans) + eqn
            print(eqn)
            temp = eval(eqn)
            self.ans = temp
            return Message(True,str(temp) ,"")
        except Exception as e:
            return Message(False,str(self.ans),e)

    def solve_using_wolfram(self , eqn):
        pass
    def parse_int(self ,text):
        operators = ["+","-","*","^"]
        res = ""
        for i in range(len(text)):

            if(text[i] not in operators):
                res = res + text[i]
            else:
                res = res + " " + text[i]+ " "
        print(res)
        text = res
        words = text.split(" ")
        help_dict = {
                'one': '1',
                'two': '2',
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9',
                'zero' : '0'
            }
        res = ""
        for numbername in words:
            try:
                res = res+help_dict[numbername]
            except:
                res = res + numbername
            
        return res
if __name__ == "__main__":
    m = MathOps()
    print(m.solve(m.parse_int("1+one timesfour by five")).msg)