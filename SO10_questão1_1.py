#Declarar
vet: int = [0]*50
i: int = 0
a: int = 0

#Início
for i in range (0, 50):
    vet[i] = int(input("Insira um valor: "))
print ("Valores entre 10 e 200:")
for i in range (0, 50):
    if (vet[i] >= 10 and vet[i] <= 200):
        print (vet[i], end = ' ')
print ("\nValores com números ímpares:")
for i in range (0, 50):
    a = vet[i] % 2
    if a != 0:
        print (vet[i], end = ' ')
print ("")
#Fim