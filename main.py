# import pyttsx3
from dotenv import load_dotenv
import os
import speech_recognition as sr
from speech_recognition import AudioData

def configure():
    load_dotenv()

def record() -> AudioData:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio: AudioData = r.listen(source)
    
    return audio

def recognize(audio: AudioData) -> str:
    
    HOUNDIFY_CLIENT_ID = os.getenv("houndify-client-id")
    HOUNDIFY_CLIENT_KEY = os.getenv("houndify-client-key")
    
    r = sr.Recognizer()
    recognizedText: str = r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)[0]
    try:
        print(recognizedText)
    except sr.UnknownValueError:
        print("I could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Houndify service; {e}")

    return recognizedText
    
def main():
    configure()
    
    
        
    
if __name__ == "__main__":
    main()