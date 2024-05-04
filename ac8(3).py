def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat

while True:
    try:
        M, N = map(int, input().split())
        
        resultado = fatorial(M) + fatorial(N)
        print(resultado)
    except EOFError:
        break
