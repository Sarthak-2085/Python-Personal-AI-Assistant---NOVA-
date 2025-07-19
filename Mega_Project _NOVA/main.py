# d:/Tcet Study/python/.venv/Scripts/activate 
# path to terminal

# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicLibrary
# import requests
# import google.generativeai as genai


# # Gemini Setup
# genai.configure(api_key="AIzaSyD_EqKsaD9zOd-tf3uWGQ__Nxi5O8ABASo")  # Replace with your actual Gemini API key
# gemini_model = genai.GenerativeModel("models/gemini-2.0-flash")

# # Importing the necessary libraries
# # pip install speechrecognition, pyttsx3, pyaudio , pocketsphinx

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# newsapi = "734f846e323d46b591894b7fda4101af" # Replace with your NewsAPI key


# def speak(text): 
#     engine.say(text)
#     engine.runAndWait()

# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://www.google.com")
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://www.youtube.com")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://www.facebook.com")
#     elif "open linkedin" in c.lower():    
#         webbrowser.open("https://www.linkedin.com")
#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ")[1]
#         link = musicLibrary.music[song]
#         webbrowser.open(link) 

#     elif "news" in c.lower():
#         try:
#             r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
#             if r.status_code == 200:
#                 data = r.json()
#                 articles = data.get('articles', [])
#                 for article in articles[:5]:  # limit to first 5 headlines
#                     speak(article['title'])
#             else:
#                 speak("Sorry, I couldn't fetch the news at this moment.")
#         except Exception as e:
#             speak("An error occurred while fetching news.")
#             print("News error:", e)
#     else:
#         try:
#             response = gemini_model.generate_content(c)
#             speak(response.text)
#         except Exception as e:
#             speak("Sorry, I couldn't understand or process your request.")
#             print("Gemini error:", e)


# if __name__ == "__main__":
#     speak(" Initializing NOVA ... ")
# while True:
#         # Listen for the wake word "Nova"
#         # obtain audio from the microphone
#         r = sr.Recognizer()

#         print("Recognizing ...")
#         try: 
#             with sr.Microphone() as source:
#                 print("Listening ...")
#                 audio = r.listen(source, timeout=4, phrase_time_limit=4)
#             word = r.recognize_google(audio)
#             if "nova" in word.lower(): speak ("Yes Sir , how may I help you ?")
#             print ("Yes Sir , how may I help you ?")

#             # Listen for the command after the wake word
#             with sr.Microphone() as source:
#                     print("Nova Active...")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)

#                     processCommand(command)


#         except Exception as e:
#             print("Error ; {0}".format(e))




                        # !!! IMPROVED CODE BY CHATGPT !!!

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
import threading


#  Gemini API Configuration
genai.configure(api_key="AIzaSyD_EqKsaD9zOd-tf3uWGQ__Nxi5O8ABASo")  #  Replace with your real key
gemini_model = genai.GenerativeModel("models/gemini-2.0-flash")

#  Other setup
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "734f846e323d46b591894b7fda4101af"  # Replace with your NewsAPI key

#  Text-to-Speech
def speak(text): 
    engine.say(text)
    engine.runAndWait()

def threaded_speak(text):
    global speak_thread
    speak_thread = threading.Thread(target=speak, args=(text,))
    speak_thread.start()

#  Command Processor
def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c:    
        webbrowser.open("https://www.linkedin.com")
    elif c.startswith("play"):
        try:
            # Get full song name after "play"
            song = c.replace("play", "").strip()
            if song:
                link = f"https://open.spotify.com/search/{song.replace(' ', '%20')}"
                threaded_speak(f"Searching for {song} on Spotify.")
                webbrowser.open(link)
            else:
                threaded_speak("Please say the name of the song after 'play'.")
        except Exception as e:
            threaded_speak("Sorry, I couldn't search for that song.")
        print("Spotify search error:", e)

    elif "news" in c:
        print("News command recognized.")  # Debug print
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                for article in articles[:5]:  # limit to first 5 headlines
                    speak(article['title'])
            else:
                speak("Sorry, I couldn't fetch the news at this moment.")
        except Exception as e:
            speak("An error occurred while fetching news.")
            print("News error:", e)
    else:
        #  Let Gemini handle general questions
        try:
            response = gemini_model.generate_content(c)
            speak(response.text)
        except Exception as e:
            speak("Sorry, I couldn't understand or process your request.")
            print("Gemini error:", e)

#  Wake word listener and main loop
if __name__ == "__main__":
    speak("Initializing NOVA ...")
    
    while True:
        r = sr.Recognizer()
        print("Recognizing ...")

        try: 
            with sr.Microphone() as source:
                print("Listening for wake word ...")
                audio = r.listen(source, timeout=4, phrase_time_limit=3)

            word = r.recognize_google(audio)
            if "nova" in word.lower():
                speak("Yes Sir, how may I help you?")
                print("Yes Sir, how may I help you?")

                # Listen for the actual command
                with sr.Microphone() as source:
                    print("Nova Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error: {0}".format(e))
