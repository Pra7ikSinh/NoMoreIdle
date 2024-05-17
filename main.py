import time
import random
from pynput.mouse import Controller as MouseController
from config import parse_arguments, config
from actions import execute_action
from utils import get_current_timestamp

def main():
    parse_arguments()
    mouse = MouseController()
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
