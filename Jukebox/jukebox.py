import os
import pygame
#from PIL import Image
from tkinter.filedialog import askdirectory
from tkinter import *
import eyed3


class Jukebox:
    def __init__(self, window, index, photoPath):
        self.photo = PhotoImage(file = photoPath)
        self.canvas = Canvas(width = 1000, height = 1000, bg = "black")
        self.label = Label(self.canvas, text = "Jukebox")
        self.listBox = Listbox(self.canvas)
        self.playResumeButton = Button(self.canvas, text = "Play/Resume")
        self.pauseButton = Button(self.canvas, text = "Pause")
        self.nextButton = Button(self.canvas, text = "Next Song")
        self.previousButton = Button(self.canvas, text = "Previous Song")
        self.stopButton = Button(self.canvas, text = "Stop")
        self.labelVar = StringVar()
        self.songLabel = Label(self.canvas, textvariable = self.labelVar, width = 35)
        self.index = index
        self.songTitles = []
        self.listOfSongs = []
        self.directoryAsk = askdirectory()
        self.num_songs = len(self.songTitles)
        self.Error_NoMP3s = "No \".mp3\" files found."

    def updateLabel(self):
        if (index != 0) and (len(self.songTitles) != 0):
            self.labelVar.set("Now Playing: " + self.songTitles[(index % len(self.songTitles)) - 1])
        else:
            self.labelVar.set("Now Playing: " + self.songTitles[index - 1])

    def directoryChooser(self):
        self.directoryAsk
        os.chdir(self.directoryAsk)

        for files in os.listdir(self.directoryAsk):
            if files.endswith(".mp3"):
                realdir = os.path.realpath(files)
                audioTag = eyed3.load(realdir)
                self.songTitles.append(audioTag.tag.title)
                self.listOfSongs.append(files)
                #print("These are files:", self.listOfSongs)
                #print("These are the number of files:", len(self.songTitles))

        pygame.mixer.init()
        pygame.mixer.music.load(self.listOfSongs[0])
        self.updateLabel()
        pygame.mixer.music.play()
        pygame.mixer.music.play()


    def constructButtons(self):
        self.canvas.pack()
        self.canvas.create_image(0,0, image = self.photo, anchor = NW)
        self.label.pack()
        self.listBox.pack()
        for items in self.songTitles:
            print(items)
            self.listBox.insert(END, items)
        self.playResumeButton.pack()
        self.pauseButton.pack()
        self.nextButton.pack()
        self.previousButton.pack()
        self.stopButton.pack()
        self.playResumeButtonWin = self.canvas.create_window(125, 120, anchor = NW, window = self.playResumeButton)
        self.pauseButtonWin = self.canvas.create_window(144, 150, anchor = NW, window = self.pauseButton)
        self.nextButtonWin = self.canvas.create_window(500, 120, anchor = NW, window = self.nextButton)
        self.previousButtonWin = self.canvas.create_window(480, 150, anchor = NW, window = self.previousButton)
        self.stopButtonWin = self.canvas.create_window(148, 181, anchor = NW, window = self.stopButton)
        self.labelWin = self.canvas.create_window(325, 40, anchor = NW, window = self.label)
        self.listBoxWin = self.canvas.create_window(270, 80, anchor = NW, window = self.listBox)
        self.songLabelWin = self.canvas.create_window(207, 265, anchor = NW, window = self.songLabel)


def playResumeSong(event):
    global index
    global myJukebox
    pygame.mixer.music.unpause()

    if pygame.mixer.music.get_busy() != True:
        index = 1
        pygame.mixer.music.load(myJukebox.listOfSongs[index - 1])
        pygame.mixer.music.play()
        pygame.mixer.music.play()
        myJukebox.updateLabel()


def pauseSong(event):
    global index
    global myJukebox
    pygame.mixer.music.pause()



def nextSong(event):
    global index
    global myJukebox
    index += 1
    #print("new index:", index)
    #print("these are the number of songs:", len(myJukebox.songTitles))
    if (index != 0) and (len(myJukebox.songTitles) != 0):
        pygame.mixer.music.load(myJukebox.listOfSongs[((index % len(myJukebox.songTitles)) -1)])
        pygame.mixer.music.play()
        pygame.mixer.music.play()
        myJukebox.updateLabel()

    else:
        pygame.mixer.music.load(myJukebox.listOfSongs[index - 1])
        pygame.mixer.music.play()
        pygame.mixer.music.play()
        myJukebox.updateLabel()


def previousSong(event):
    global index
    global myJukebox
    index -= 1
    #print("new index is:", index)
    #print("these are the number of songs:", len(myJukebox.songTitles))
    if (index != 0) and (len(myJukebox.songTitles) != 0):
        pygame.mixer.music.load(myJukebox.listOfSongs[((index % len(myJukebox.songTitles)) -1)])
        pygame.mixer.music.play()
        pygame.mixer.music.play()
        myJukebox.updateLabel()

    else:
        pygame.mixer.music.load(myJukebox.listOfSongs[index - 1])
        pygame.mixer.music.play()
        pygame.mixer.music.play()
        myJukebox.updateLabel()

def stopSong(event):
    global index
    global myJukebox
    pygame.mixer.music.stop()
    myJukebox.labelVar.set("")


if __name__ == "__main__":
    window = Tk()
    window.geometry("700x500+450+200")
    window.title("Jukebox")
    index = 1
    print("NOTE: ***** Choose the folder containing the background image. *****")
    folderForImage = askdirectory()
    os.chdir(folderForImage)
    for files in os.listdir(folderForImage):
        if files.endswith(".gif"):
            photoPath = os.path.realpath(files)
    myJukebox = Jukebox(window, index, photoPath)
    print("NOTE: ***** Now choose the directory containing the music files (.mp3 format) *****")
    myJukebox.directoryChooser()
    myJukebox.constructButtons()
    myJukebox.nextButton.bind("<Button-1>", nextSong)
    myJukebox.previousButton.bind("<Button-1>", previousSong)
    myJukebox.playResumeButton.bind("<Button-1>", playResumeSong)
    myJukebox.pauseButton.bind("<Button-1>", pauseSong)
    myJukebox.stopButton.bind("<Button-1>", stopSong)
    #print("The type of set_endevent:", type(pygame.mixer.music.set_endevent()))
    window.mainloop()
