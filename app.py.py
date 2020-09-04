#play sound from a gui

import tkinter
from playsound import playsound


def play_song():
    playsound("drive_off.mp3", block=False)


window = tkinter.Tk()

B = tkinter.Button(window, text ="Play", command = play_drive_off)
B.pack()
window.mainloop()



