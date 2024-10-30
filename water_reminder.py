
import time 
# import text_speech as tx
from plyer import notification


def reminder():
    global samay
    # waterRem = "! This is an every hour water reminder ! \n                                                               Please drink a glass of water."
    while True:
        samay = time.strftime("%H")

        # print(waterRem.center(250))

        notifiacation()

        # tx.text_to_speech('Please drink water')

        time.sleep(1200)

        if samay == '10':
            exit()
        else:
            continue


def notifiacation():

    notification.notify(

        # title = "Water Reminder",
        title = "20-20 Rule",
        # message = "Water is the only drink for a wise man.",
        message = "Precaution is better than cure.\nComplete video lecture before 5`o clock",
        timeout=3
    )
    

reminder()