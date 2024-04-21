x = int(input())
y = int(input())

soma = sum(i for i in range(min(x, y), max(x, y) + 1) if i % 13 != 0)

print(soma)
