coluna = int(input())
operacao = input().upper()

matriz = []
for _ in range(12):
    linha = []
    for _ in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
for i in range(12):
    soma += matriz[i][coluna]

if operacao == 'M':
    resultado = soma / 12
else:
    resultado = soma

print(f'{resultado:.1f}')