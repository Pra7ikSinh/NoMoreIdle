import argparse
from utils import getCurrentTimestamp

config = {
    "moveMouse": False,
    "scrollAction": False,
    "pressShiftKey": False,
    "randomMode": False,
    "pixelsToMove": 1,
    "mouseMovementPattern": 0, # Diagonal
    "randomIntervalStart": 0,
    "randomIntervalStop": 0,
    "sleepSeconds": 3,
    "mouseDirection": 0,
}

def parseArguments():
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
        config["sleepSeconds"] = args.seconds

    if args.pixels:
        config["pixelsToMove"] = args.pixels

    if args.circular:
        config["mouseMovementPattern"] = 1

    if args.random:
        start, stop = args.random
        if start > stop:
            print("Error: The start of the random interval must be less than the stop.")
            exit()
        config["randomIntervalStart"] = start
        config["randomIntervalStop"] = stop
        config["randomMode"] = True

    mode = args.mode
    if mode == "keyboard":
        config["pressShiftKey"] = True
    elif mode == "mouse":
        config["moveMouse"] = True
    elif mode == "both":
        config["pressShiftKey"] = config["moveMouse"] = True
    elif mode == "scroll":
        config["scrollAction"] = True
    else:
        config["moveMouse"] = True

    printConfiguration()

def printConfiguration():
    """Prints the current configuration."""
    print("--------")
    if config["pressShiftKey"]:
        print(getCurrentTimestamp(), "Keyboard action enabled")
    if config["scrollAction"]:
        print(getCurrentTimestamp(), "Mouse scroll action enabled")
    if config["moveMouse"]:
        movementType = "circularly" if config["mouseMovementPattern"] == 1 else "diagonally"
        print(getCurrentTimestamp(), f"Mouse movement enabled: {config['pixelsToMove']} pixels {movementType}")
    if config["randomMode"]:
        print(getCurrentTimestamp(), f"Random interval enabled: {config['randomIntervalStart']} - {config['randomIntervalStop']} seconds")
    else:
        print(getCurrentTimestamp(), f"Fixed interval: {config['sleepSeconds']} seconds")
    print("--------")
