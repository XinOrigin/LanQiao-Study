from datetime import date,timedelta
start =date(2000,1,1)
end = date(2020,1,1)
delta = timedelta(days=1)
while start<= end:
    if start.day == 1 or start.weekday() == 0:
        pass
    start + = delta