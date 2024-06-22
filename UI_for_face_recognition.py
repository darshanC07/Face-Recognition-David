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
    

def close_cam():
    close_cam_button = tk.Button(root, text="Close camera",command=default_cam_screen)
    close_cam_button.pack()
    if cv2.waitKey(1)==ord("q"):
        cap.release()
        label_widget.config(image="./images.chair.jpg")
    
def default_cam_screen():
    cam_screen_widget = tk.Label(root,text="Face Camera", width=500, height=500)
    cam_screen_widget.place(x=label_widget.winfo_x(),y=label_widget.winfo_y())

    

root = tk.Tk()

label = tk.Label(root,text="FACE-RECOGNITION SYSTEM")
label.pack()

w = 800 # width for the Tk root
h = 650 # height for the Tk root

root.geometry(f"{w}x{h}")

cam_button = tk.Button(root, text="Open camera",command=lambda:[open_cam(),close_cam()])
cam_button.pack()

# cam_frame = tk.Frame(root,width=500, height=500)
# cam_frame.place(x=100)


label_widget = tk.Label(root, width=500, height=500)
label_widget.pack()



root.mainloop() # starts the mainloop

    
