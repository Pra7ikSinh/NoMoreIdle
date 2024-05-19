from datetime import datetime

def getCurrentTimestamp():
    """Returns the current time formatted as HH:MM:SS."""
    return datetime.now().strftime("%H:%M:%S")
