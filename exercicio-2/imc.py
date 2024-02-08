import math

def imc(peso, altura):
    resultado = peso / math.pow(altura, 2)
    print("Seu IMC é: ", round(resultado))
    return resultado

resultado_imc = imc(float(input("Digite seu peso: ")), float(input("Digite sua altura: ")))

if resultado_imc < 18.5:
    print("Baixo Peso")
elif resultado_imc > 18.5 and resultado_imc < 24.99:
    print("Normal")
elif resultado_imc > 25 and resultado_imc < 29.99:
    print("Sobrepeso")
else:
    print("Obesidade")

