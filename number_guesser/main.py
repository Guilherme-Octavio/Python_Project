import random
from time import sleep

print("Bem vindo ao adivinhador de numero")
print("----------------------------------")
top_range = input("Até que numero (int) deseja adivinhar: ")
print("----------------------------------")
print("Selecione numero inteiro (int) ou Numero com virgulas (float)")
numbers_types = input()
if numbers_types != "int" and numbers_types != "float":
    print("Por favor Digite (int) ou (float)")
    numbers_types = input()
    if numbers_types != "int" and numbers_types != "float":
        print("Sério????")
        sleep(1)
        quit()



#Verifica se o userinput é um digito
if top_range.isdigit():
    top_range = int(top_range)
    lives = top_range / 2
    if lives > 10:
        lives = 10

    # Verifica se o numero não é 0 ou menor a ele
    if top_range <=0:
        print("Digite um numero maior que 0 da proxima vez")
        sleep(2)
        quit()
    # Verifica se o numero não é 10 ou menor a ele    
    elif top_range <= 10:
        print("Muito facil né, pela mor né")
        sleep(1)
        quit()
    # Verifica se o numero não é 250 ou maior a ele    
    elif top_range >= 250:
        print("Calma la né amigão")
        sleep(1)
        quit()
else:
    print("Digite uma numero da proxima vez")
    sleep(2)
    quit()

# Seleciona a dificuldade do jogo, Logo a quant de vidas/tentativas
print("Agora selecione a dificuldade (E)asy (N)ormal (H)ard")
dificult = input()

if dificult == "E" or dificult == "e" and top_range > 50:
    print("Agora você tem ",lives ," vidas")
    print("O numero selecionado pela maquina é inteiro")
    d = 0
    
elif top_range < 50 and dificult == "E" or dificult == "e":
    print("Você não pode selecionar facil com ", top_range," digitos")
    sleep(1)
    quit()

elif dificult == "N" or dificult == "n":
    print("Agora você tem ",lives ," vidas")
    if numbers_types == "float":
        print("O numero selecionado pode ser fracionado em 2 casas '0.00'")
        d = 2


elif dificult == "H" or dificult == "h":
    print("Agora você tem ",lives ," vidas")
    if numbers_types == "float":
        print("O numero selecionado pode ser fracionado em 3 casas '0.000'")
        d = 3


else:
    print("Digite uma das opcões")
    quit()

if numbers_types == "int":
    random_number = random.randint(0, top_range)
elif numbers_types == "float":
    random_number = round(random.uniform(0.0, top_range), d)

while True:
    if lives > 0:
        
        print("Vida: ", lives)
        if numbers_types == "int":
            valid_number = int(input("Adivinhe: "))
        elif numbers_types == "float":
            valid_number = float(input("Adivinhe: "))

        if valid_number < random_number:
            print("Digite um numero maior")
            lives -= 1

        elif valid_number > random_number:
            print("Digite um numero menor")
            lives -= 1

        elif valid_number == random_number:
            print("Vida: ", lives)
            print("Parabens você conseguiu!!")
            sleep(1)
            quit()
    else:
        print("Você perdeu todas as vidas")
        print("O numero era", random_number)
        print("--------------------------")
        print("GAME OVER")
        sleep(1)
        quit()