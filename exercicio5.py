sexo = input("Digite o sexo (f) ou (m): ")
altura = float(input("Altura (em metros): "))

if sexo == "m":
    peso_ideal = (72.7 * altura) - 58
    print("Peso ideal: ", peso_ideal)
elif sexo == "f":
    peso_ideal = (62.1 * altura) - 44.7
    print("Peso ideal: ", peso_ideal)
else:
    print("Sexo inválido! Digite 'f' para feminino ou 'm' para masculino.")