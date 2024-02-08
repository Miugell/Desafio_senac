pergunta_1 = input("Telefonou para a vítima? (sim/não): ").lower()
pergunta_2 = input("Esteve no local do crime? (sim/não): ").lower()
pergunta_3 = input("Mora perto da vítima? (sim/não): ").lower()
pergunta_4 = input("Devia para a vítima? (sim/não): ").lower()
pergunta_5 = input("Já trabalhou com a vítima? (sim/não): ").lower()

respostas_positivas = [pergunta_1, pergunta_2, pergunta_3, pergunta_4, pergunta_5].count('sim')

if respostas_positivas == 0 or respostas_positivas == 1:
    print("Inocente")
elif respostas_positivas == 2:
    print("Suspeita")
elif respostas_positivas == 3 or respostas_positivas == 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Respostas inválidas. Responda com 'sim' ou 'não' ")