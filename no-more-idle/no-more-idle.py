import time
import random
from pynput.mouse import Controller as MouseController
from config import parseArguments, config
from actions import executeAction
from utils import getCurrentTimestamp

def main():
    parseArguments()
    mouse = MouseController()
    lastPosition = mouse.position

    try:
        while True:
            currentPosition = mouse.position
            if currentPosition == lastPosition:
                executeAction()
            else:
                print(getCurrentTimestamp(), "User activity detected")
                config['tab_count'] = 1
            lastPosition = currentPosition

            if config["randomMode"]:
                sleepTime = random.randint(config["randomIntervalStart"], config["randomIntervalStop"])
            else:
                sleepTime = config["sleepSeconds"]

            print(getCurrentTimestamp(), f"Sleeping for {sleepTime} seconds")
            time.sleep(sleepTime)
            print("--------")

    except KeyboardInterrupt:
        print("\nExiting. Goodbye!")
        exit()

if __name__ == "__main__":
    main()
