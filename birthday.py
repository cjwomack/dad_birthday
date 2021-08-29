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
    hb_str = ",🎈 Happy Birthday 🎂 to you 🥳     ,🎁 Happy Birthday 🎂 to you 🥳         "\
        ",🎉 Happy Birthday 🎂 dear Daddy 🧔          ,🎁 Happy Birthday 🎂 to you 🥳          ,"\
            "🎈 Hip Hip Hoo ray🎉   ,🎁 Hip Hip Hoo ray🎈  "
    
    jgf_str = "For 🥳 he's a jolly good fellow 🧔         ,for he's a jolly good fellow 🥳          ,"\
        "for 🧔 he's a jolly good fellow 🥳                       ,and so say all of us 👩 👧 👨      ,"\
            "✨ and so say all of us 👩 👧 👨        ,and so say all of us 👩 👧 👨  ,"\
            "for 🥳 he's a jolly good fellow 🧔     ,for 🧔 he's a jolly good fellow 🥳     ,"\
                "for 🥳 he's a jolly good fellow 🧔                    "
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
    for letter in "✨ which ":
        print(colored(letter,r_colour()),end="")
        time.sleep(0.075)
    time.sleep(0.25)
    for letter in "🚷 nobody ":
        print(colored(letter,r_colour()),end="")
        time.sleep(0.075)
    time.sleep(0.25)
    for letter in "can deny 🍰 ✨":
        print(colored(letter,r_colour()),end="")
        time.sleep(0.075)
    print()
    time.sleep(30)
