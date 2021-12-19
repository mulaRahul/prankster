import os
import time
import winsound

def pull_prank():
    # Opens the image file
    os.startfile(r"X:\prankster\nun.jpg")
    
    # Background music via https://www.FesliyanStudios.com
    # plays the .wav file
    winsound.PlaySound(r"X:\prankster\jump-scare.wav", 
                       flags=winsound.SND_FILENAME)

time.sleep(360)
pull_prank()