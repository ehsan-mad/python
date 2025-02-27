from datetime import datetime ,timedelta


today=datetime.today().date()
print(today)
yesterday=today - timedelta(days=1)
print(yesterday)
tomorrow=today + timedelta(days=1)
print(tomorrow)


time=datetime.today()
updated_time=time + timedelta(hours=2,minutes=45)
print(time,updated_time)


