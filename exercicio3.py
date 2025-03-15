import math

pontoPlanoUmX = int(input("X do primeiro ponto: "))
pontoPlanoUmY = int(input("Y do primeiro ponto: ")) 

PontoPlanoDoisX = int(input("X do segundo ponto: "))
PontoPlanoDoisY = int(input("Y do segundo ponto: "))

distanciaPontos = math.sqrt(((PontoPlanoDoisX - pontoPlanoUmX) ** 2) + ((PontoPlanoDoisY - pontoPlanoUmY) ** 2))

print("Valor da distância entre os pontos: ", distanciaPontos)