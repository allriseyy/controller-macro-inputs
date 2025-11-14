import time
import random
import pyautogui
import keyboard

# Safety: moving mouse to top-left corner raises a PyAutoGUI fail-safe exception
pyautogui.FAILSAFE = True

def flick_around_one_third(center_fraction_x=1/3, center_fraction_y=1/3,
                           radius=80, move_duration=0.02, interval=0.05):
    """
    Repeatedly flicks the mouse around a point that is at (1/3, 1/3) of the screen
    (from top-left), moving up/down/left/right and right-clicking every time.

    Press ESC to stop instantly.
    Move mouse to TOP-LEFT corner for PyAutoGUI fail-safe.
    """

    screen_width, screen_height = pyautogui.size()

    # Center point at one third of the screen
    center_x = int(screen_width * center_fraction_x)
    center_y = int(screen_height * center_fraction_y)

    print("Mouse flicker starting...")
    print("Center point:", center_x, center_y)
    print("Press ESC to stop, or move mouse to TOP-LEFT corner for fail-safe.")

    # Directions: up, down, left, right
    directions = [
        (0, -1),  # up
        (0, 1),   # down
        (-1, 0),  # left
        (1, 0),   # right
    ]

    while True:
        # Instant cancel with ESC
        if keyboard.is_pressed("esc"):
            print("\nStopped by ESC key.")
            break

        # Pick a random direction
        dx_dir, dy_dir = random.choice(directions)

        # Pick a random distance within the radius
        distance = random.randint(radius // 2, radius)

        target_x = center_x + dx_dir * distance
        target_y = center_y + dy_dir * distance

        # Make sure we stay on screen
        target_x = max(0, min(screen_width - 1, target_x))
        target_y = max(0, min(screen_height - 1, target_y))

        # Quick flick to target position
        pyautogui.moveTo(target_x, target_y, duration=move_duration)

        # Right-click at that position
        pyautogui.click(button="right")

        # Small pause before next flick
        time.sleep(interval)

if __name__ == "__main__":
    print("Starting in 2 seconds... Put your hand near ESC just in case.")
    time.sleep(2)
    try:
        flick_around_one_third(
            center_fraction_x=1/3,
            center_fraction_y=1/3,
            radius=80,          # how far from the center
            move_duration=0.02, # how fast each flick is
            interval=0.05       # time between flicks
        )
    except pyautogui.FailSafeException:
        print("\nPyAutoGUI fail-safe triggered (mouse went to top-left). Stopped safely.")
