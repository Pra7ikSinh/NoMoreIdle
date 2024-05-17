from datetime import datetime

def get_current_timestamp():
    """Returns the current time formatted as HH:MM:SS."""
    return datetime.now().strftime("%H:%M:%S")
