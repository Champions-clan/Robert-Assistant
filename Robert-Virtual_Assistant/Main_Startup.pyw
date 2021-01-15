from pynput.keyboard import Key, KeyCode, Listener
from pynput import keyboard
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
import os
import sys


with sqlite3.connect("./DataBase/database.db", check_same_thread=False) as db:
    cur = db.cursor()

user_settings = []


def fetching():
    cur.execute("SELECT * FROM UserSettings")
    fetch = cur.fetchall()
    user_settings.clear()
    for i in fetch[0]:
        user_settings.append(i)


fetching()


def Settings_Gui():
    global root
    global button1

    def buttons_save_function():
        if entry1.get() != user_settings[0]:
            cur.execute("Update UserSettings set SettingsHotkey=? where SettingsHotkey=?", [
                        entry1.get(), user_settings[0]])
            db.commit()
            print("Done")
        if entry2.get() != user_settings[2]:
            cur.execute("Update UserSettings set KeyboardHotkey=? where KeyboardHotkey=?", [
                        entry2.get(), user_settings[2]])
            db.commit()
            print("Done")
        if entry3.get() != user_settings[4]:
            cur.execute("Update UserSettings set CustomSoundLocation=? where CustomSoundLocation=?", [
                        entry3.get(), user_settings[4]])
            db.commit()
            print("Done")
        if combo1.get() != user_settings[1]:
            cur.execute("Update UserSettings set InputVia=? where InputVia=?", [
                        combo1.get(), user_settings[1]])
            db.commit()
            print("Done")
        if combo2.get() != user_settings[3]:
            cur.execute("Update UserSettings set ReminderAlert=? where ReminderAlert=?", [
                        combo2.get(), user_settings[3]])
            db.commit()
            print("Done")
        os.execv(sys.executable, ['python']+['./Main_Startup.pyw'])

    def function_click_on_entry(key):
        list_in_function_click_on_entry = []
        if key.char != '\x08':
            list_in_function_click_on_entry.append(key.keysym)
            print(list_in_function_click_on_entry)
            entry1.insert(
                END, str(list_in_function_click_on_entry[0]).split('\n')[0])
            list_in_function_click_on_entry.clear()

    root = tk.Tk()
    root.geometry("400x400")
    root.resizable(0, 0)

    theme_list = []

    if user_settings[-1] == "Dark":
        theme_list.append("./Assets/Dark Theme.png")
        theme_list.append("./Assets/theme_button_dark.png")
        theme_list.append("#36393F")
        theme_list.append("./Assets/save_button_dark.png")
    else:
        theme_list.append("./assets/Light Theme.png")
        theme_list.append("./Assets/theme_button_light.png")
        theme_list.append("#B0EACD")
        theme_list.append("./Assets/save_button_light.png")

    background_image = Label(root)
    background_image.place(relx=0, rely=0, width=400, height=400)
    img = PhotoImage(file=theme_list[0])
    background_image.configure(image=img)

    button1 = Button(root, borderwidth="0", cursor="hand2")
    button1.place(x=308, y=34, height=25, width=49)
    img2 = PhotoImage(file=theme_list[1])
    button1.configure(image=img2)
    button1.configure(command=lambda: theme_button_function())

    combostyle = ttk.Style()
    combostyle.theme_create('combostyle',
                            settings={'TCombobox':
                                      {'configure':
                                       {'selectbackground': theme_list[2],
                                        'fieldbackground': theme_list[2],
                                        'background': theme_list[2],
                                        'relief': 'flat',
                                        'borderwidth': 0,
                                        'foreground': "White",
                                        }}})
    combostyle.theme_use('combostyle')
    root.option_add("*TCombobox*Listbox*Background", theme_list[2])

    entry1 = Entry(root, bg=theme_list[2], relief="flat",
                   width=15, fg="white", font=("Montserrat", 10, "bold"), justify='center')
    entry2 = Entry(root, bg=theme_list[2], relief="flat",
                   width=15, fg="white", font=("Montserrat", 10, "bold"), justify='center')
    entry3 = Entry(root, bg=theme_list[2], relief="flat",
                   width=15, fg="white", font=("Montserrat", 10, "bold"), justify='center')
    combo1 = ttk.Combobox(root, values=["Voice", "Keyborad"], width=13,
                          justify='center', state='readonly', font=("Montserrat", 10, "bold"))
    combo2 = ttk.Combobox(root, values=["Sound", "Notification"], width=13,
                          justify='center', state='readonly', font=("Montserrat", 10, "bold"))

    button_save = Button(root, command=lambda: buttons_save_function(
    ), bg=theme_list[2], activebackground=theme_list[2], relief="flat", overrelief="flat", fg="white", borderwidth="0", cursor="hand2")

    img3 = PhotoImage(file=theme_list[-1])
    button_save.configure(image=img3)

    entry1.place(x=249, y=129)
    entry2.place(x=249, y=209)
    entry3.place(x=249, y=295)
    combo1.place(x=250, y=169)
    combo2.place(x=250, y=251)
    button_save.place(x=142, y=336, height=38, width=119)

    entry1.insert(0, user_settings[0])
    entry2.insert(0, user_settings[2])
    entry3.insert(0, user_settings[4])

    entry1.bind("<1>", lambda x: entry1.delete(0, "end"))
    entry1.bind("<Key>", function_click_on_entry)

    if user_settings[1] == "Voice":
        combo1.current(0)
    else:
        combo1.current(1)
    if user_settings[3] == "Sound":
        combo2.current(0)
    else:
        combo2.current(1)

    root.mainloop()


def function_2():
    print('Function 2 activated')


def theme_button_function():
    if user_settings[-1] == "Dark":
        cur.execute(
            "Update UserSettings set ThemeMode='Light' where ThemeMode = 'Dark'")
        db.commit()
        root.destroy()
        fetching()
        Settings_Gui()
    else:
        cur.execute(
            "Update UserSettings set ThemeMode='Dark' where ThemeMode = 'Light'")
        db.commit()
        root.destroy()
        fetching()
        Settings_Gui()


with keyboard.GlobalHotKeys({
        user_settings[0]: Settings_Gui,
        user_settings[2]: function_2}) as h:
    h.join()


def on_press(key):
    try:
        return f"Alphanumreic key {key.char} pressed"
    except AttributeError:
        return f"Special key {key} pressed"


def on_release(key):
    print(f"{key} released")
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()