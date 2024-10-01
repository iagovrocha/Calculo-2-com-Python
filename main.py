# Grupo: Alan Rocha Barbosa Soares, Alla Henrique Passos Lima, Arthur de Oliveira Ferreira, 
# Iago Vieira Rocha, João Paulo Lordêlo Pedreira Vivas, Luiz Fernando Santos Sobral.

from sympy import *

def calcular(expre, limitInferior=None, limitSuperior=None):
    func = parse_expr(expre, transformations="all", evaluate=False)

    if limitInferior is not None and limitSuperior is not None:
        integral = integrate(func, (x, limitInferior, limitSuperior))
    else:
        integral = integrate(func, x)
    return integral

def calcularArea(expre, limitInferior=None, limitSuperior=None):
    func = parse_expr(expre, transformations="all", evaluate=False)
    if limitInferior is not None and limitSuperior is not None:
        f_abs = Abs(func)
        integral = abs(integrate(f_abs, (x, limitInferior, limitSuperior)))
    else:
        integral = integrate(func, x)
    return integral

def calculoComprimento(expre, limitInferior=None, limitSuperior=None):
    func = parse_expr(expre, transformations="all", evaluate=False)
    derivada = diff(func, x)
    comprimento = integrate(sqrt(1 + derivada**2), (x, limitInferior, limitSuperior)).doit().evalf()
    return comprimento

def calculoVolume(expre, limitInferior=None, limitSuperior=None):
    func = parse_expr(expre, transformations="all", evaluate=False)
    volume = integrate(pi*func**2, (x, limitInferior, limitSuperior))
    return volume

x = Symbol('x')

print("=-"*40)
print(f"{"Calculadora de Área, Comprimento e Volume":^80}")
print("=-"*40)

expressão = str(input("Digite a função f(x): "))
limiteInicial = str(input("Digite o limite inicial do limite de interação: "))
limiteFinal = str(input("Digite o limite final do limite de interação: "))

limiteInicial = float(limiteInicial) if limiteInicial else None
limiteFinal = float(limiteFinal) if limiteFinal else None
print("=-"*40)
print(f"    Calculo da Integral: {calcular(expressão, limiteInicial, limiteFinal)}")
print(f"    A área é: {calcularArea(expressão, limiteInicial, limiteFinal)} u.a")
print(f"    O comprimento é: {calculoComprimento(expressão, limiteInicial, limiteFinal)}")
print(f"    O volume é: {calculoVolume(expressão, limiteInicial, limiteFinal)} u.c")
print("=-"*40)
