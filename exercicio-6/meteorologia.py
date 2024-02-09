temperaturas = []

while True:
    temp = input("Digite uma temperatura (ou digite 'fim', para encerrar): ")
    if temp.lower() == "fim":
        break
    temperaturas.append(float(temp))

if temperaturas:
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)
    temperatura_media = sum(temperaturas) / len(temperaturas)

    print(f"A maior temperatura é: {temperatura_maxima}")
    print(f"A menor temperatura é: {temperatura_minima}")
    print(f"A média das temperaturas é: {temperatura_media:.2f}")

else:
    print("Colaca uma temperatura animal")