import random
from datetime import  datetime
from datetime import  timedelta, datetime

time = datetime.strptime("8:00", "%H:%M")
print(time.strftime("%H:%M"))

hours = random.randint(0,23)
minutes = random.randint(0,59)
seconds= random.randint(0,59)
random_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
today_date = datetime.now().strftime("%Y-%m-%d")
print(f"Приглашаю на собрание сегодня {today_date} в {random_time}")

initial_time=datetime.strptime("08:00", "%H:%M")
added_minutes = random.randint(15,100)
new_time = initial_time +timedelta(minutes=added_minutes)
print(f"Время до прибавления: {initial_time.strftime('%H:%M')}")
print(f"Время после прибывания: {new_time.strftime('%H:%M')}")

start_time = time(hour=12)
end_time = time(hour=18)
interval=timedelta(minutes=15)
current_time = start_time
while current_time <= end_time:
    print(current_time.strftime("%H:%M"))
    current_time += interval

start_time = time(hour=6)
intervals = []
for _ in range(10):
    intervals.append(random.randint(1,15))
current_time = start_time
for i, interval in enumerate(intervals):
    print(f"{i+1}. Время:{current_time.strftime('%H:%M')} Промежуток: {interval} мин")
    current_time+=timedelta(minutes=interval)
