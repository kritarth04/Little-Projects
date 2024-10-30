# write a progam to pronounce any thing written .
# use win32
#try to implement in other programms to make them cool

import pyttsx3 as voice

def text_to_speech(text):

    #initialization
    speech = voice.init()

    # rate changing 
    rate = speech.getProperty('rate')  
    speech.setProperty('rate', 150)


    #voice changing
    voices = speech.getProperty('voices')
    speech.setProperty('voice', voices[1].id)

    # to execute the programm 
    speech.say(text)
    speech.runAndWait()

# import time
# text_to_speech("Go away green gram lentiles or else you will suffer , go in 5 seconds. go help mom")

# text_to_speech("5")
# time.sleep(2)
# text_to_speech("4")
# time.sleep(2)
# text_to_speech("3")
# time.sleep(2)
# text_to_speech("2")
# time.sleep(2)
# text_to_speech("1")
# text_to_speech("you will suffer")

