from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import os.path
import shutil
from subprocess import call

window = Tk()
window.title("jumpcutter-gui")
window.geometry('320x300')

# Variables
selectedFile = ""
saveFile = ""
hiddenLocal = False
hiddenURL = True




# Checking if TEMP folder exist (failed/cancelled task)
if os.path.exists("TEMP"):
    MsgBox = messagebox.askquestion ('Warning','TEMP folder exist, probably because of failed/canceled job. Do you want do delete it? If you dont delete it, jumpcutting will fail.',icon = 'warning')
    if MsgBox == 'yes':
        # If user select yes then remove TEMP folder and ignore (readonly) errors
        shutil.rmtree("TEMP", ignore_errors=True)

# First group of widgets - select original file and place to save jumpcutted
group1 = LabelFrame(window, text="File", padx=1, pady=1)
group1.grid(padx=1, pady=1)

grouplocalremote = LabelFrame(group1, text="Use Local/URL", padx=1, pady=1)
grouplocalremote.grid(padx=1, pady=1)

def localfile():
    global hiddenLocal
    if hiddenLocal:
        fileLocation.grid_remove()
        labelURLFile.grid()
    else:
        fileLocation.grid()
    hiddenLocal = not hiddenLocal

def useurl():
    global hiddenURL
    if hiddenURL:
        fileLocation.grid_remove()
        labelLocalFile.grid_remove()

        labelURLFile.grid()
    else:
        fileLocation.grid()
        labelLocalFile.grid()
    hiddenURL = not hiddenURL

localFilechkstate = BooleanVar()
localFilechkstate.set(True) #set check state

urlchkstate = BooleanVar()
urlchkstate.set(False) #set check state

localFilechk = Checkbutton(grouplocalremote, text='Local File', command=localfile, var=localFilechkstate)
localFilechk.grid(column=0, row=0)
urlchk = Checkbutton(grouplocalremote,text='Use URL', command=useurl, var=urlchkstate)
urlchk.grid(column=1, row=0)

labelLocalFile = Label(group1, text="Select your original video file")
labelLocalFile.grid(column=0, row=1)
labelURLFile = Label(group1, text="Enter your URL")
labelURLFile.grid(column=0, row=1)


fileLocation = Entry(group1,width=48)
fileLocation.grid(column=0, row=2)
# Action after pressing ... button to selectfile
def selectFileItem():
    # Open file selecter and making path variable
    global selectedFile
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
    saveFileLocation.insert(END, finalname + '_jumpcut' + extension)
    # Writing save location to variable
    global saveFile
    saveFile = saveFileLocation.get()

    # Debug messagebox with path
    #messagebox.showinfo('Selected video path',selectedFile)
    
# Button to open file item selection box
selectFile = Button(group1, text="...", command=selectFileItem)
selectFile.grid(column=2, row=2)

label2 = Label(group1, text="Localization of jumpcutted video file")
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

label3 = Label(group2, text="Sounded speed (default=1)")
label3.grid(column=0,row=5)
soundspeed = Entry(group2,width=4)
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

# Action after clicking Go! button
def execute():

    # Checking if file is selected + base command
    if selectedFile == "":
        messagebox.showinfo('Warning', "Input file was not set!")
    else:
        jumpcutterCMD = "python jumpcutter.py --input_file " + selectedFile

    # Checking if save destination entry is empty
    if saveFile == "":
        messagebox.showinfo('Warning', "Output file was not set!")
    else:
        jumpcutterCMD = jumpcutterCMD + " --output_file " + saveFile

    # Checking if fps entry is empty
    if fps.index("end") == 0:
        fps_empty = True
    else:
       jumpcutterCMD = jumpcutterCMD + " --frame_rate " + fps.get()

    # Checking if sound speed entry is empty
    if soundspeed.index("end") == 0:
        soundspeed_empty = True
    else:
        jumpcutterCMD = jumpcutterCMD + " --sounded_speed " + soundspeed.get()

    # Checking if silent threshold entry is empty
    if silentthreshold.index("end") == 0:
        silentthreshold_empty = True
    else:
        jumpcutterCMD = jumpcutterCMD + " --silent_threshold " + silentthreshold.get()

    # Checking if silent speed entry is empty
    if silentspeed.index("end") == 0:
        silentspeed_empty = True
    else:
        jumpcutterCMD = jumpcutterCMD + " --silent_speed " + silentspeed.get()

    # Debug msgbox with command that will be executed
    messagebox.showinfo('Executing', jumpcutterCMD)
    messagebox.showinfo('jumpcutter-gui', "Main GUI window will be unresponsive until jumpcutting process will be finished")
    # Executing command
    # !!! Add support detection for linux and macos
    call(jumpcutterCMD, shell=True)
    MsgBox = messagebox.askquestion ('Done!','Jumpcutting is done, do you want to play jumpcutted version?',icon = 'info')
    if MsgBox == 'yes':
        call(saveFile, shell=True)

executeButton = Button(window, text="Go!", command=execute)
executeButton.grid(column=0,row=8)
window.mainloop()


