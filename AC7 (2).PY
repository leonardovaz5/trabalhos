cont_pares = 0

for _ in range(5):
   
    valor = int(input())
    
    
    if valor % 2 == 0:
        cont_pares += 1

print(f"{cont_pares} valores pares")
