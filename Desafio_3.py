import os

Código = input("Digite o Código do produto:")
Nome = input("Digite o Nome do produto:")
Quantidade = int(input("Digite a Quantidade do produto:"))
Preço = int(input("Digite o Preço do produto:"))

Valor = Quantidade * Preço;

print("----------Informações----------")
print("Código:",Código)
print("Nome:",Nome)
print("Valor Total:",Valor)
print("-------------------------------")

os.system("pause")