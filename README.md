# jumpcutter-gui
![screenshot](https://i.issei.space/hhlv4.png)
## What is jumpcutter?
It is a Python script originally writed by [carykh](https://github.com/carykh/jumpcutter) that detect where in video volume level is lower than X value and cuts out those frames and audio.  
Warning: it can be using a lot of disk space and CPU, depends on quality and length of video you are trying to jumpcut
## What is jumpcutter-gui and videocut?
Jumpcutter-gui is my attempt to make something useful in Python, it is a GUI wrapper to jumpcutter.py, writen with Tkinter. Videocut is simple app to cut video based on start and end time, can be really useful if you don't want to jumpcut whole video.
## How to install
Manual way:  
```
git clone https://github.com/ihyoudou/jumpcutter-gui
cd jumpcutter-gui
pip install -r requirements.txt
python jumpcutter-gui.py
```
You also need to have ffmpeg installed!

Tested on Windows 8.1 (amd64, Python 3.7.3), Windows 10 (amd64, Python 3.6.7)

## Troubleshooting
**My final video have audio of sync, what to do?!**  
You need to specify FPS value, it is pretty common issue with 50fps videos

