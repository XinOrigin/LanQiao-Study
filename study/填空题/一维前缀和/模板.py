a:list
s = [0] *(n+1)
for i in range(1,n+1):
    s[i] = s[i-1] + a[i-1]