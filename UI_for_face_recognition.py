import tkinter as tk
import cv2
from PIL import ImageTk, Image

IMAGE_PATH = 'assets/face_cam.png'
cam_on = False
cap = None


def show_frame():
    if cam_on:
        ret, frame = cap.read()
        if ret:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image).resize((822, 652))
            imgtk = ImageTk.PhotoImage(image=img)
            canvas_face_cam.imgtk = imgtk
            canvas_face_cam.create_image((302,150),image=imgtk)
        canvas_face_cam.after(10, show_frame)

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
    if camera_screen:
        canvas_face_cam.imgtk = camera_screen
        canvas_face_cam.create_image((302,150),image=camera_screen)
    else:
        print("Custom image not found")

# Create the main window
root = tk.Tk()
root.title("Main Window")
root.geometry("1000x600")
root.config(background="#576CA8")
root.grid_columnconfigure(0, minsize=600)
root.grid_columnconfigure(1, minsize=367)
root.grid_rowconfigure(0)
root.grid_rowconfigure(1, weight=1)

camera_screen = tk.PhotoImage(file = IMAGE_PATH).subsample(1)

header = tk.Label(root,text="Face-Recognition System")
header.grid(row=0,columnspan=2,pady=10)

# Create and place the frames
frame1 = tk.Frame(root, bg='#576CA8',width=600,height=500)
frame2 = tk.Frame(root, bg='green',width=367,height=500)

canvas_face_cam = tk.Canvas(frame1, width = 600, height = 300)
canvas_face_cam.create_image((302,150), image = camera_screen)
canvas_face_cam.pack(anchor="center",pady=100,fill=tk.BOTH)

#buttons 
TurnCameraOn = tk.Button(frame1, text="Start Video", command=start_vid, anchor="center")
TurnCameraOn.place(anchor="center",x=250,y= 425)
TurnCameraOff = tk.Button(frame1, text="Stop Video", command=stop_vid, anchor="center")
TurnCameraOff.place(anchor="center",x=350,y= 425)

frame1.grid(row=1, column=0, sticky="nsew", padx=(5, 10))
frame2.grid(row=1, column=1, sticky="nsew", padx=(10, 5))




# Run the main loop
root.mainloop()
