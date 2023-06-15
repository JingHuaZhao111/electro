from datetime import datetime, timedelta
import time


def next_update_time():
    current_time = datetime.now().replace(second=0, microsecond=0)
    next_update_time = current_time.replace(hour=0, minute=0, second=0) + timedelta(minutes=15)

    while True:
        current_time = datetime.now().replace(second=0, microsecond=0)

        if current_time >= next_update_time:
            next_update_time = current_time + timedelta(minutes=15)
            return next_update_time

        time.sleep(1)
