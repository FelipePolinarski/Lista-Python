x = int(input("Digite a base: "))
y = int(input("Digite o expoente: "))
cont = 1
result = x

while cont < y:
  result = result * x
  cont = cont + 1
print(result)
