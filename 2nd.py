import tkinter as tk
import csv_Play
from tkinter import filedialog
import la
import convo_
import getfreq
import consec

root=tk.Tk()
root.geometry("7500x6400")
#root.attributes("-fullscreen", True)
def deleteframes():
    for frame in main_frame.winfo_children():
        frame.destroy()
##############
def mi():
    deleteframes()
    l2 = tk.Label(main_frame, text="Mixing")
    l2.grid(row=0, column=2,pady=15)    
    
    
    def mix():
       la.mix(fl1.cget("text"),fl2.cget("text"))
    def open(fl):
        # e=Entry(top,text="Enter no. of files to be selected for convolution")
        file_path = filedialog.askopenfilename(initialdir="Downloads", title="Select a file", filetypes=(
        ("MP3 files", "*.mp3"), ("WAV files", "*.wav"), ("All files", "*.*")))
        if file_path:
              #Self.text="{}",file_path
              fl.config(text="" + file_path)

    fl1 = tk.Label(main_frame, text="")
    fl2 = tk.Label(main_frame, text="")

    bt1 = tk.Button(main_frame, text="Select File 1", command=lambda: open(fl1))
    bt1.grid(row=1, column=0,padx=60)
    bt2 = tk.Button(main_frame, text="Select File 2", command=lambda: open(fl2))
    bt2.grid(row=1, column=1,padx=60)
    # 
    bt4 = tk.Button(main_frame, text="play mixed signal", command=mix)  
    bt4.grid(row=1, column=4,padx=60)

    
    
    

####################
def con():
    deleteframes()
    l2 = tk.Label(main_frame, text="Convolution")
    l2.grid(row=0, column=2,pady=15)
       

    def pcon():
        convo_.con(getfreq.get_audio_frequency(fl1.cget("text")), getfreq.get_audio_frequency(fl2.cget("text")))

    def open(fl):
        # e=Entry(top,text="Enter no. of files to be selected for convolution")
        file_path = filedialog.askopenfilename(initialdir="Downloads", title="Select a file", filetypes=(
        ("MP3 files", "*.mp3"), ("WAV files", "*.wav"), ("All files", "*.*")))
        if file_path:
              #Self.text="{}",file_path
              fl.config(text="" + file_path)

    fl1 = tk.Label(main_frame, text="")
    fl2 = tk.Label(main_frame, text="")

    bt1 = tk.Button(main_frame, text="Select File 1", command=lambda: open(fl1))
    bt1.grid(row=1, column=0,padx=60)
    bt2 = tk.Button(main_frame, text="Select File 2", command=lambda: open(fl2))
    bt2.grid(row=1, column=1,padx=60)
    # 
    bt3 = tk.Button(main_frame, text="play convolved signal", command=pcon)  
    bt3.grid(row=1, column=3,padx=60)

###################
def band():
    deleteframes()
    def conse():
        consec.play(var.get())
    def dropd():
        csv_Play.inn(var.get())
    

    new_windoe = tk.Button(main_frame, text="Play selected band" , command=dropd)    
    
    l = tk.Label(main_frame, text="Play the bands by selecting them from the dropdown list", anchor="nw", borderwidth=3)
    l.grid(row=1, column=0, padx=90, pady=3)
    opt = [
        "A_band",
        "B_band",
        "C_band",
        "D_band",
        "E_band",
        "F_band"
    ]

    var = tk.StringVar()
    var.set(opt[0])
    o = tk.OptionMenu(main_frame, var, *opt)
    o.grid(row=2, column=0)
    new_windoe.grid(row=2, column=1)
    consecutive = tk.Button(main_frame, text="Play consecutive" ,command=conse)
    consecutive.grid(row=3, column=0)    
    succes = tk.Button(main_frame, text="Play Successive" )
    succes.grid(row=3, column=1) 
    ra = tk.Button(main_frame, text="Play Random" )
    ra.grid(row=3, column=2)    



#option frame
Option_frame=tk.Frame(root,bg="#ADD8E6")
home_btn=tk.Button(Option_frame,text="ABOUT",fg="#158aff")

home_btn.place(x=10,y=50)

playband=tk.Button(Option_frame,text="Play bands",fg="#158aff",command=band)
playband.place(x=10,y=100)

convobtn=tk.Button(Option_frame,text="Convolution",fg="#158aff",command=con)
convobtn.place(x=10,y=150)

mix=tk.Button(Option_frame,text="Mixing",fg="#158aff",command=mi)
mix.place(x=10,y=200)
Option_frame.pack(side=tk.LEFT)
Option_frame.pack_propagate(False)
Option_frame.configure(width=100,height=400)


#main frame
main_frame=tk.Frame(root,bg="#ffb6c1")
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=400,height=400)
root.mainloop()

