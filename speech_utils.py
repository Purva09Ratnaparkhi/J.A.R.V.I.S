import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 190)

def take_command(ui):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        ui.terminalPrint("Listening...")
        r.pause_threshold = 0.5 
        r.non_speaking_duration = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        ui.terminalPrint(f"User: {query}\n")
    except Exception as e:
        print("Sorry, I could not understand. Please say again.")
        return "none"
    return query.lower()
