import sys 
def all_input():
    all_data = sys.stdin.read().split()
    if not all_data:
        return
    
    n = int(all_data[0])
    return list(map(int,all_data[1:n+1])) 


def check_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    else:
        return True
 
def main():
    numbers = all_input()
    if not numbers:
        return
    primes = [str(x) for x in numbers if check_prime(x) ]
    print(" ".join(primes))
if __name__ == "__main__":
    main()
