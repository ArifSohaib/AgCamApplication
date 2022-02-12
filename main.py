#!/usr/bin/env pipenv-shebang

import tkinter
from PIL import Image, ImageTk
import imageio 
from datetime import datetime
from pathlib import Path
from apscheduler.schedulers.background import BackgroundScheduler



def take_image_now():
    print(f"took image at {datetime.now()}")
    current_task_label['text'] = f"took image at {datetime.now()}"
    image = video.get_next_data()
    image_PIL = Image.fromarray(image)
    image_PIL.save(Path(Path.cwd(),"data",f"image_{datetime.now()}.jpg"))

def start_scheduler():
    current_task_label['text'] = f"started scheduler at {datetime.now()}"
    scheduler.resume()

def stop_scheduler():
    current_task_label['text'] = f"stopped scheduler at {datetime.now()}"
    scheduler.pause()

def stream():
    try:
        image = video.get_next_data()
        frame_image = Image.fromarray(image)
        frame_image = frame_image.rotate(180)
        frame_image=ImageTk.PhotoImage(frame_image)
        l1.config(image=frame_image)
        l1.image = frame_image
        l1.after(delay, lambda: stream())
    except:
        video.close()
        return 

scheduler = BackgroundScheduler()
window = tkinter.Tk()
window.title("AgCam Data Recorder")
window.minsize(width=500, height=300)
my_label = tkinter.Label(text="Farmaid AgCam Recorder", font=("Ariel",24,"bold"))
my_label.pack(side="top")
current_task_label = tkinter.Label(text="Current Task: Streaming video",font=("Ariel",18,"bold"))
start_interval_button = tkinter.Button(text="Take Picture every 15 minutes", command=start_scheduler)
stop_interval_button = tkinter.Button(text="Stop taking pictures automatically", command=stop_scheduler)
take_pic_now = tkinter.Button(text="Take Picture Now", command=take_image_now)


frame = tkinter.Frame()
l1 = tkinter.Label(frame)
video = imageio.get_reader("<video0>")
start_interval_button.pack(side = tkinter.RIGHT)
stop_interval_button.pack(side = tkinter.RIGHT)
take_pic_now.pack(side = tkinter.RIGHT)
l1.pack()
frame.pack()
current_task_label.pack()
delay = int(1000 / video.get_meta_data()['fps'])
stream()
scheduler.add_job(take_image_now,'interval',seconds=15)
scheduler.start(paused=True)
window.mainloop()