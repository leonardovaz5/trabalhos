def eq_seg_grau(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta >= 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        return x1, x2
    else:
        return None

def bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

print(eq_seg_grau(1, -3, 2))  # Saída: (2.0, 1.0)
print(eq_seg_grau(1, -2, 1))   # Saída: (1.0, 1.0)
print(eq_seg_grau(2, 3, 4))    # Saída: None

print(bissexto(2020))  # Saída: True
print(bissexto(2021))  # Saída: False
print(bissexto(2000))  # Saída: True
