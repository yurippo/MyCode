print("********************************")
print("Bem vindo ao jogo Advinhação Int !")
print("********************************")

numero_secreto = 42
chute_str = input("Digite seu número")
chute = int(chute_str)
print("Você digitou ", chute)
if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")