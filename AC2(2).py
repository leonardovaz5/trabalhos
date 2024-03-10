def calcula_salario(valor_hora, num_horas, irpf=0.275):
    salario_bruto = valor_hora * num_horas
    desconto_irpf = salario_bruto * irpf
    salario_liquido = salario_bruto - desconto_irpf
    return salario_liquido

salario_liquido = calcula_salario(23, 161)
print("Salário líquido: R$", salario_liquido)
