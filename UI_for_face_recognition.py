import tkinter as tk
from PIL import Image, ImageTk
import cv2

cap = cv2.VideoCapture(0)

def open_cam():
    ret, frame = cap.read()
    rgba_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    
    captured_img = Image.fromarray(rgba_frame)
    
    photo_image = ImageTk.PhotoImage(image=captured_img)
    
    label_widget.photo_image = photo_image
    
    label_widget.configure(image=photo_image)

    label_widget.after(10, open_cam)



root = tk.Tk()

label = tk.Label(root,text="FACE-RECOGNITION SYSTEM")
label.pack()

w = 800 # width for the Tk root
h = 650 # height for the Tk root

root.geometry(f"{w}x{h}")

cam_button = tk.Button(root, text="Open camera",command=open_cam)
cam_button.pack()

label_widget = tk.Label(root)
label_widget.pack()

root.mainloop() # starts the mainloop

    
