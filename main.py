from dotenv import load_dotenv
import os
import speech_recognition as sr

def configure():
    load_dotenv()

def listen(timeLimit: int) -> sr.AudioData:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio: sr.AudioData = r.listen(source, timeout=2, phrase_time_limit=timeLimit)
    
    return audio

def recognize(audio: sr.AudioData) -> str:
    
    HOUNDIFY_CLIENT_ID = os.getenv("houndify-client-id")
    HOUNDIFY_CLIENT_KEY = os.getenv("houndify-client-key")
    r = sr.Recognizer()
    recognizedText: str
    
    try:
        recognizedText = r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)[0]
        print(recognizedText)
    except sr.UnknownValueError:
        print("I could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Houndify service; {e}")

    return recognizedText
    
def main():
    configure()
    
    wakeWord: str = ""
    audio: sr.AudioData
    while wakeWord != os.getenv("wake-word"):
        try:
            audio = listen(2)
            wakeWord = recognize(audio)
        except sr.WaitTimeoutError:
            print("Couldn't hear anything...")
    
if __name__ == "__main__":
    main()