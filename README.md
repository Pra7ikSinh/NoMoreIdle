# NoMoreIdle

A powerful Python script designed to prevent your computer from going idle. This script simulates user activity by moving the mouse, scrolling, or pressing keys at set intervals. It is ideal for keeping your system active during extended periods of inactivity.

## Features

- Move the mouse in a diagonal or circular pattern.
- Scroll the mouse wheel.
- Press and release the Shift key.
- Configurable action intervals.
- Randomized intervals to simulate more natural activity.
- Easy command-line configuration.

## Requirements

- Python 3.x
- `pynput` library (install with `pip install pynput`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/anti-idle-script.git
    cd anti-idle-script
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script with the desired options:

```bash
 python main.py [OPTIONS]
```

## Features

- Move the mouse in a diagonal or circular pattern.
- Scroll the mouse wheel.
- Press and release the Shift key.
- Configurable action intervals.
- Randomized intervals to simulate more natural activity.
- Easy command-line configuration.

## Examples

1. Default Usage: Move the mouse diagonally every 60 seconds by 1 pixel.
    ```bash
    python main.py
    ```

2. Custom Interval and Pixels: Move the mouse diagonally every 30 seconds by 5 pixels.
    ```bash
    python main.py -s 30 -p 5
    ```
3. Circular Mouse Movement: Move the mouse in a circular pattern every 45 seconds.
    ```bash
    python main.py -s 30 -p 5
    ```
4. Keyboard Mode: Press and release the Shift key every 60 seconds.
    ```bash
    python main.py -m keyboard
    ```
5. Scroll Mode: Scroll the mouse wheel every 50 seconds.
    ```bash
    python main.py -m scroll -s 50
    ```
6. Random Interval: Move the mouse in a random interval between 30 to 90 seconds.
    ```bash
    python main.py -r 30 90
    ```
7. Use All Features
    ```bash
    python main.py -s 30 -p 5 -c -m both -r 10 60
    ```

## License

This project is licensed under the MIT (Licence)[www.google.com]. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
# 
   For any inquiries or issues, please contact pra7iksinh@gmail.com.

