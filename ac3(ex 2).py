def dia_semana(numero):
    dias_da_semana = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]
    if 1 <= numero <= 7:
        return dias_da_semana[numero - 1]
    else:
        return ""

def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia

# Executando o teste
testa_dia_semana()
