import datetime
d = datetime.date(1900,1,1)

while d <= datetime.date(2024,12,31):
    
    if d.day==1 and d.weekday() == 0:
        print(d)
    d += datetime.timedelta(days=1)