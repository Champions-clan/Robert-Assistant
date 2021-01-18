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

print(user_settings)


def Settings_Gui():
    global root
    global button1

    def buttons_save_function():
        if entry1['text'] != user_settings[0]:
            cur.execute("Update UserSettings set SettingsHotkey=? where SettingsHotkey=?", [
                        entry1['text'], user_settings[0]])
            db.commit()
            print("Done")
        elif entry2['text'] != user_settings[2]:
            cur.execute("Update UserSettings set KeyboardHotkey=? where KeyboardHotkey=?", [
                        entry2['text'], user_settings[2]])
            db.commit()
            print("Done")
        elif entry3.get() != user_settings[4]:
            cur.execute("Update UserSettings set CustomSoundLocation=? where CustomSoundLocation=?", [
                        entry3.get(), user_settings[4]])
            db.commit()
            print("Done")
        elif entry4['text'] != user_settings[-1]:
            cur.execute("Update UserSettings set CodeBaseHotkey=? where CodeBaseHotkey=?", [
                        entry4['text'], user_settings[-1]])
            db.commit()
            print("Done")
        elif combo1.get() != user_settings[1]:
            cur.execute("Update UserSettings set InputVia=? where InputVia=?", [
                        combo1.get(), user_settings[1]])
            db.commit()
            print("Done")
        elif combo2.get() != user_settings[3]:
            cur.execute("Update UserSettings set ReminderAlert=? where ReminderAlert=?", [
                        combo2.get(), user_settings[3]])
            db.commit()
            print("Done")
        else:
            print("Error in saving data")
        os.execv(sys.executable, ['python']+['./Main_Startup.pyw'])

    def function_click_on_entry_1():
        list_in_function_click_on_entry = []

        def on_press_click_on_entry(key):
            if len(list_in_function_click_on_entry) < 3:
                list_in_function_click_on_entry.append(str(key))
                print(key)
            else:
                listener_function_click_on_entry_1.stop()

        with Listener(on_press=on_press_click_on_entry) as listener_function_click_on_entry_1:
            listener_function_click_on_entry_1.join()

        string_var = ""
        string_var = string_var + list_in_function_click_on_entry[0]
        list_in_function_click_on_entry.pop(0)
        print(list_in_function_click_on_entry)
        for i in list_in_function_click_on_entry:
            if i == "Key.alt_l" or i == "Key.alt_gr":
                string_var = string_var + "+" + "<alt>"
            elif i == "Key.ctrl_l" or i == "Key.ctrl_r":
                string_var = string_var + "+" + "<ctrl>"
            elif i == "Key.shift" or i == "Key.shift_r":
                string_var = string_var + "+" + "<shift>"
            else:
                string_var = string_var + "+" + i
            print(string_var)
        textvar_entry1.set(string_var)

    def function_click_on_entry_2():
        list_in_function_click_on_entry = []

        def on_press_click_on_entry(key):
            if len(list_in_function_click_on_entry) < 3:
                list_in_function_click_on_entry.append(str(key))
                print(key)
            else:
                listener_function_click_on_entry_2.stop()

        with Listener(on_press=on_press_click_on_entry) as listener_function_click_on_entry_2:
            listener_function_click_on_entry_2.join()

        string_var = ""
        string_var = string_var + list_in_function_click_on_entry[0]
        list_in_function_click_on_entry.pop(0)
        for i in list_in_function_click_on_entry:
            if i == "Key.alt_l" or i == "Key.alt_gr":
                string_var = string_var + "+" + "<alt>"
            elif i == "Key.ctrl_l" or i == "Key.ctrl_r":
                string_var = string_var + "+" + "<ctrl>"
            elif i == "Key.shift" or i == "Key.shift_r":
                string_var = string_var + "+" + "<shift>"
            else:
                string_var = string_var + "+" + i
            print(string_var)
        textvar_entry2.set(string_var)

    def function_click_on_entry_4():
        list_in_function_click_on_entry = []

        def on_press_click_on_entry(key):
            if len(list_in_function_click_on_entry) < 3:
                list_in_function_click_on_entry.append(str(key))
                print(key)
            else:
                listener_function_click_on_entry_4.stop()

        with Listener(on_press=on_press_click_on_entry) as listener_function_click_on_entry_4:
            listener_function_click_on_entry_4.join()

        string_var = ""
        string_var = string_var + list_in_function_click_on_entry[0]
        list_in_function_click_on_entry.pop(0)
        print(list_in_function_click_on_entry)
        for i in list_in_function_click_on_entry:
            if i == "Key.alt_l" or i == "Key.alt_gr":
                string_var = string_var + "+" + "<alt>"
            elif i == "Key.ctrl_l" or i == "Key.ctrl_r":
                string_var = string_var + "+" + "<ctrl>"
            elif i == "Key.shift" or i == "Key.shift_r":
                string_var = string_var + "+" + "<shift>"
            else:
                string_var = string_var + "+" + i
        textvar_entry4.set(string_var)

    root = tk.Tk()
    root.geometry("400x400")
    root.resizable(0, 0)

    theme_list = []

    if user_settings[5] == "Dark":
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
    button1.place(x=308, y=30, height=25, width=49)
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

    textvar_entry1 = tk.StringVar()
    textvar_entry2 = tk.StringVar()
    textvar_entry3 = tk.StringVar()
    textvar_entry4 = tk.StringVar()

    entry1 = Button(root, textvariable=textvar_entry1, command=lambda: function_click_on_entry_1(), font=("Montserrat", 10, "bold"),
                    width=13, bg=theme_list[2], activebackground=theme_list[2], relief="flat", overrelief="flat", fg="white", borderwidth="0", cursor="hand2")

    entry2 = Button(root, textvariable=textvar_entry2, command=lambda: function_click_on_entry_2(), font=("Montserrat", 10, "bold"),
                    width=13, bg=theme_list[2], activebackground=theme_list[2], relief="flat", overrelief="flat", fg="white", borderwidth="0", cursor="hand2")

    entry3 = Entry(root, textvariable=textvar_entry3, font=("Montserrat", 10, "bold"),
                   width=16, bg=theme_list[2], relief="flat", fg="white", borderwidth="0")

    entry4 = Button(root, textvariable=textvar_entry4, command=lambda: function_click_on_entry_4(), font=("Montserrat", 10, "bold"),
                    width=13, bg=theme_list[2], activebackground=theme_list[2], relief="flat", overrelief="flat", fg="white", borderwidth="0", cursor="hand2")

    combo1 = ttk.Combobox(root, values=["Voice", "Keyborad"], width=14,
                          justify='center', state='readonly', font=("Montserrat", 10, "bold"))
    combo2 = ttk.Combobox(root, values=["Sound", "Notification"], width=14,
                          justify='center', state='readonly', font=("Montserrat", 10, "bold"))

    button_save = Button(root, command=lambda: buttons_save_function(
    ), bg=theme_list[2], activebackground=theme_list[2], relief="flat", overrelief="flat", fg="white", borderwidth="0", cursor="hand2")

    img3 = PhotoImage(file=theme_list[-1])
    button_save.configure(image=img3)

    entry1.place(x=251, y=90)
    entry2.place(x=251, y=175)
    entry3.place(x=251, y=300)
    entry4.place(x=251, y=215)
    combo1.place(x=250, y=136)
    combo2.place(x=250, y=263)
    button_save.place(x=142, y=336, height=38, width=119)

    textvar_entry1.set(user_settings[0])
    textvar_entry2.set(user_settings[2])
    textvar_entry3.set(user_settings[4])
    textvar_entry4.set(user_settings[-1])

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


def code_base_gui():
    print("Function 3 activated")


def theme_button_function():
    if user_settings[5] == "Dark":
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
        user_settings[2]: function_2,
        user_settings[-1]: code_base_gui}) as h:
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
