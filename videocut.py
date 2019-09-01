# Videocut by Issei Hyoudou 2019
# contact: issei@issei.space
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from subprocess import call
import os.path

# Variables
saveFile = ""
window = Tk()
window.title("Videocut")
window.geometry('200x250')
window.resizable(False, False)

# Input file widgets
selectinputlabel = Label(window, text="Select input file")
selectinputlabel.grid(column=0, row=0)

inputFileLabel = Entry(window, width=28)
inputFileLabel.grid(column=0, row=1)

def inputFileItem():
    global inputFileItem
    inputFileItem = filedialog.askopenfilename()
    inputFileLabel.insert(END, inputFileItem)
    # Getting table with base filename
    baseFileName = os.path.basename(inputFileItem)
    # Variable only with extension
    extension = os.path.splitext(baseFileName)[1]
    # Original path to file without file and extension
    originalPath = inputFileItem.replace(baseFileName, '')
    # Combaining original Path with filename (without extension)
    finalname = (originalPath + os.path.splitext(baseFileName)[0])
    # Inserting original Path with filename + _jumpcut suffix + original extension
    saveFileLocation.insert(END, finalname + '_cut' + extension)
    # Writing save location to variable
    global saveFile
    saveFile = saveFileLocation.get()

inputButtonFile = Button(window, text="...", command=inputFileItem)
inputButtonFile.grid(column=1, row=1)

# Widgets for selecting output for final video
# By default program will output video with _cut sufix in the same directory
selectoutputlabel = Label(window, text="Select output for file")
selectoutputlabel.grid(column=0, row=2)

def saveFileItem():
    # Open file selecter and making path variable
    global saveFile
    saveFile = filedialog.asksaveasfilename()
    # Writing path to label
    saveFileLocation.insert(END, saveFile)
    # Debug messagebox with path
    #print('Selected video path: ' + selectedFile)

saveFileLocation = Entry(window, width=28)
saveFileLocation.grid(column=0, row=3)

saveButtonFile = Button(window, text="...", command=saveFileItem)
saveButtonFile.grid(column=1, row=3)

selectStartLabel = Label(window, text="Start time (hh:mm:ss)")
selectStartLabel.grid(column=0, row=4)
startTimeEntry = Entry(window, width=20)
startTimeEntry.grid(column=0, row=5)

selectEndlabel = Label(window, text="Stop time (hh:mm:ss)")
selectEndlabel.grid(column=0, row=8)
stopTimeEntry = Entry(window, width=20)
stopTimeEntry.grid(column=0, row=9)

# Why there is two cutting options?
# It is because there are utilizing diffrent ffmpeg funcitions, faster one just extract portion of video, that is not compatible with all video formats
# and might cause a/v desync
# Secound option, slower, extract frames and re-encode video, a/v desync should not occur there

def slowerEnc():
    cmd = "ffmpeg -i " + inputFileItem + " -ss " + startTimeEntry.get() + " -t " + stopTimeEntry.get() + " -async 1 -strict -2 " + saveFile
    print("Command to execute: " + cmd)
    call(cmd, shell=True)

def fasterEnc():
    cmd = "ffmpeg -ss " + startTimeEntry.get() + " -t " + stopTimeEntry.get() + " -i " + inputFileItem + " -acodec copy -vcodec copy -async 1 " + saveFile
    print("Command to execute: " + cmd)
    call(cmd, shell=True)

slowgoButton = Button(window, text="Go! (slower)", command=slowerEnc)
slowgoButton.grid(column=0, row=12,sticky=E+W)

fastgoButton = Button(window, text="Go! (faster)", command=fasterEnc)
fastgoButton.grid(column=0, row=13,sticky=E+W)
window.grid_columnconfigure(1,weight=1)
window.mainloop()