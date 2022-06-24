import speech_recognition as sr
import pyttsx3
import pywhatkit



listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 150)
engine.setProperty('volume', 0.7)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():


    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
    except:
        pass
    return rec

def run():
    talk("Hola soy dicci que quieres reproducir?")
    rec = listen()

    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk("Reproduciendo a " + music)
        pywhatkit.playonyt(music)

run()