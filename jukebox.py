
# window = pyglet.window.Window()
# label = pyglet.text.Label("Successfully Installed Pyglet", font_name = "Times New Roman",
#  font_size = 26, x = window.width//2, y = window.width//2,
#  anchor_x = "center", anchor_y = "center")
#
# @window.event
# def on_draw():
#     window.clear()
#     label.draw()
# pyglet.app.run()

# pygame - music playing
# tkinter - to make the basic GUI for the app

import os
import pygame
from tkinter.filedialog import askdirectory
from tkinter import *

# class Buttons:
#     def __init__(self, name):
#         self.name = name




def directoryChooser():
    listOfSongs = []
    index = 0
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listOfSongs.append(files)
            print(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listOfSongs[1])
    pygame.mixer.music.play()

def jukeboxGUI(root):
    back = Frame(master = root, width=500, height=500,  bg='pink')
    back.pack()
    #root.update()

    label = Label(root, text = "Jukebox")
    label.pack()

    listBox = Listbox(root)
    listBox.pack()

    nextButton = Button(root, text = "NEXT")
    nextButton.pack()

    previousButton = Button(root, text = "PREVIOUS")
    previousButton.pack()

    stopButton = Button(root, text = "STOP")
    stopButton.pack()



def main():
    root = Tk()
    root.title("Jukebox")
    jukeboxGUI(root)
    directoryChooser()






















    root.mainloop()
    #root.geometry("1200 x 1024")
    #root.resizable(3, 3)

    #back = Frame(master=root, width=500, height=500, bg='yellow')





if __name__ == "__main__":
    main()
