import sys
import time

import pygame
import pyautogui

# Safety: moving mouse to top-left will stop PyAutoGUI actions
pyautogui.FAILSAFE = True

# --- CONFIGURATION ---

# Delay between each key press inside a sequence
KEY_DELAY = 0.03

# Delay between sequences
SEQUENCE_DELAY = 0.1

# Button mapping for PS5 controller (may vary)
BUTTON_X = 1  # If X doesn't trigger, try 0 or 2

# The sequences to execute when X is pressed
SEQUENCES = [
    "WWQRD",
    "WWWRD",
    "EEWRD",
    "QWERD",
    "EEERD",
    "2",
    "WWQRD",
    "WWWRD",
    "EEWRD",
    "EEERD",
    "QWERD"
]

# -----------------------

def press_sequence(seq: str):
    """Press keys in a string one-by-one."""
    print(f"Executing sequence: {seq}")
    for char in seq:
        pyautogui.press(char.lower())
        time.sleep(KEY_DELAY)
    time.sleep(SEQUENCE_DELAY)

def main():
    pygame.init()
    pygame.joystick.init()

    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("No controller detected. Plug in your PS5 controller and try again.")
        sys.exit(1)

    js = pygame.joystick.Joystick(0)
    js.init()

    print(f"Using controller: {js.get_name()}")
    print("Ready!")
    print("- Press X to execute all sequences:")
    for s in SEQUENCES:
        print("  →", s)
    print("- Press Ctrl+C to exit.")
    print("- Move mouse to TOP-LEFT corner for PyAutoGUI fail-safe.")

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    button_index = event.button

                    if button_index == BUTTON_X:
                        print("\nX pressed → running macros...")
                        for seq in SEQUENCES:
                            press_sequence(seq)
                        print("Done.\n")

            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\nExiting.")
    finally:
        pygame.joystick.quit()
        pygame.quit()

if __name__ == "__main__":
    main()
