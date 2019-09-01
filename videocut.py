from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from subprocess import call

# Variables
saveFile = ""
window = Tk()
window.title("video cut")
window.geometry('200x250')

selectinputlabel = Label(window, text="Select input video file")
selectinputlabel.grid(column=0, row=0)

inputFileLabel = Entry(window, width=30)
inputFileLabel.grid(column=0, row=1)

def inputFileItem():
    global inputFileItem
    inputFileItem = filedialog.askopenfilename()
    inputFileLabel.insert(END, inputFileItem)

inputButtonFile = Button(window, text="...", command=inputFileItem)
inputButtonFile.grid(column=8, row=1)

selectoutputlabel = Label(window, text="Select output for file")
selectoutputlabel.grid(column=0, row=2)

def saveFileItem():
    # Open file selecter and making path variable
    global saveFile
    saveFile = filedialog.asksaveasfilename()
    # Writing path to label
    saveFileLocation.insert(END, saveFile)
    # Debug messagebox with path
    #messagebox.showinfo('Selected video path',selectedFile)

saveFileLocation = Entry(window, width=30)
saveFileLocation.grid(column=0, row=3)

saveButtonFile = Button(window, text="...", command=saveFileItem)
saveButtonFile.grid(column=8, row=3)

selectStartLabel = Label(window, text="Start time (hh:mm:ss)")
selectStartLabel.grid(column=0, row=4)
startTimeEntry = Entry(window, width=20)
startTimeEntry.grid(column=0, row=5)

selectEndlabel = Label(window, text="Stop time (hh:mm:ss)")
selectEndlabel.grid(column=0, row=8)
stopTimeEntry = Entry(window, width=20)
stopTimeEntry.grid(column=0, row=9)

def slowerEnc():
    cmd = "ffmpeg -i " + inputFileItem + " -ss " + startTimeEntry.get() + " -t " + stopTimeEntry.get() + " -async 1 -strict -2 " + saveFile
    print("Command to execute: " + cmd)

def fasterEnc():
    cmd = "ffmpeg -ss " + startTimeEntry.get() + " -t " + stopTimeEntry.get() + " -i " + inputFileItem + " -acodec copy -vcodec copy -async 1 " + saveFile
    print("Command to execute: " + cmd)

slowgoButton = Button(window, text="Go! (slower)", command=slowerEnc)
slowgoButton.grid(column=0, row=11)

fastgoButton = Button(window, text="Go! (faster)", command=fasterEnc)
fastgoButton.grid(column=0, row=12)
window.mainloop()