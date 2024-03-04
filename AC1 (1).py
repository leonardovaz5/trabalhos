import math

def resolver_equacao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2*a)
    x2 = (-b - raiz_delta) / (2*a)
    return x1, x2

a = float(input("Informe o parâmetro a da equação: "))
b = float(input("Informe o parâmetro b da equação: "))
c = float(input("Informe o parâmetro c da equação: "))

raiz1, raiz2 = resolver_equacao_segundo_grau(a, b, c)

print("A primeira raiz da equação é", raiz1)
print("A segunda raiz da equação é", raiz2)
