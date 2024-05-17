from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from config import config
from utils import get_current_timestamp

# Initialize controllers
mouse = MouseController()
keyboard = KeyboardController()

def move_mouse():
    """Moves the mouse in a specified pattern."""
    delta_x = config["pixels_to_move"] if config["mouse_direction"] in (0, 3) else -config["pixels_to_move"]
    delta_y = config["pixels_to_move"] if config["mouse_direction"] in (0, 1) else -config["pixels_to_move"]

    new_position = (mouse.position[0] + delta_x, mouse.position[1] + delta_y)
    mouse.position = new_position

    config["mouse_direction"] = (config["mouse_direction"] + config["mouse_movement_pattern"]) % 4

    print(get_current_timestamp(), f"Moved mouse to: {mouse.position}")

def perform_scroll():
    """Scrolls the mouse wheel."""
    mouse.scroll(0, -2)
    print(get_current_timestamp(), "Mouse wheel scrolled")

def press_shift():
    """Presses and releases the Shift key."""
    keyboard.press(Key.shift)
    keyboard.release(Key.shift)
    print(get_current_timestamp(), "Shift key pressed")

def execute_action():
    """Executes the configured action to simulate user activity."""
    print(get_current_timestamp(), "Simulating user activity")
    if config["move_mouse"]:
        move_mouse()
    if config["scroll_action"]:
        perform_scroll()
    if config["press_shift_key"]:
        press_shift()
