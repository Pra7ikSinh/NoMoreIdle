# NoMoreIdle
A powerful Python script designed to prevent your computer from going idle. Simulate user activity by moving the mouse, scrolling, or pressing keys at set intervals. Ideal for keeping your system active during extended periods of inactivity.

Features
Mouse Movement: Move the mouse in a specified pattern (circular or diagonal) to prevent screensaver activation or system sleep.
Keyboard Interaction: Simulate key presses (e.g., Shift key) to keep the system active.
Scrolling Action: Perform mouse scroll actions to simulate activity.
Random Intervals: Choose fixed or random intervals for actions to simulate more natural activity.
Usage
Command Line Arguments
-s, --seconds: Time to wait before acting again (in seconds). Default is 300 seconds.
-p, --pixels: Number of pixels to move the mouse. Default is 1 pixel.
-c, --circular: Move the mouse in a circular pattern.
-m, --mode: Action mode. Options are 'keyboard', 'mouse', 'both', or 'scroll'. Default is 'mouse'.
-r, --random: Specify a random interval range in seconds (start stop).
Example Command
sh
Copy code
python main.py --seconds 300 --pixels 10 --circular --mode both --random 10 20
Example Configurations
Fixed Interval Mouse Movement:

sh
Copy code
python main.py --seconds 300 --pixels 10 --mode mouse
Circular Mouse Movement with Random Intervals:

sh
Copy code
python main.py --circular --random 10 20
Simulate Both Mouse and Keyboard Activity:

sh
Copy code
python main.py --mode both
Installation
Clone the Repository:

sh
Copy code
git clone https://github.com/yourusername/nomoreidle.git
cd nomoreidle
Install Dependencies:

sh
Copy code
pip install -r requirements.txt
Run the Script:

sh
Copy code
python main.py
Project Structure
main.py: The main script that orchestrates user activity simulation.
config.py: Handles configuration and parsing command-line arguments.
actions.py: Contains functions to perform mouse and keyboard actions.
utils.py: Contains utility functions like getting the current timestamp.
Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance the functionality or fix bugs.

License
This project is licensed under the MIT License.

Keywords
NoMoreIdle, Idle Activity Simulator, Prevent Idle State, Mouse Movement, Keyboard Simulation, Screen Saver Prevention, System Sleep Prevention, User Activity Simulation, Python Automation, Random Intervals, Idle State Detection.
