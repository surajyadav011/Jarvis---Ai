import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary


recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    

    
def processCommand(c):
    print("preprocessing:",c)
    
    if "open chrome" in c.lower():
        print("opening chrome")
        webbrowser.open("https://chrome.com")
    elif "open facebook" in c.lower():
        print("opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        print("opening youtube")
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
        
        
        
if __name__=="__main__":
    speak("Initialising Jarvis........")
    #listen for the wake word Jarvis
    #obtain audio from the microphone
    while True:
        r=sr.Recognizer()
        
        print("recognizing....")
        try:
            with sr.Microphone(device_index=0) as source:
                print("Listening......")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
            word=r.recognize_google(audio)
            print("You said:", word)

            if "jarvis" in word.lower():
                speak("Yaaa...")
                #Listen for the command
                with sr.Microphone(device_index=0) as source:  
                    print("Jarvis Active")
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio=r.listen(source)
                command=r.recognize_google(audio)
                    
                print("Command:",command)
                processCommand(command)
                    
            
        except Exception as e:
            print("Error:",e)
    
    
        
        
            
        
    
