from dotenv import load_dotenv
import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import library
import gpt_module

engine = pyttsx3.init()

def configure() -> None:
    load_dotenv()

def listen(timeLimit: int) -> sr.AudioData:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio: sr.AudioData = r.listen(source, timeout=3, phrase_time_limit=timeLimit)
    
    return audio

def recognize(audio: sr.AudioData) -> str:
    
    HOUNDIFY_CLIENT_ID = os.getenv("houndify-client-id")
    HOUNDIFY_CLIENT_KEY = os.getenv("houndify-client-key")
    r = sr.Recognizer()
    recognizedText: str = ""
    
    try:
        recognizedText = r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)[0].lower()
        print(recognizedText)
    except sr.UnknownValueError:
        print("I could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Houndify service; {e}")

    return recognizedText
    
def recognizeWakeWord() -> bool:
    wakeWord: str = ""
    audio: sr.AudioData
    while wakeWord != os.getenv("wake-word"):
        try:
            audio = listen(2)
            wakeWord = recognize(audio)
        except sr.WaitTimeoutError:
            print("Couldn't hear anything...")
    else:
        return True
    
def response() -> None:
    command: sr.AudioData = listen(5)
    commandstr: str = recognize(command).lower()
    specifics: list = commandstr.split(" ")
    action: str = specifics[0]
    
    if action in library.allowedActions:
        try:
            if action not in library.allowedActions:
                engine.say("Sorry, I can't do that.")
                engine.runAndWait()
                return
            elif len(specifics) == 1:
                engine.say("Please specify an action.")
                engine.runAndWait()
                return           
            actionObject: str = ''.join(specifics[1:])
            webbrowser.open(library.allowedActions.get(action).get(actionObject))
            
        except Exception as e:
            print(f"An error occurred: {e}")
            engine.say("Sorry, I couldn't process your request.")
            engine.runAndWait()    
    else:
        prompt: str = commandstr
        briefPromt: str = prompt + "\nplease respond briefly."
        
        response: str = gpt_module.aiResponse(briefPromt)
        print(response)
        engine.say(response)
        engine.runAndWait()
        
    
def main() -> None:
    configure()
    if recognizeWakeWord():
        print("Wake word recognized!")
        engine.say("Hello, how can I help you?")
        engine.runAndWait()
        response()
        
    
if __name__ == "__main__":
    main()