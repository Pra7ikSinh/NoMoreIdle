#!/usr/bin/env python

import argparse
import time
from datetime import datetime
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import random

# Initialize controllers
mouse = MouseController()
keyboard = KeyboardController()

# Global flags and settings
config = {
    "move_mouse": False,
    "scroll_action": False,
    "press_shift_key": False,
    "random_mode": False,
    "pixels_to_move": 100,
    "mouse_direction_delta": 0,
    "rand_interval_start": 0,
    "rand_interval_stop": 0,
    "move_interval_seconds": 3,
    "mouse_direction": 0,
}


def get_current_timestamp():
    """Returns the current time formatted as HH:MM:SS."""
    return datetime.now().strftime("%H:%M:%S")


def parse_arguments():
    """Parse and handle command line arguments."""
    parser = argparse.ArgumentParser(
        description="Simulates user activity to prevent idle state detection."
    )

    parser.add_argument("-s", "--seconds", type=int, help="Idle threshold in seconds. Default is 300.")
    parser.add_argument("-p", "--pixels", type=int, help="Pixels to move the mouse. Default is 1.")
    parser.add_argument("-c", "--circular", action='store_true', help="Move mouse in a circular pattern.")
    parser.add_argument("-m", "--mode", help="Action mode: 'keyboard', 'mouse', 'both', or 'scroll'. Default is 'mouse'.")
    parser.add_argument("-r", "--random", type=int, nargs=2, help="Random interval range in seconds (start stop).")

    args = parser.parse_args()

    if args.seconds:
        config["move_interval_seconds"] = args.seconds

    if args.pixels:
        config["pixels_to_move"] = args.pixels

    if args.circular:
        config["mouse_direction_delta"] = 1

    if args.random:
        start, stop = args.random
        if start > stop:
            print("Error: The start of the random interval must be less than the stop.")
            exit()
        config["rand_interval_start"] = start
        config["rand_interval_stop"] = stop
        config["random_mode"] = True

    mode = args.mode
    if mode == "keyboard":
        config["press_shift_key"] = True
    elif mode == "mouse":
        config["move_mouse"] = True
    elif mode == "both":
        config["press_shift_key"] = config["move_mouse"] = True
    elif mode == "scroll":
        config["scroll_action"] = True
    else:
        config["move_mouse"] = True

    print_configuration()


def print_configuration():
    """Prints the current configuration."""
    print("--------")
    if config["press_shift_key"]:
        print(get_current_timestamp(), "Keyboard action enabled")
    if config["scroll_action"]:
        print(get_current_timestamp(), "Mouse scroll action enabled")
    if config["move_mouse"]:
        movement_type = "circularly" if config["mouse_direction_delta"] == 1 else "diagonally"
        print(get_current_timestamp(), f"Mouse movement enabled: {config['pixels_to_move']} pixels {movement_type}")
    if config["random_mode"]:
        print(get_current_timestamp(), f"Random interval enabled: {config['rand_interval_start']} - {config['rand_interval_stop']} seconds")
    else:
        print(get_current_timestamp(), f"Fixed interval: {config['move_interval_seconds']} seconds")
    print("--------")


def move_mouse():
    """Moves the mouse in a specified pattern."""
    delta_x = config["pixels_to_move"] if config["mouse_direction"] in (0, 3) else -config["pixels_to_move"]
    delta_y = config["pixels_to_move"] if config["mouse_direction"] in (0, 1) else -config["pixels_to_move"]

    new_position = (mouse.position[0] + delta_x, mouse.position[1] + delta_y)
    mouse.position = new_position

    config["mouse_direction"] = (config["mouse_direction"] + config["mouse_direction_delta"]) % 4

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


def main():
    parse_arguments()
    last_position = mouse.position

    try:
        while True:
            current_position = mouse.position
            if current_position == last_position:
                execute_action()
            else:
                print(get_current_timestamp(), "User activity detected")
            last_position = current_position

            if config["random_mode"]:
                sleep_time = random.randint(config["rand_interval_start"], config["rand_interval_stop"])
            else:
                sleep_time = config["move_interval_seconds"]

            print(get_current_timestamp(), f"Sleeping for {sleep_time} seconds")
            time.sleep(sleep_time)
            print("--------")

    except KeyboardInterrupt:
        print("\nExiting. Goodbye!")
        exit()


if __name__ == "__main__":
    main()
