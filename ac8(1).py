import math

def mdc(a, b):
    return math.gcd(a, b)
    
N = int(input())

for _ in range(N):
    F1, F2 = map(int, input().split())
   
    max_div = mdc(F1, F2)
    
    result = max_div
    print(result)
