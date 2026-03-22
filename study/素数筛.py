import sys
def check_prime(n):
    if n <2: 
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True
input_data = sys.stdin.readline().strip().split()
if len(input_data) >= 2:
    a,b = int(input_data[0]),int(input_data[1])
prime = []
for i in range(a,b+1):
    if check_prime(i):
        prime.append(str(i))
print(" ".join(prime))
