# Converts text to speech
import pyttsx3
import speech_recognition as sr


class Recognnizer:
    def __init__(self) -> None:
        self.r = sr.Recognizer()
        self.log = []
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
    

    def Recognize(self):
        with sr.Microphone() as source:
            
            print("Listening...")
            self.r.pause_threshold = 1
            audio = self.r.listen(source)
    
        try:
            print("Recognizing...")   
            query = self.r.recognize_google(audio, language ='en-in')
            print(f"User said: {query}\n")
    
        except Exception as e:
            print(e)   
            print("Unable to Recognize your voice.") 
            return "None"
        
        return query
  
if __name__ == "__main__":
    r = Recognnizer()
    while True:
        print(r.Recognize())