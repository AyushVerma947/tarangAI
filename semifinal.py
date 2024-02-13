from cProfile import label
import glob
from optparse import Option
import tkinter as tk
import csv_Play
from tkinter import filedialog, Toplevel
import la
import convo_
import getfreq
import consec
import mixing
import M_random
import succesive
import mix_random
import band_mix
import getlist2
import mix_fr
import play_notes
import heal as he

root = tk.Tk()
root.geometry("7500x6400")



def deleteframes():
    for frame in main_frame.winfo_children():
        frame.destroy()


##############
def no():
    def p():
        play_notes.play_music(e.get())
    deleteframes()
    e=tk.Entry(main_frame,text="hello")
    e.grid(row=0,column=0)
    e.insert(0,"enter notes")
    bt1 = tk.Button(main_frame, text="PLay", command=p)
    bt1.grid(row=1, column=0, padx=60)

def mi():
    deleteframes()
    l2 = tk.Label(main_frame, text="Mixing")
    l2.grid(row=0, column=2, pady=15)

    def mix():
        # mi()
        mixing.mix(fl1.cget("text"), fl2.cget("text"))

    def open(fl):
        # e=Entry(top,text="Enter no. of files to be selected for convolution")
        file_path = filedialog.askopenfilename(initialdir="Downloads", title="Select a file", filetypes=(
            ("WAV files", "*.wav"), ("MP3 files", "*.mp3"), ("All files", "*.*")))
        if file_path:
            # Self.text="{}",file_path
            fl.config(text="" + file_path)

    fl1 = tk.Label(main_frame, text="")
    fl2 = tk.Label(main_frame, text="")

    ##
    def up1():
        global n1,var2
        opt2 = getlist2.s(var.get())
        n1.destroy()
        var2 = tk.StringVar()
        var2.set("select")
       
        n1 = tk.OptionMenu(main_frame, var2, *opt2)
        
        n1.grid(row=6, column=0)
    def up2():
        global n2,var3
        opt3 = getlist2.s(var1.get())
        n2.destroy()
        var3 = tk.StringVar()
        var3.set("select")
        
        n2 = tk.OptionMenu(main_frame, var3, *opt3)
        n2.grid(row=6, column=1)
    def up(n1,n2):
       up1()
       up2()
    def mbf():
        global var2,var3
        mix_fr.play_mixed_audio(var2.get(),var3.get())

    bt1 = tk.Button(main_frame, text="Select File 1", command=lambda: open(fl1))
    bt1.grid(row=1, column=0, padx=60)
    bt2 = tk.Button(main_frame, text="Select File 2", command=lambda: open(fl2))
    bt2.grid(row=1, column=1, padx=60)
    #
    bt4 = tk.Button(main_frame, text="play mixed signal", command=mix)
    bt4.grid(row=1, column=4, padx=60)
    #
    bt5 = tk.Button(main_frame,text="mix randomly",command=band_mix.r)
    bt5.grid(row=2,column=1,padx=60)
    bt6 = tk.Button(main_frame,text="get frequency",command= lambda:up(n1,n2))
    bt6.grid(row=5,column=1,padx=60)
    bt7 = tk.Button(main_frame,text="mix selected frequency",command= mbf)
    bt7.grid(row=7,column=0,padx=60)
    ##
    

    l = tk.Label(main_frame, text="mix the band freq by selecting them from the dropdown list", anchor="nw", borderwidth=3)
    l.grid(row=3, column=0, padx=90, pady=3)
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
    o.grid(row=4, column=0)
    #up1()
    opt2 = getlist2.s(var.get())
    global var2
    var2 = tk.StringVar()
    var2.set("select")
    global n1
    n1= tk.OptionMenu(main_frame, var2, *opt2)
    n1.grid(row=6, column=0)
    
###############################
    #l = tk.Label(main_frame, text="Play the bands by selecting them from the dropdown list", anchor="nw", borderwidth=3)
    #l.grid(row=1, column=0, padx=90, pady=3)
    opt1 = [
        "A_band",
        "B_band",
        "C_band",
        "D_band",
        "E_band",
        "F_band"
    ]

    var1 = tk.StringVar()
    var1.set((opt1[0]))
    o2 = tk.OptionMenu(main_frame, var1, *opt1)
    o2.grid(row=4, column=1)
##
    #up2()
    opt3 = getlist2.s(var1.get())
    global var3
    var3 = tk.StringVar()
    var3.set("select")
    global n2
    n2 = tk.OptionMenu(main_frame, var3, *opt3)
    n2.grid(row=6, column=1)
####################
def con():
    deleteframes()
    l2 = tk.Label(main_frame, text="Convolution")
    l2.grid(row=0, column=2, pady=15)

    def pcon():
        convo_.con(getfreq.get_audio_frequency(fl1.cget("text")), getfreq.get_audio_frequency(fl2.cget("text")))

    def open(fl):
        # e=Entry(top,text="Enter no. of files to be selected for convolution")
        file_path = filedialog.askopenfilename(initialdir="Downloads", title="Select a file", filetypes=(
          ("WAV files", "*.wav"),("MP3 files", "*.mp3"),  ("All files", "*.*")))
        if file_path:
            # Self.text="{}",file_path
            fl.config(text="" + file_path)

    fl1 = tk.Label(main_frame, text="")
    fl2 = tk.Label(main_frame, text="")

    bt1 = tk.Button(main_frame, text="Select File 1", command=lambda: open(fl1))
    bt1.grid(row=1, column=0, padx=60)
    bt2 = tk.Button(main_frame, text="Select File 2", command=lambda: open(fl2))
    bt2.grid(row=1, column=1, padx=60)
    # 
    bt3 = tk.Button(main_frame, text="play convolved signal", command=pcon)
    bt3.grid(row=1, column=3, padx=60)

