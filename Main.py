from pynput import keyboard
import os


def function_1():
    print("function_1")
    os.system('python ./App/Gui.py')


def function_2():
    print("function_2")
    os.system('python ./App/Robert.pyw')


with keyboard.GlobalHotKeys({
    "<shift>+<tab>+6": function_1,
        "<shift>+<tab>+7": function_2, }) as h:
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
