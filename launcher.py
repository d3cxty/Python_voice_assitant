import speech_recognition as sr
import nltk
import subprocess

def main():
    # Set up the recognizer and microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Keep listening until you say "stop"
    while True:
        # Adjust for background noise
        print("Adjusting for noise... Say something!")
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=2)  # Increased to 2 seconds

        # Listen for audio
        print("Listening...")
        with microphone as source:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  # Added phrase timeout

        # Convert audio to text
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            text = text.lower()
        except sr.UnknownValueError:
            print("Couldn't understand you.")
            continue
        except sr.RequestError:
            print("Couldn't connect to recognition service.")
            continue

        # Process the text with NLTK
        tokens = nltk.word_tokenize(text)
        print(f"Tokens: {tokens}")
        tags = nltk.pos_tag(tokens)
        print(f"Tags: {tags}")

        # Find the verb and noun
        verb = None
        noun = None
        for word, tag in tags:
            if tag.startswith('VB') or (word in ["open", "shut", "cancel", "say"] and tag.startswith('JJ')):
                verb = word
            if tag.startswith('NN'):
                noun = word

        # Fallback: If no verb found, check tokens directly
        if verb is None:
            if "open" in tokens:
                verb = "open"
            elif "stop" in tokens:
                verb = "stop"
            elif "shut" in tokens:
                verb = "shut"
            elif "cancel" in tokens:
                verb = "cancel"
            elif "say" in tokens:
                verb = "say"

        # Match the verb and noun to an action
        if verb == "stop":
            print("Goodbye!")
            break
        elif verb == "open" and noun == "browser":
            print("Opening a browser...")
            subprocess.run("start chrome", shell=True)
        elif verb == "open" and noun == "notepad":
            print("Opening Notepad...")
            subprocess.run("start notepad", shell=True)
        elif verb == "open" and noun == "files":
            print("Opening File Explorer...")
            subprocess.run("start explorer", shell=True)
        elif verb == "open" and noun == "youtube":
            print("Opening YouTube...")
            subprocess.run("start chrome https://www.youtube.com", shell=True)
        elif verb == "say" and noun == "hello":
            print("Hello to you too!")
        elif verb == "open" and noun == "calculator":
            print("Opening Calculator...")
            subprocess.run("start calc", shell=True)
        elif verb == "open" and noun == "music":
            print("Opening music player...")
            subprocess.run("start wmplayer", shell=True)
        elif verb == "shut" and noun == "down":
            print("Shutting down your computer in 30 seconds... (say 'cancel shutdown' to stop)")
            subprocess.run("shutdown /s /t 30", shell=True)
        elif verb == "cancel" and noun == "shutdown":
            print("Canceling shutdown...")
            subprocess.run("shutdown /a", shell=True)
        elif verb == "open" and noun == "paint":
            print("Opening Paint...")
            subprocess.run("start mspaint", shell=True)
        else:
            print("I don't understand that command")

if __name__ == "__main__":
    main()