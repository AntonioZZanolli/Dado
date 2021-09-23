import random
from time import sleep

print("*********Bem-vindo*********\n"
      "***************************")
escolha = int(input("Para girar o dado digíte 1: "))

while escolha == 1:
    dado = (1, 2, 3, 4, 5, 6)
    resultado = random.choice(dado)
    print(resultado)
    escolha = int(input("Para girar o dado novamente digíte 1, ou \n"
                        "Aperte outra tecla para finalizar: "))
else:
    print("Obrigado por utilizador o dado")
    sleep(2)