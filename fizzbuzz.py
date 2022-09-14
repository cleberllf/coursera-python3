numero = int(input("Qual número deseja saber se é divisível por 3 e por 5? "))
if ((numero % 3 == 0) and (numero %5 == 0)):
    print("FizzBuzz")
else:
    print(numero)