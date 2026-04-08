from datetime import *
start = date(2000,1,1)
end = date(2020,10,1)
d =timedelta(days=1)
km = 0
while start <= end:
    if start.day == 1 or start.weekday() == 0:
        km+=1

    start+= d
    km+=1
print(km)
