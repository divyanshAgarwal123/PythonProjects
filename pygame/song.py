from pygame import mixer
mixer.init()
mixer.music.load("Shane McMahon - Here Comes The Money (Entrance Theme).mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
while True:
    print("Press 'p' to pause, 'r' to resumePress 'e' to exit the program")
    x=input("")
    if x=='p':
        mixer.music.pause()
    elif x=='u':
        mixer.music.unpause()
    elif x=='s':
        mixer.music.stop()
        break