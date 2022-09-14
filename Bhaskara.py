import math
print("Vamos calcular uma equação do segundo grau (ax²+bx+c=0):")
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
delta = (b**2)-(4*a*c)
if (delta > 0):
    print("Possui duas raízes reais:")
    dX = 2*a
    nX1 = int(-b+math.sqrt(delta))
    nX2 = int(-b-math.sqrt(delta))
    if (nX1 % dX == 0):
        print("X' =", nX1//dX)
    else:
        # Apresenta a reposta em forma de fração
        print("X' =", nX1,"/",dX)
    if (nX2 % dX == 0):
        print("X'' =", nX2//dX)
    else:
        # Apresenta a reposta em forma de fração
        print("X'' =", nX2,"/",dX)
elif (delta == 0):
    print("Possui somente uma raiz real:")
    x = (- b - math.sqrt(delta))/(2*a)
    print("X' = X'' =",x)
else:
    print("Não possui raízes reais.")
