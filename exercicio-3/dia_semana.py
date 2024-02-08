dias_semana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", 
               "Sexta-feira", "Sabado"]
numero = int(input("Digite um numero inteiro de 1 a 7: "))

if 1 <= numero <=7:
    print(f"O numero {numero} é", dias_semana[numero -1])
else:
    print("Numero inválido, por favor digite um numero de 1 a 7")