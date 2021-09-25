#Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.


n = int(input("Digite um número inteiro: ")) 
d = (n // 10) % 10 
print("O digito das dezenas e:", d)