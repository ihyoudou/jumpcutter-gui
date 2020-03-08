# Jumpcutter GUI
![screenshot](https://i.issei.space/hhlv4.png)
![screenshot](https://i.issei.space/01ucm.png)
## What is jumpcutter?
It is a Python script originally writed by [carykh](https://github.com/carykh/jumpcutter) that detect where in video volume level is lower than X value and cuts out those frames and audio.  
Warning: it can be using a lot of disk space and CPU, depends on quality and length of video you are trying to jumpcut
## What is jumpcutter-gui and videocut?
Jumpcutter-gui is my attempt to make something useful in Python, it is a GUI wrapper to jumpcutter.py, writen with Tkinter. Videocut is simple app to cut video based on start and end time, can be really useful if you don't want to jumpcut whole video.
## How to install
At first, make sure that you have installed FFMPEG and youtube-dl on your system.

```
git clone https://github.com/ihyoudou/jumpcutter-gui
cd jumpcutter-gui
pip install -r requirements.txt
python jumpcutter-gui.py
```
Tested on Windows 8.1 (amd64, Python 3.7.3), Windows 10 (amd64, Python 3.6.7), Debian 10.2 (amd64, Python 3.7.3)

## ToDo list
* Add option to select quality of downloaded youtube video
* Execute jumpcutter as subprocess instead of freezing whole GUI
* Clean-up GUI, make errors more clear and more usable

## Troubleshooting
**My final video have audio of sync, what to do?!**  
You need to specify FPS value, it is pretty common issue with 50fps videos

**Youtube-dl is not downloading youtube video**  
Please try updating youtube-dl to newest version using
```youtube-dl -U``` command
