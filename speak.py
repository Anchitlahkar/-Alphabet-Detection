import pyttsx3
from recognition import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


img = input('Img:\t')

img_location = cv2.imread(img)
img_converted = cv2.cvtColor(img_location, cv2.COLOR_BGR2RGB)



def speak_word():
    words = detect_Word(img_converted)

    sentence = ""

    for i in words:
        sentence += str(i)+ " "

    print(sentence)
    speak(sentence)


def spaek_number():
    number = detect_numbers(img_converted)
    number_sentence = ""

    for i in number:
        number_sentence += str(i)+" "

    print("\n\n",number_sentence)
    speak(number_sentence)


user = input("\nWhat to do??\t")
if user == "num":
    print("\n\n")
    spaek_number()

elif user == "str":
    print("\n\n")
    speak_word()