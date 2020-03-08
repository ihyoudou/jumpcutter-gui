# Jumpcutter-gui by Issei Hyoudou 2020
# Contact: issei@issei.space
# Repo: https://github.com/isseihere/jumpcutter-gui
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import os.path
import shutil
from subprocess import call

window = Tk()
window.title("Jumpcutter GUI")
window.geometry('320x330')
window.resizable(False, False)

# Variables
selectedFile = ""
saveFile = ""
hiddenLocal = False
hiddenURL = True
jumpcutterCMD = "python jumpcutter.py"


# Checking if TEMP folder exist (failed/cancelled task)
if os.path.exists("TEMP"):
    MsgBox = messagebox.askquestion ('Warning','TEMP folder exist, probably because of failed or canceled job. Do you want do delete it?',icon = 'warning')
    if MsgBox == 'yes':
        # If user select yes then remove TEMP folder and ignore (readonly) errors
        shutil.rmtree("TEMP", ignore_errors=True)

# First group of widgets - select original file and place to save jumpcutted version
group1 = LabelFrame(window, text="Main", padx=1, pady=1)
group1.grid(padx=1, pady=1)

grouplocalremote = LabelFrame(group1, text="Use Local/URL", padx=1, pady=1)
grouplocalremote.grid(padx=1, pady=1)

def localfile():
    global hiddenLocal
    if hiddenLocal:
        labelLocalFile.grid()
        fileLocation.grid()
        selectFile.grid()
        labelURLFile.grid_remove()
        URLLocation.grid_remove()
    else:
        labelURLFile.grid_remove()
        URLLocation.grid_remove()
        selectFile.grid()
        labelLocalFile.grid()
        fileLocation.grid()
    print("Selected Local/URL value: " + option.get())

def useurl():
    global hiddenURL
    if hiddenURL:
        # Action if URL radiobutton is selected
        labelLocalFile.grid_remove()
        fileLocation.grid_remove()
        selectFile.grid_remove()
        labelURLFile.grid()
        URLLocation.grid()
        
        hiddenLocal = False
    else:
        # Action if URL radiobutton is not selected
        labelURLFile.grid()
        URLLocation.grid()
        selectFile.grid_remove()
        labelLocalFile.grid_remove()
        fileLocation.grid_remove()
        hiddenLocal = True
    hiddenURL = not hiddenURL
    print("Selected Local/URL value: " + option.get())

# Variable that is responsible for allow only one radiobutton to be selected
option = StringVar()
# By default select local file radiobutton
option.set("local")
# Local file radiobutton 
localfilechk = Radiobutton(grouplocalremote, text='Local File', command=localfile, var=option, value="local")
localfilechk.grid(column=0, row=0)
# URL radiobutton
urlchk = Radiobutton(grouplocalremote,text='Use URL', command=useurl, var=option, value="url")
urlchk.grid(column=1, row=0)

labelLocalFile = Label(group1, text="Original video file")
labelLocalFile.grid(column=0, row=1)
labelURLFile = Label(group1, text="Original video URL")
labelURLFile.grid(column=0, row=1)
# Remove on startup URL label
labelURLFile.grid_remove()


fileLocation = Entry(group1,width=48)
fileLocation.grid(column=0, row=2)

URLLocation = Entry(group1,width=48)
URLLocation.grid(column=0, row=2)
# Remove on startup URL textbox
URLLocation.grid_remove()
# Action after pressing ... button to selectfile
def selectFileItem():
    # Open file selecter and making path variable
    global selectedFile
    # Clearing saveFileLocation
    saveFileLocation.delete(0, END)
    selectedFile = filedialog.askopenfilename()
    # Writing path to label
    fileLocation.insert(END, selectedFile)
    # Getting table with base filename
    baseFileName = os.path.basename(selectedFile)
    # Variable only with extension
    extension = os.path.splitext(baseFileName)[1]
    # Original path to file without file and extension
    originalPath = selectedFile.replace(baseFileName, '')
    # Combaining original Path with filename (without extension)
    finalname = (originalPath + os.path.splitext(baseFileName)[0])
    # Inserting original Path with filename + _jumpcut suffix + original extension
    if (selectedFile != ""):
        saveFileLocation.insert(END, finalname + '_jumpcut' + extension)
    # Writing save location to variable
    global saveFile
    saveFile = saveFileLocation.get()

    # Debug messagebox with path
    #messagebox.showinfo('Selected video path',selectedFile)
    
# Button to open file item selection box
selectFile = Button(group1, text="...", command=selectFileItem)
selectFile.grid(column=2, row=2)

label2 = Label(group1, text="Save to")
label2.grid(column=0, row=3)

