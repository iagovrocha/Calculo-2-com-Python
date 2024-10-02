from sympy import *
x, y, z = symbols('x y z')
funcaoX= str(input("Digite sua função f(x) aqui: ")).lower()

derivada = diff(funcaoX, x)
a = float(input('Digite o inicio do limite: '))
b = float(input('Digite o fim do limite: '))

Comprimento = integrate(sqrt(1 + ((derivada)**2)), (x, a, b))

print(derivada)
print(f'O comprimento da função é {Comprimento}')