def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def calculadora():
    while True:
        try:
            num1 = float(input("Informe um número: "))
            num2 = float(input("Informe outro número: "))
            operacao = input("Informe a operação (soma, subtração, multiplicação, divisão): ")

            if operacao.lower() == 'soma':
                resultado = soma(num1, num2)
            elif operacao.lower() == 'subtração':
                resultado = subtracao(num1, num2)
            elif operacao.lower() == 'multiplicação':
                resultado = multiplicacao(num1, num2)
            elif operacao.lower() == 'divisão':
                resultado = divisao(num1, num2)
            else:
                print("Operação inválida")
                continue

            print(f"Resultado: {resultado}")
        except ValueError:
            print("Por favor, insira números válidos.")
        except Exception as e:
            print("Ocorreu um erro:", e)

        continuar = input("Deseja realizar outra operação? (s/n): ")
        if continuar.lower() != 's':
            break

# Testando a calculadora
calculadora()
