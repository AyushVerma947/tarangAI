from cProfile import label
import tkinter as tk
from turtle import left, right
import csv_Play
def about():
    l1=tk.Label(label,text="this is TarangAI").pack()
def band():
    def dropd():
        csv_Play.inn(var.get())
    label.destroy()
    label = tk.Label(main_frame)
    label.pack(side="left")
    label.configure(bg="#ffb6c1",width=400,height=600)

    new_windoe = tk.Button(label, text="Play selected band" , command=dropd)    
    new_windoe.grid()
    l = tk.Label(label, text="Play the bands by selecting them from the dropdown list", anchor="nw", borderwidth=3, relief=SUNKEN)
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
    o = tk.OptionMenu(label, var, *opt)
    o.grid(row=2, column=0)

# Create the main window
root = tk.Tk()
root.geometry("7733x4463")
root.title("Two Frames Example")

# Create frames
option_frame = tk.Frame(root)
option_frame.pack(side="left", padx=10, pady=10)
option_frame.configure(bg="#0000FF",width=100,height=600)

main_frame = tk.Frame(root)
main_frame.pack(side="left", padx=10, pady=10)


# Code for the contents of the option frame
labe = tk.Label(option_frame, text="Option Frame Content")
labe.pack(side="left")
labe.configure(bg="#0000FF",width=100,height=600)


    

bt1_home=tk.Button(labe,text="ABOUT",command=about)
bt1_home.pack()

bt2=tk.Button(labe,text="play bands",command=band)
bt2.pack()



# Code for the contents of the main frame
label = tk.Label(main_frame, text="Main Frame Content")
label.pack(side="left")
label.configure(bg="#ffb6c1",width=400,height=600)

    





# Add content to framesmain_frame_content()

# Start the main loop
root.mainloop()
