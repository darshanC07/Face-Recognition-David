import cv2
from tkinter import *
from PIL import Image, ImageTk
import os

cam_on = False
cap = None

mainWindow = Tk()
mainWindow.geometry("900x1000")

# Load the custom image to be displayed when the camera is off
custom_img_path = "C:/Users/acer/OneDrive/Documents/Darshan's project/Python projects/face_recognition_system/final_face_recognition/face-cam.jpg"  

if os.path.exists(custom_img_path):
    custom_img = Image.open(custom_img_path).resize((822, 652))
    custom_imgtk = ImageTk.PhotoImage(custom_img)
else:
    print(f"Error: {custom_img_path} does not exist")
    custom_imgtk = None

def show_frame():
    if cam_on:
        ret, frame = cap.read()
        if ret:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image).resize((822, 652))
            imgtk = ImageTk.PhotoImage(image=img)
            vid_lbl.imgtk = imgtk
            vid_lbl.configure(image=imgtk)
        vid_lbl.after(10, show_frame)

def start_vid():
    global cam_on, cap
    if cam_on:
        stop_vid()
    cam_on = True
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video capture")
        return
    show_frame()

def stop_vid():
    global cam_on
    cam_on = False
    if cap and cap.isOpened():
        cap.release()
    # Display the custom image if available
    if custom_imgtk:
        vid_lbl.imgtk = custom_imgtk
        vid_lbl.configure(image=custom_imgtk)
    else:
        print("Custom image not found")

header_label = Label(mainWindow, width=60, height=100, anchor=CENTER)
header_label.pack()

vid_lbl = Label(mainWindow,highlightbackground="black",highlightthickness=4, width=800,height=650)

if custom_imgtk:
    vid_lbl.imgtk = custom_imgtk
    vid_lbl.configure(image=custom_imgtk)

vid_lbl.pack()

mainWindow.update()
# print(vid_lbl.winfo_reqwidth(),vid_lbl.winfo_reqheight())

# Buttons
TurnCameraOn = Button(header_label, text="Start Video", command=start_vid, anchor=CENTER)
TurnCameraOn.grid(row=1, column=0, pady=20)
TurnCameraOff = Button(header_label, text="Stop Video", command=stop_vid, anchor=CENTER)
TurnCameraOff.grid(row=1, column=1, padx=20, pady=20)

mainWindow.mainloop()
