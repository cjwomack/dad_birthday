from IPython.display import display, HTML
from threading import Thread
from termcolor import colored
import time
from random import randint

def r_colour():
    colours = ["grey","red","green","white","blue","magenta","cyan"]
    return colours[randint(0,6)]
def play_music():
    js = "<script>var myAudio = new Audio('Voice 002.wav');myAudio.play();</script>"
    display(HTML(js))
    #sound = AudioSegment.from_wav(r'Voice 002.wav')
    #play(sound)

def start_music():
    music_thread = Thread(target=play_music)
    music_thread.start()

def play():
    play_music()
    time.sleep(3)
    animation_thread=Thread(target=animation)
    animation_thread.start()

def animation():
    hb_str = ",π Happy Birthday π to you π₯³     ,π Happy Birthday π to you π₯³         "\
        ",π Happy Birthday π dear Daddy π§          ,π Happy Birthday π to you π₯³          ,"\
            "π Hip Hip Hoo rayπ   ,π Hip Hip Hoo rayπ  "
    
    jgf_str = "For π₯³ he's a jolly good fellow π§         ,for he's a jolly good fellow π₯³          ,"\
        "for π§ he's a jolly good fellow π₯³                       ,and so say all of us π© π§ π¨      ,"\
            "β¨ and so say all of us π© π§ π¨        ,and so say all of us π© π§ π¨  ,"\
            "for π₯³ he's a jolly good fellow π§     ,for π§ he's a jolly good fellow π₯³     ,"\
                "for π₯³ he's a jolly good fellow π§                    "
    #time.sleep(1)
    for phrase in hb_str.split(","):
        for letter in phrase:
            print(colored(letter,r_colour()),end="")
            time.sleep(0.085)
        print()
    
    for phrase in jgf_str.split(","):
        for letter in phrase:
            print(colored(letter,r_colour()),end="")
            time.sleep(0.055)
        print()
    for letter in "β¨ which ":
        print(colored(letter,r_colour()),end="")
        time.sleep(0.075)
    time.sleep(0.25)
    for letter in "π· nobody ":
        print(colored(letter,r_colour()),end="")
        time.sleep(0.075)
    time.sleep(0.25)
    for letter in "can deny π° β¨":
        print(colored(letter,r_colour()),end="")
        time.sleep(0.075)
    print()
    time.sleep(30)
