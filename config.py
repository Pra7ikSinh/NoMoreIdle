import argparse
from utils import get_current_timestamp

config = {
    "move_mouse": False,
    "scroll_action": False,
    "press_shift_key": False,
    "random_mode": False,
    "pixels_to_move": 60,
    "mouse_movement_pattern": 0,
    "rand_interval_start": 0,
    "rand_interval_stop": 0,
    "move_interval_seconds": 3,
    "mouse_direction": 0,
}

def parse_arguments():
    """Parse and handle command line arguments."""
    parser = argparse.ArgumentParser(
        description="Simulates user activity to prevent idle state detection."
    )

    parser.add_argument("-s", "--seconds", type=int, help="Time to wait before acting again (in seconds). Default is 60 seconds.")
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
        config["mouse_movement_pattern"] = 1

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
        movement_type = "circularly" if config["mouse_movement_pattern"] == 1 else "diagonally"
        print(get_current_timestamp(), f"Mouse movement enabled: {config['pixels_to_move']} pixels {movement_type}")
    if config["random_mode"]:
        print(get_current_timestamp(), f"Random interval enabled: {config['rand_interval_start']} - {config['rand_interval_stop']} seconds")
    else:
        print(get_current_timestamp(), f"Fixed interval: {config['move_interval_seconds']} seconds")
    print("--------")
