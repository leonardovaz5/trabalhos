import math

# Função para resolver equação do segundo grau
def resolver_equacao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2*a)
    x2 = (-b - raiz_delta) / (2*a)
    return x1, x2

# Entrada dos coeficientes da equação
a = float(input("Informe o parâmetro a da equação: "))
b = float(input("Informe o parâmetro b da equação: "))
c = float(input("Informe o parâmetro c da equação: "))

# Resolução da equação
raiz1, raiz2 = resolver_equacao_segundo_grau(a, b, c)

# Exibição das raízes
print("A primeira raiz da equação é", raiz1)
print("A segunda raiz da equação é", raiz2)
