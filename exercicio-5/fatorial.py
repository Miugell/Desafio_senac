def fatorial(numero):
    resultado = 1
    while numero > 0:
        resultado *= numero
        numero -= 1
    return resultado

numero_usuario = int(input("Digite um numero: "))
print(f"O fatorial de {numero_usuario} é: {fatorial(numero_usuario)}")