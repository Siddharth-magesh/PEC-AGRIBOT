import speech_recognition as sr
import pyttsx3

def listen():
    # Initialize recognizer instance
    recognizer = sr.Recognizer()

    while True:
        try:
            # Capture audio from microphone
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
                audio = recognizer.listen(source, timeout=5)  # Listen for 5 seconds

            # Recognize speech
            print("Recognizing...")
            user_input = recognizer.recognize_google(audio)
            return user_input

        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return None

def talk(text):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Set properties for the speech engine (optional)
    engine.setProperty('rate', 150)  # Speed of speech

    # Speak the text
    engine.say(text)
    engine.runAndWait()


