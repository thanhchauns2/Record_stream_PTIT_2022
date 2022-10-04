import vlc # pip install python-vlc
from datetime import datetime
import time
import os
import schedule # pip install schedule

default_length = 60 # Seconds
vlcInstance = vlc.Instance("--demux=ts",b"--rtsp-frame-buffer-size=800000",b"--network-caching=1000")
path = "D://iec_ptit_2022/cvanomaly_detection/xarac/record16h_18h/scheduled/"

#get Preset Path
def get_path():
   
    if(os.path.exists(path) == False):
        os.makedirs(path)
    return path

def get_stream(length = default_length):
    mediaName = datetime.now().strftime("%m-%d-%Y-%Hh%Mm%Ss") +".avi"
    media_record = vlcInstance.media_new("rtsp://iocldg:iocldg123123@14.241.197.248:2006/cam/realmonitor?channel=1&subtype=0")
    media_record.add_option("sout=#duplicate{dst=file{access=file,mux=avi,dst="+get_path()+ "/" + mediaName+"},dst=display}")
    media = vlcInstance.media_player_new()
    media.set_media(media_record)
    media.play()
    time.sleep(length)
    media.stop()
    media.release()

scheduled_times = [
    ("15:41:00", 60),
    ("15:41:45", 75),
]

for x in scheduled_times:
    schedule.every().day.at(x[0]).do(get_stream,x[1])

def run():
    d1 = datetime.now()
    d1 = datetime(d1.year,d1.month,d1.day,18,1,0)
    while datetime.now() < d1:
        schedule.run_pending()
        time.sleep(1)

run()