import os
import webbrowser
from tkinter import *

def start_stream():
    webbrowser.open("https://webrtc.remoteconsole.victormartin.eu:4000/broadcast.html")
    executable = '.\start-streaming.bat'
    os.system(executable)

#Génération fenetre

window = Tk()

window.title("VI-Agency eRemote FOH. Broadcast System")
window.geometry("720x600")
window.minsize(720, 600)
window.maxsize(720, 600)
window.iconbitmap("./logo-noir.ico")
window.config(background="#252525")

#Frame
frame_titre = Frame(window, bg="#252525")
frame_logo = Frame(window, bg="#252525")

#Logo SAF

logo_safran = PhotoImage(file="./logo-blanc.png").subsample(15)
canvas_logo = Canvas(frame_logo, width=300, height=300, bg="#252525", bd=0, highlightthickness=0)
canvas_logo.create_image(150, 150, image=logo_safran)
canvas_logo.grid(row=0, column=0, sticky=N)

#Main action

label_title = Label(frame_titre, text="eRemote FOH Broadcast System", font=("Helvetica", 25), bg="#252525", fg="white")
label_title.pack()

button_scan = Button(frame_titre,text="Start Application",font=("Helvetica", 15),bg="#AF0404", fg="white", command=start_stream)
button_scan.pack()

#Affichage fenetre

frame_logo.pack()
frame_titre.pack(ipady=20)
window.mainloop()