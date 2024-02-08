import math

valor_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas você trabalhou no mês? "))

salario_bruto = valor_hora * horas_trabalhadas

imposto_renda = (salario_bruto /100) * 11
inss = (salario_bruto / 100) *8

salario_liquido = salario_bruto - imposto_renda - inss

print(f"Salário Bruto: R$ {math.ceil(salario_bruto)},00")
print(f"Imposto de renda(11%): R$ {round(imposto_renda)},00")
print(f"INSS (8%): R$ {round(inss)},00")
print(f"Salário liquido: R$ {round(salario_liquido)},00")