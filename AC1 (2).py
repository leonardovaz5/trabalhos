ano = int(input("Informe um ano: ")) # Solicita ao usuário que insira um ano

# Verifica se o ano é bissexto e imprime o resultado
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto")  # Se for bissexto, imprime que é bissexto
else:
    print(ano, "não é um ano bissexto")  # Se não for bissexto, imprime que não é bissexto
