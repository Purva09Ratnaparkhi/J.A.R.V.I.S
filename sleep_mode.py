import speech_recognition as sr
import time

def listen_for_wake_word(wake_word="wake up"):
    
    
    # Loop until wake-up word is detected
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for wake-up word...")
            r.pause_threshold = 0.5
            r.non_speaking_duration = 0.3
            audio = r.listen(source)
            
            try:
                # Recognize the audio
                query = r.recognize_google(audio, language='en-in')
                query = query.lower()
                print(f"User said: {query}")

                # Check if the wake-up word is spoken
                if wake_word in query:
                    print("Wake-up word detected!")
                    return True  # Proceed further after wake-up word
                else:
                    print("Wake-up word not detected. Continuing to listen...")
            
            except sr.UnknownValueError:
                print("Sorry, I could not understand. Please say again.")            
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
