import datetime

now=datetime.datetime.now()
date=datetime.date.today()
time=datetime.datetime.now().time()
print(now)
print(date)
print(time)

formatted_time=now.strftime("%Y/%m/%d %H:%M:%S") #full 2025 format year
formatted_time=now.strftime("%y/%m/%d %H:%M:%S") #short 25 year
formatted_time=now.strftime("%y/%b/%d %H:%M:%S")#letter month feb
formatted_time=now.strftime("%y/%B/%d %H:%M:%S")#Full letter month feb
formatted_time=now.strftime("%y/%B/%d %H:%M:%S")#Full letter month feb
formatted_time=now.strftime("%y/%B/%d %a %H:%M:%S")#short week letter week wed
formatted_time=now.strftime("%y/%B/%d %A %H:%M:%S")#week letter month wednesday
formatted_time=now.strftime("%y/%B/%d %A %I:%M:%S")#12 hours format I
formatted_time=now.strftime("%y/%B/%d %A %I:%M:%S %p")#AM PM P

datte="25-12-2300 10:45:00"
parsedate=datetime.datetime.strptime(datte,"%d-%m-%Y %H:%M:%S")
print(formatted_time)
print(parsedate, type(parsedate))