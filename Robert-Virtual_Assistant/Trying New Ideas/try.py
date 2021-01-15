# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x400")
# root.mainloop()


import tkinter as tk


def move(steps=10, distance=0.1):
    if steps > 0:
        # get current position
        relx = float(frame.place_info()['relx'])
        # set new position
        frame.place_configure(relx=relx+distance)
        # repeate it after 10ms
        root.after(10, move, steps-1, distance)


def toggle(event):
    if button["text"] == "Yes":
        move(25, 0.02)  # 50*0.02 = 1
        button["text"] = "No"
        print("Clicked on yes")
    elif button["text"] == "No":
        move(25, -0.02)
        button["text"] = "Yes"
        print("Clicked on no")


# --- main --
root = tk.Tk()
frame = tk.Frame(root, background='red')
frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)
button = tk.Button(frame, text='Yes', width=5, height=1, radius=2)
button.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.1)
button.bind("<Button-1>", toggle)
root.mainloop()
