from datetime import datetime


def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time
