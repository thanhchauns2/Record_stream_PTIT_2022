import vlc # pip install python-vlc
from datetime import datetime
import time
import os

default_length = 60 # Seconds
vlcInstance = vlc.Instance("--demux=ts",b"--rtsp-frame-buffer-size=800000",b"--network-caching=1000")
path = "/Streams/"

#get Preset Path
def get_path():
   
    if(os.path.exists(path) == False):
        os.makedirs(path)
    return path

def get_stream(length = default_length):
    mediaName = datetime.now().strftime("%m-%d-%Y-%Hh%Mm%Ss") +".avi"
    media_record = vlcInstance.media_new("rtsp://iocldg:iocldg123123@14.241.197.248:2006/cam/realmonitor?channel=1&subtype=0")
    media_record.add_option("sout=#duplicate{dst=file{access=file,mux=avi,dst="+get_path()+ "/" + mediaName+"}}")
    media = vlcInstance.media_player_new()
    media.set_media(media_record)
    media.play()
    time.sleep(length)
    media.stop()
    media.release()

for i in range(10):
    get_stream(600)
    time.sleep(600)
