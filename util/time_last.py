from datetime import datetime, timedelta


def last_update_time():
    current_time = datetime.now()+timedelta(hours=8)
    last_update_time = current_time.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(minutes=15)

    while last_update_time < current_time:
        last_update_time += timedelta(minutes=15)

    return last_update_time
