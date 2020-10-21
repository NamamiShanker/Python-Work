import cv2
from PIL import Image
from PIL import ImageTk
import threading
import tkinter as tk


def button1_clicked(videoloop_stop):
    threading.Thread(target=videoLoop, args=(videoloop_stop,)).start()


def button2_clicked(videoloop_stop):
    videoloop_stop[0] = True


def videoLoop(mirror=False):
    No = 0
    cap = cv2.VideoCapture(No)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

    while True:
        ret, to_draw = cap.read()
        if mirror is True:
            to_draw = to_draw[:, ::-1]

        image = cv2.cvtColor(to_draw, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        panel = tk.Label(image=image)
        panel.image = image
        panel.place(x=50, y=50)

        # check switcher value
        if videoloop_stop[0]:
            # if switcher tells to stop then we switch it again and stop videoloop
            videoloop_stop[0] = False
            panel.destroy()
            break


# videoloop_stop is a simple switcher between ON and OFF modes
videoloop_stop = [False]

root = tk.Tk()
root.geometry("1920x1080+0+0")

button1 = tk.Button(
    root, text="start", bg="#fff", font=("", 50),
    command=lambda: button1_clicked(videoloop_stop))
button1.place(x=1000, y=100, width=400, height=250)

button2 = tk.Button(
    root, text="stop", bg="#fff", font=("", 50),
    command=lambda: button2_clicked(videoloop_stop))
button2.place(x=1000, y=360, width=400, height=250)

root.mainloop()