#################
def healing():
    deleteframes()

    # def randomsound():
    #     M_random.play(var.get())

    # def conse():
    #     consec.play(var.get())

    # def s():
    #     succesive.successive(var.get())

    def h():
        t=int(get_key_from_value(frequencies_info,(var.get())))
        he.play_frequency(t,6)
        # he.play_frequency()

    def get_key_from_value(dictionary, target_value):
        for key, value in dictionary.items():
            if value == target_value:
                return key
        return None  
    new_windoe = tk.Button(main_frame, text="Play", command=h)

    l = tk.Label(main_frame, text="select healing frequency", anchor="nw", borderwidth=3)
    l.grid(row=1, column=0, padx=90, pady=3)


    frequencies_info = {
            "174": "Pain Reduction, Healing",
            "285": "Energy Fields, Healing",
            "396": "Emotional Healing, Liberation from Fear",
            "528": "DNA Repair, Overall Healing",
            "639": "Relationships, Interpersonal Connection",
            "741": "Problem-Solving, Intuitive Thinking",
            "852": "Awakens Intuition, Spiritual Development",
            "963": "Spiritual Connections, Oneness with the Universe"
        }

    frequencies = list(frequencies_info.keys())



    # opt = [
    #     417,
    #     528,
    #     639,
    #     741,
    #     852,
    #     963,
    # ]
    opt =list(frequencies_info.values())
    var = tk.StringVar()
    var.set(opt[0])
    o = tk.OptionMenu(main_frame, var, *opt)
    o.grid(row=2, column=0)
    new_windoe.grid(row=2, column=1)
    # consecutive = tk.Button(main_frame, text="Play consecutive", command=conse, padx=15, pady=10)
    # consecutive.grid(row=3, column=0)
    # succes = tk.Button(main_frame, text="Play Successive", padx=15, pady=10,command=s)
    # succes.grid(row=3, column=1)
    # ra = tk.Button(main_frame, text="Play Random", padx=15, pady=10,command=randomsound)
    # ra.grid(row=3, column=2)


Option_frame = tk.Frame(root, bg="#ADD8E6", relief="sunken", borderwidth=2)

###################
def band():
    deleteframes()

    def randomsound():
        M_random.play(var.get())

    def conse():
        consec.play(var.get())

    def s():
        succesive.successive(var.get())

    def dropd():
        csv_Play.inn(var.get())

    new_windoe = tk.Button(main_frame, text="Play selected band", command=dropd)

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
    consecutive = tk.Button(main_frame, text="Play consecutive", command=conse, padx=15, pady=10)
    consecutive.grid(row=3, column=0)
    succes = tk.Button(main_frame, text="Play Successive", padx=15, pady=10,command=s)
    succes.grid(row=3, column=1)
    ra = tk.Button(main_frame, text="Play Random", padx=15, pady=10,command=randomsound)
    ra.grid(row=3, column=2)


Option_frame = tk.Frame(root, bg="#ADD8E6", relief="sunken", borderwidth=2)


def about():
    deleteframes()
    tk.Frame(root, bg="#ffb6c1", relief="sunken", borderwidth=2)
    ti=tk.Label(main_frame,text="Tarang AI: AI Based Music Generator\n",fg="red",bg="#ffb6c1",font=80)
    la=tk.Label(main_frame,text="These are following  functions you can do with it:\n\n1.play bands: you can play band(consecutive, succesive, random order)\n2.convolution: you can input two files anf play the concolved signal\n3.Mixing: we have given may options for mixing such as  from file, from bands, and also random mixing\n4.PLay note: you can input notes of any song of music and it will be played \n\n\n THANK YOU!",font=56,fg="purple",bg="#ffb6c1")
    ti.configure(font=("times",50))
    ti.grid(row=0,column=1,sticky="NW",columnspan=2,padx=80)
    la.grid(row=1,column=1,padx=150)
    #main_frame.label.text         


home_btn = tk.Button(Option_frame, text="ABOUT", fg="#158aff", padx=20, pady=10, command=about)

home_btn.place(x=10, y=50)
home_btn.pack(pady=20)

#aboutus= Label(text="")

playband = tk.Button(Option_frame, text="Play bands", fg="#158aff", padx=20, pady=10, command=band)
playband.place(x=10, y=100)
playband.pack(pady=20)

convobtn = tk.Button(Option_frame, text="Convolution", fg="#158aff", command=con, padx=20, pady=10)
convobtn.place(x=10, y=150)
convobtn.pack(pady=20)

mix = tk.Button(Option_frame, text="Mixing", fg="#158aff", command=mi, padx=20, pady=10)
mix.place(x=10, y=200)
mix.pack(pady=20)

note = tk.Button(Option_frame, text="Play Notes", fg="#158aff", command=no , padx=20, pady=10)
note.place(x=10, y=200)
note.pack(pady=20)

heal = tk.Button(Option_frame, text="heal yourself", fg="#158aff", padx=20, pady=10, command=healing)
heal.place(x=10, y=100)
heal.pack(pady=20)

Option_frame.pack_propagate(False)
Option_frame.configure(width=150, height=400)
Option_frame.pack(side="left", fill="y")

main_frame = tk.Frame(root, bg="#ffb6c1", relief="sunken", borderwidth=2)
main_frame.pack_propagate(False)
main_frame.configure(width=400, height=400)
main_frame.pack(side="left", fill="both", expand=True)
about()
#
# main_frame.pack_propagate(False)
# main_frame.configure(width=400, height=400)
# main_frame.pack(side="top",fill="y")

root.mainloop()