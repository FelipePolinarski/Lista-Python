x = int(input( "Digite o primeiro número: "))
y = int(input( "Digite o segundo número: "))
total = 0

def divisao(x,y,total):
  if y == 0:
    print("Não é possível dividir por zero.")
    y = int(input("Digite o segundo número novamente: "))
  while x >= y:
    x = x - y
    total = total + 1
  print(total)
  
divisao(x,y,total)
