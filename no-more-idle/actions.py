import time
import random
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from config import config
from utils import getCurrentTimestamp

mouse = MouseController()
keyboard = KeyboardController()

def moveMouse():
    """Moves the mouse in a specified pattern based on the configuration settings."""
    delta_x = config["pixelsToMove"] if config["mouseDirection"] in (0, 3) else -config["pixelsToMove"]
    delta_y = config["pixelsToMove"] if config["mouseDirection"] in (0, 1) else -config["pixelsToMove"]

    newPosition = (mouse.position[0] + delta_x, mouse.position[1] + delta_y)
    mouse.position = newPosition

    config["mouseDirection"] = (config["mouseDirection"] + config["mouseMovementPattern"]) % 4

    print(getCurrentTimestamp(), f"Moved mouse to: {mouse.position}")

def performScroll():
    """Scrolls the mouse wheel."""
    mouse.scroll(0, -2)
    print(getCurrentTimestamp(), "Mouse wheel scrolled")

def pressShift():
    """Presses and releases the Shift key."""
    keyboard.press(Key.shift)
    keyboard.release(Key.shift)
    print(getCurrentTimestamp(), "Shift key pressed")


def changeWindow():
    """Simulates pressing Alt + Tab to change windows."""
    keyboard.press(Key.alt)
    for _ in range(config["tab_count"]):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.1)
    keyboard.release(Key.alt)
    print(getCurrentTimestamp(), f"Alt+Tab pressed {config['tab_count']} time(s) to change windows")
    config["tab_count"] += 1

def moveMouseRandomly():
    """Moves the mouse to a random position within a defined range."""
    screen_width, screen_height = 1920, 1080
    delta_x = random.randint(-50, 50)
    delta_y = random.randint(-50, 50)
    new_x = max(0, min(mouse.position[0] + delta_x, screen_width))
    new_y = max(0, min(mouse.position[1] + delta_y, screen_height))
    mouse.position = (new_x, new_y)
    print(getCurrentTimestamp(), f"Moved mouse randomly to: {mouse.position}")

def performRandomScroll():
    """Scrolls randomly up or down."""
    direction = random.choice([-1, 1])
    mouse.scroll(0, direction * random.randint(1, 5))
    print(getCurrentTimestamp(), f"Mouse wheel scrolled {'up' if direction == -1 else 'down'}")

def executeAction():
    """Executes the configured action to simulate user activity."""
    print(getCurrentTimestamp(), "Simulating user activity")
    if config["moveMouse"]:
        moveMouse()
    if config["scrollAction"]:
        performScroll()
    if config["pressShiftKey"]:
        pressShift()
    if config["changeWindow"]:
        changeWindow()
    if config["randomMouseMove"]:
        moveMouseRandomly()
    if config["randomScroll"]:
        performRandomScroll()

