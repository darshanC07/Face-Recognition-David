import cv2
from tkinter import *
from PIL import Image, ImageTk


cam_on = False
cap = None
mainWindow = Tk()
mainWindow.geometry("800x650")


# mainFrame = Frame(mainWindow, height = 640, width = 810)
# mainFrame.place(x=350,y=0)
# mainFrame.pack()

# cameraFrame = Frame(mainWindow, height = 640, width = 405)
# cameraFrame.pack()
   

def show_frame():

    if cam_on:

        ret, frame = cap.read()    

        if ret:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    
            img = Image.fromarray(cv2image).resize((810,640))
            imgtk = ImageTk.PhotoImage(image=img)        
            vid_lbl.imgtk = imgtk    
            vid_lbl.configure(image=imgtk)    
        
        vid_lbl.after(10, show_frame)

def start_vid():
    vid_lbl.pack()
    global cam_on, cap
    stop_vid()
    cam_on = True
    cap = cv2.VideoCapture(0) 
    show_frame()

def stop_vid():
    global cam_on
    cam_on = False
    
    if cap:
        cap.release()
        
        
header_label = Label(mainWindow,width=100, height=100, anchor=CENTER)
header_label.pack()

vid_lbl = Label(mainWindow)
# vid_lbl.grid(row=0, column=0)

#Buttons
TurnCameraOn = Button(header_label, text="start Video", command=start_vid,anchor=CENTER)
TurnCameraOn.grid(row=1,column=0, pady=20)
TurnCameraOff = Button(header_label, text="stop Video", command=stop_vid,anchor=CENTER)
TurnCameraOff.grid(row=1, column=1, padx=20,pady=20)

mainWindow.mainloop()
