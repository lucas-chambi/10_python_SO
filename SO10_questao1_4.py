#Declarar
vet: float = [0]*30
i: int = 0
total: int = 0
media: float = 0.0
quant: int = 0
pos: int = 0

#Início
for i in range (0, 30):
    vet[i] = int(input("Insira um valor: "))
    total += vet[i]
media = total / 30
print (f"Média do grupo: {media:.2f}")
for i in range (0, 30):
    if (vet[i] > media):
        quant += 1
print ("Quantidade de notas acima da média:", quant)
print ("Posição dos valores abaixo da média:", end = ' ')
for i in range (0, 30):
    if vet[i] < media:
        print (i, end = ' ')
print ("")
#Fim