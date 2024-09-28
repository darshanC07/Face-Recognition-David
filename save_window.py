import tkinter as tk
import time

def get_name():
    global save_window
    face_name = face_name_entry.get()
    if face_name:
        msg = tk.Label(save_window,text="File saved successfully",fg="black", font=("Helvetica", 10, "bold"))
        msg.place(relx=0.5,y=150, anchor="center")
        save_window.update()
        print(face_name)
        time.sleep(2)
        save_window.destroy()
    
save_window = tk.Tk()
save_window.title("Save Face")
save_window.geometry("300x170")
save_window.resizable(False,False)
label_save = tk.Label(save_window,text="Enter the Face name", fg="black", font=("Helvetica", 16, "bold"))
label_save.place(relx=0.5,y=25, anchor="center")
        
face_name_entry = tk.Entry(save_window, width=40,borderwidth=2,background="#D3D3D3",font=("Helvetica", 10, "bold"))
face_name_entry.place(relx=0.5,y=63, anchor="center")
        
submit_name = tk.Button(save_window, text="Save",width=15, height=2, background="#D3D3D3", font=("Helvetica", 10, "bold"),command=get_name)
submit_name.place(relx=0.5,y=110, anchor="center")

save_window.mainloop()
# print(get_name())