from datetime import datetime

exam_date= datetime(2025,12,23,11,30,0)
now= datetime.now()
remaining_time = exam_date - now

if remaining_time.total_seconds() > 0:
    days = remaining_time.days
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print("Time the left until the exam:")
    print(f"{days} days, {hours} hours ,{minutes}, minutes, {seconds} seconds")
else:
    print(" The exam time has passed")