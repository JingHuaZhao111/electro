from datetime import datetime, timedelta


def next_update_time():
    current_time = datetime.now()+timedelta(hour=8)
    next_update_time = current_time.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(minutes=15)

    while next_update_time <= current_time:
        next_update_time += timedelta(minutes=15)

    return next_update_time
