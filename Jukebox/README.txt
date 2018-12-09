# CSC111-FinalProject-Jukebox


## Objective 

This jukebox is basically a python(2.7 & 3.0) based music player which play songs in the chosen folder. It functions in the same way as online music players such as Spotify, apple music, and etc. 

## Description

 The jukebox displays a list of songs that the music directory selected by the user contains. Know that the jukebox currently only supports the **.mp3 format** media files.  **BEFORE YOU START THE PROGRAM, YOU NEED TO KNOW A FEW THINGS:** 

1. The very **first command to select a directory** is to direct the user to select a folder containing a “**.gif**” background image. The user is free to choose a background of their own choice, but the jukebox window is optimized for the background image provided with the jukebox program file, hence they might want to use that. 

2. The **second command to select a directory** is to direct the user to select a folder containing the **.mp3** music files. **PLEASE NOTE:** the music files to be selected ideally should have metadata music tags attached to them (**explanation:** Music metadata, which is also referred to as ID3 metadata, is the information embedded in an audio file that is used to identify the content of the media files. The tag basically consists of the **title, artist, album, year released, and genre** information. Note that this is important because the user could name a particular media file just about anything and to display that inaccurate file name in the jukebox as a song title is incorrect and gives no information about the song playing whatsoever, hence the need for media files with relevant metadata.). 


## Installation
Execute the programs using the terminal (Mac OS). Before installing the modules on the terminal, check if your Python is at least version 3.7. 


1. Python version check:
```
python --version
```
2. pygame module
```
sudo pip install pygame
```

3. eyed3 module
 - Install hombrew (https://brew.sh/)
 - Follow the instruction written on the homepage
 - ```pip install eyed3```
 
## How to Run Jukebox.py
In the command line, first change the directory to the folder “Jukebox”, and pass the following command “python3 jukebox.py”. **Remember**: the **python3** is extremely important because macOS have preinstalled python 2.7 and the program need to run with Python 3.7.0 (the eyed3 module won’t be imported with Python 2.7). 


## Known Bugs
The jukebox.py has several different known bugs:
- The user cannot randomly play songs from the song list. The jukebox doesn’t have the function to shuffle the songs. 
- The jukebox doesn’t automatically move on to the next song once the previous song finishes playing. The user has to manually click either next song, previous song or play to play the song list from up top. 
- The jukebox doesn’t have a function to play one single song repeatedly. In order to play the song repeatedly, the user has to wait until the jukebox moves on to the next song and click on the previous song.
- In order for the Jukebox to display the name of the ‘Now Playing’ song, the songs must have music tag. 