saveFileLocation = Entry(group1,width=48)
saveFileLocation.grid(column=0, row=4)
# Action after pressing ... button to save file
def saveFileItem():
    # Open file selecter and making path variable
    global saveFile
    saveFile = filedialog.asksaveasfilename()
    # Writing path to label
    saveFileLocation.insert(END, saveFile)
    # Debug messagebox with path
    #messagebox.showinfo('Selected video path',selectedFile)
    

saveButtonFile = Button(group1, text="...", command=saveFileItem)
saveButtonFile.grid(column=2, row=4)

# Group 2 - it is for general manipulation, FPS, sounded speed, silent threshold, silent speed
group2 = LabelFrame(window, text="General", padx=1, pady=1)
group2.grid(padx=0, pady=0)


label2 = Label(group2, text="Video FPS (def=auto)")
label2.grid(column=0,row=1)
fps = Entry(group2,width=4)
fps.grid(column=4, row=1)

label3 = Label(group2, text="Sounded speed (def=1)")
label3.grid(column=0,row=5)
soundspeed = Entry(group2,width=4)
soundspeed.insert(0, '1')
soundspeed.grid(column=4, row=5)

label4 = Label(group2, text="Silent threshold (from 0 to 1)")
label4.grid(column=0,row=7)
silentthreshold = Entry(group2,width=4)
silentthreshold.grid(column=4, row=7)

label5 = Label(group2, text="Silent speed (default=99999)")
label5.grid(column=0,row=9)
silentspeed = Entry(group2,width=4)
silentspeed.insert(0, '99999')
silentspeed.grid(column=4, row=9)

# quality of frames to be extracted from input video. 1 is highest, 31 is lowest, 3 is the default.
qualityLabel = Label(group2, text="Quality of frames (default=3)")
qualityLabel.grid(column=0,row=10)
framesQuality = Entry(group2,width=4)
framesQuality.insert(0, '3')
framesQuality.grid(column=4, row=10)

# Action after clicking start button
def execute():
    global jumpcutterCMD
    # Checking if file is selected + base command
    if option.get() == "local":
        if selectedFile == "":
            messagebox.showinfo('Warning', "Input file was not set!")
        else:
            jumpcutterCMD = jumpcutterCMD + " --input_file " + selectedFile
    elif option.get() == "url":
        if URLLocation.get() == "":
            messagebox.showinfo('Warning', "Input URL was not set!")
        else:
            jumpcutterCMD = jumpcutterCMD + " --url " + URLLocation.get()

    # Checking if save destination entry is empty
    if saveFile == "":
       print("Output file was not set!")
    else:
        jumpcutterCMD = jumpcutterCMD + " --output_file " + saveFile

    # Checking if fps entry is empty
    if fps.index("end") == 0:
        print("FPS entry is empty, using autodetect. If your final video is out of sync you need to enter proper FPS value")
    else:
       jumpcutterCMD = jumpcutterCMD + " --frame_rate " + fps.get()

    # Checking if sound speed entry is empty
    if soundspeed.index("end") == 0:
        print("Sounded speed is empty, using default (1)")
    else:
        jumpcutterCMD = jumpcutterCMD + " --sounded_speed " + soundspeed.get()

    # Checking if silent threshold entry is empty
    if silentthreshold.index("end") == 0:
        print("Silent threshold is empty, using default (1)")
    else:
        jumpcutterCMD = jumpcutterCMD + " --silent_threshold " + silentthreshold.get()

    # Checking if silent speed entry is empty
    if silentspeed.index("end") == 0:
        print("Silent speed is empty")
    else:
        jumpcutterCMD = jumpcutterCMD + " --silent_speed " + silentspeed.get()
    
    # Checking if frames quality entry is empty
    if framesQuality.index("end") == 0:
        print("Frames quality entry is empty, using default")
    else:
        jumpcutterCMD = jumpcutterCMD + " --frame_quality " + framesQuality.get()

    # Debug msgbox with command that will be executed
    print('Executing: ' + jumpcutterCMD)
    messagebox.showinfo('jumpcutter-gui', "Main GUI window will be unresponsive until jumpcutting process will be finished, please check terminal output for more information")
    # Executing command
    
    call(jumpcutterCMD, shell=True)
    # !!! Add support detection for linux and macos and error detection
    if os.path.exists(".jumpcutterdone") == True:
        os.remove(".jumpcutterdone")
        print('Jumpcutting has finished with success, deleting .jumpcutterdone file')
        MsgBox = messagebox.askquestion ('Done!','Jumpcutting is done, do you want play jumpcutted version?',icon = 'info')
        if MsgBox == 'yes':
            call(saveFile, shell=True)
    else:
        print('Error! .jumpcutterdone was not found')
        messagebox.showerror('Error!', "An error occurred, please check your terminal window")

executeButton = Button(window, text="Start", command=execute)
executeButton.grid(column=0,row=8)
window.mainloop()