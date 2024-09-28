import tkinter as tk
import cv2
from PIL import ImageTk, Image

IMAGE_PATH = 'assets/face_cam.png'
cam_on = False
cap = None
current_y = 10  # Starting y-coordinate for the first text message

def text_adder(role, text):
    global current_y
    text_container.create_text((10, current_y), text=f"{role} : {text}", fill="white", font=("Merriweather", 10, "bold"), anchor="nw")
    current_y += 20  # Move down for the next message
    text_container.config(scrollregion=text_container.bbox("all"))  # Update scroll region

def show_frame():
    if cam_on:
        ret, frame = cap.read()
        if ret:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image).resize((822, 652))
            imgtk = ImageTk.PhotoImage(image=img)
            canvas_face_cam.imgtk = imgtk
            canvas_face_cam.create_image((302, 150), image=imgtk)
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
        canvas_face_cam.create_image((302, 190), image=camera_screen)
    else:
        print("Custom image not found")

# Create the main window
root = tk.Tk()
root.title("Main Window")
root.geometry("1000x600")
root.config(background="#576CA8")
root.resizable(False,False)
root.grid_columnconfigure(0, minsize=600)
root.grid_columnconfigure(1, minsize=367)
root.grid_rowconfigure(0)
root.grid_rowconfigure(1, weight=1)

camera_screen = tk.PhotoImage(file=IMAGE_PATH).subsample(1)
rounded_frame2_bg = tk.PhotoImage(file="./assets/frame2bg.png")

header = tk.Label(root, text="Face-Recognition System", bg="#576CA8", fg="white", font=("Helvetica", 16, "bold"))
header.grid(row=0, columnspan=2, pady=10)

# Create and place the frames
frame1 = tk.Frame(root, bg='#576CA8', width=600, height=500)
frame2 = tk.Canvas(root, bg='#576CA8', width=367, height=500, borderwidth=0, highlightthickness=0)

# Add background image to the canvas
frame2.create_image((185, 250), image=rounded_frame2_bg)

# Create a text container canvas inside frame2
text_container = tk.Canvas(frame2, bg='#274690', width=340, height=460, borderwidth=0, highlightthickness=0)
text_container.place(x=20, y=20)

# Add a scrollbar to the text container
scrollbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=text_container.yview)
scrollbar.place(x=335, y=15, height=470)
text_container.config(yscrollcommand=scrollbar.set)

# Add some initial conversation text
for i in range(20):
    text_adder("User", "Hello David")
    text_adder("David", "Hello sir")


canvas_face_cam = tk.Canvas(frame1, width=600, height=380, borderwidth=0, highlightthickness=0)
canvas_face_cam.create_image((300, 190), image=camera_screen)

canvas_face_cam.pack(anchor="center", pady=50, fill=tk.BOTH)

# Buttons
TurnCameraOn = tk.Button(frame1, text="Start Video", command=start_vid, anchor="center")
TurnCameraOn.place(anchor="center", x=250, y=460)
TurnCameraOff = tk.Button(frame1, text="Stop Video", command=stop_vid, anchor="center")
TurnCameraOff.place(anchor="center", x=350, y=460)

frame1.grid(row=1, column=0, sticky="nsew", padx=(8, 8))
frame2.grid(row=1, column=1, sticky="nsew", padx=(8, 8))

# Run the main loop
root.mainloop()
