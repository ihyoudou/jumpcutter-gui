# jumpcutter-gui
## What is jumpcutter?
It is a Python script originally writed by [carykh](https://github.com/carykh/jumpcutter) that detect where in video volume level is lower than X value and cuts out those frames and audio.
## How to install
Manual way:  
```
git clone https://github.com/isseihere/jumpcutter-gui
cd jumpcutter-gui
pip install -r requirements.txt
python jumpcutter-gui.py
```
You also need to have ffmpeg installed!

Tested on Windows 8.1 (amd64, Python 3.7.3), Windows 10 (amd64, Python 3.7.3), Debian buster (i386, Python)

## Troubleshooting
**My final video have audio of sync, what to do?!**  
You need to specify FPS value, it is pretty common issue with 50fps videos

## Known issues
- Youtube links don't work (some sort of problem in pyTube, need to be replaced with youtube-dl)
