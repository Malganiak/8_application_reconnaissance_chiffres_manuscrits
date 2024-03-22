import pyttsx3 # library to say the number

def tts(chiffre) : 
    engine = pyttsx3.init()
    engine.say(chiffre)
    engine.runAndWait()