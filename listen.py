import speech_recognition as sr;
import nltk;

def main():
    recogniser = sr.Recognizer()
    microphone = sr.Microphone()
    
    print("making adjustments")
    with microphone as source:
        recogniser.adjust_for_ambient_noise(source,duration=1)
        
    print("listening.....")
    with microphone as source:
        audio = recogniser.listen(source,timeout=10)
        
        
    try:
        text = recogniser.recognize_google(audio)
        print(f"u said {text}")
        if "stop" in text:
            print("good bye")
        
    except sr.UnknownValueError:
        print("unknown error")

if __name__ == "__main__":
        main()       