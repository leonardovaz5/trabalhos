N = int(input())

vetor = list(map(int, input().split()))

menor_valor = vetor[0]
posicao = 0
for i in range(1, N):
    if vetor[i] < menor_valor:
        menor_valor = vetor[i]
        posicao = i

print("Menor valor:", menor_valor)
print("Posicao:", posicao)
