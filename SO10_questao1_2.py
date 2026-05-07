#Declarar
vet: int = [0]*100
i: int = 0
maior: int = 0
menor: int = 0
total: int = 0
media: int = 0

#Início
for i in range (0, 100):
    vet[i] = int(input("Insira um valor: "))
menor = vet[0]
maior = vet[0]
total += vet[0]
for i in range (1, 100):
    if (vet[i] > maior):
        maior = vet[i]
    elif (vet[i] < menor):
        menor = vet[i]
    total += vet[i]
print ("Menor valor:", menor)
print ("Maior valor:", maior)
media = total / 100
print ("Média dos valores:", media)
#Fim