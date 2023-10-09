import tkinter as tk
import sys, time, threading
import vlc

name_station = ["Рок", "Музыка 80-ых", "Европа Плюс", "Музыка 90-ых", "Джаз", "КИНО"]

chanals = ["http://jfm1.hostingradio.ru:14536/rock00.mp3",
          "http://europaplus.hostingradio.ru:8014/retro80-128.mp3",
          "http://europaplus.hostingradio.ru:8014/ep-light128.mp3",
          "http://europaplus.hostingradio.ru:8014/retro90-128.mp3",
          "http://europaplus.hostingradio.ru:8014/retro90-128.mp3",
          "http://pub0101.101.ru:8000/stream/pro/aac/64/103"
          ]

radio_idx = 0
flag = 0

def thread(my_func):
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper

@thread
def playradio(canals):
    global flag
    flag = 1
    ppp = vlc.MediaPlayer(canals)
    ppp.play()
    while flag == 1:
        time.sleep(1)
    ppp.stop()

def PlayMusic():
    global flag, chanals, radio_idx
    flag = 0
    time.sleep(1)
    playradio(chanals[radio_idx])

def stopRadio():
    global flag
    flag = 0
    time.sleep(1)

def forward_station():
    global radio_idx, chanals
    radio_idx += 1
    if radio_idx > 5:
        radio_idx = 0
    label_radio_name["text"] = str(name_station[radio_idx])
    label_radio_name.update()
    PlayMusic()

def backward_station():
    global radio_idx
    radio_idx -= 1
    if radio_idx < 0:
        radio_idx = 5
    label_radio_name["text"] = str(name_station[radio_idx])
    label_radio_name.update()
    PlayMusic()
    

root = tk.Tk()

root.geometry("500x200")
root.resizable(False, False)

label_radio_name = tk.Label(root, text=str(name_station[radio_idx]), font=("Helvetica", 48))
button_forward = tk.Button(root, text="Forward",pady=2, padx=2, command=forward_station)
button_backward = tk.Button(root, text="Backward",pady=2, padx=2, command=backward_station)
button_on = tk.Button(root, text="On",pady=2, padx=2, command=PlayMusic)
button_off = tk.Button(root, text="Off",pady=2, padx=2, command=stopRadio)

label_radio_name.pack()
button_forward.pack()
button_backward.pack()
button_on.pack()
button_off.pack()


