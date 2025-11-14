import time
import random
import math
import pyautogui
import keyboard   # <-- NEW: for instant ESC abort

pyautogui.FAILSAFE = True  # moving mouse to top-left stops immediately

def human_like_mouse_move_top_to_bottom(duration_seconds=0.6, horizontal_jitter=40):
    """
    Fast human-like mouse movement from top to bottom
    with ESC key instant abort.
    """
    screen_width, screen_height = pyautogui.size()

    start_x = screen_width // 2
    start_y = 10
    end_x = screen_width // 2
    end_y = screen_height - 10

    steps = 100   # fewer steps = faster
    step_delay = duration_seconds / steps

    pyautogui.moveTo(start_x, start_y)

    for i in range(steps + 1):

        # 🔴 INSTANT CANCEL SAFETY CHECK
        if keyboard.is_pressed("esc"):
            print("\nABORTED by ESC key!")
            return

        t = i / steps
        eased_t = t * t * (3 - 2 * t)

        current_y = start_y + (end_y - start_y) * eased_t

        curve = math.sin(eased_t * math.pi)
        jitter = random.uniform(-1, 1)

        current_x = start_x + curve * horizontal_jitter + jitter * 2

        pyautogui.moveTo(current_x, current_y)
        time.sleep(step_delay)

if __name__ == "__main__":
    print("Starting fast movement in 1 second...")
    print("Press ESC at ANY time to cancel instantly.")
    print("OR move mouse to TOP-LEFT corner for PyAutoGUI failsafe.")
    time.sleep(1)

    human_like_mouse_move_top_to_bottom(duration_seconds=0.1, horizontal_jitter=60)

    print("Done.")
