import os
import pygame
from tkinter.filedialog import askdirectory
from tkinter import *
import eyed3

root = Tk()
root.minsize(300,300)

listOfSongs = []
songTitles = []
index = 0

labelVar = StringVar()
songLabel = Label(root, textvariable = labelVar, width = 50)

def directoryChooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith("mp3"):
            realdir = os.path.realpath(files)
            audioTag = eyed3.load(realdir)
            #tag.link(realdir)
            songTitles.append(audioTag.tag.title)
            listOfSongs.append(files)
            print(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listOfSongs[0])
    pygame.mixer.music.play()

directoryChooser()

def updateLabel():
    global index
    #global songname
    labelVar.set(songTitles[index])

def nextSong(event):
    global index
    index += 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updateLabel()


def previousSong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updateLabel()

def stopSong(event):
    pygame.mixer.music.stop()
    labelVar.set("")




label = Label(root, text = "Music Player")
label.pack()

listBox = Listbox(root)
listBox.pack()




for items in songTitles:
    listBox.insert(END, items) ### this point onwards, clean code



nextButton = Button(root, text = "Next song")
nextButton.pack()

previousButton = Button(root, text = "Previous song")
previousButton.pack()

stopButton = Button(root, text = "Stop")
stopButton.pack()

nextButton.bind("<Button-1>", nextSong)
previousButton.bind("<Button-1>", previousSong)
stopButton.bind("<Button-1>", stopSong)

songLabel.pack()




root.mainloop()
