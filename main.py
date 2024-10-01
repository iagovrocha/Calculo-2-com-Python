from sympy import *

def calcular(expre, limitInferior=None, limitSuperior=None):
    func = simplify(expre, evaluate=False)

    if limitInferior is not None and limitSuperior is not None:
        integral = integrate(func, (x, limiteInicial, limiteFinal))
    else:
        integral = integrate(func, x)

    return integral


def calcularArea(expre, limitInferior=None, limitSuperior=None):
    func = parse_expr(expre, transformations="all", evaluate=False)
    # TEM QUE MELHORAR
    if limitInferior is not None and limitSuperior is not None:
        raizes = solve(func, x, dict=True)
        print(raizes)
        controle = False
        a = list()
        for r in raizes:
            a.append(r[x])
            if r[x] < 0:
                controle = True
        m = max(a)

        if controle:
            integral = abs(integrate(func, (x, limiteInicial, m))) + abs(integrate(func, (x, m, limiteFinal)))
        else:
            integral = abs(integrate(func, (x, limiteInicial, limiteFinal)))
    else:
        integral = integrate(func, x)

    return integral


x, y, z = symbols('x y z')

expressão = str(input("Digite a função f(x): "))
limiteInicial = str(input("Digite o limite inicial do limite de interação: "))
limiteFinal = str(input("Digite o limite final do limite de interação: "))

limiteInicial = float(limiteInicial) if limiteInicial else None
limiteFinal = float(limiteFinal) if limiteFinal else None

print(f"TESTE 01: {calcular(expressão, limiteInicial, limiteFinal)}")



# TEM QUE VERIFICAR SE A ÁREA NÃO ESTÁ FORA PODE SER ANTES OU DEPOIS, POR EXEMPLO TODAS AS RAIZES POSITIVAS,
# MAS NENHUMA É ANTES DO LIMITE INICIAL ISSO FAZ COM QUE VERIFICAMOS SE AS RAIZES ESTÃO DEPOIS DOS LIMIT. INICIAL
# https://pt.symbolab.com/solver/integral-calculator/%20%5Cint_%7B0%7D%5E%7B5%7D%5Cleft(2x%5E%7B2%7D-11x%2B5%5Cright)dx?or=input

"""raizes = solve(expressão, x, dict=True)
print(raizes)
controle = False
a = list()
for r in raizes:
    a.append(r[x])
    if r[x] < 0:
        controle = True
m = max(a)

if controle:
    integral = abs(integrate(expressão, (x, limiteInicial, m))) + abs(integrate(expressão, (x, m, limiteFinal)))

else:
    integral = abs(integrate(expressão, (x, limiteInicial, limiteFinal)))"""

#integral = integrate(expressão, (x, 0, 5))
#print(raizes[0][x])
#print(f"O resultado da integral: {integrate(expressão, (x, limiteInicial, limiteFinal))}")
print(f"A área é: {calcularArea(expressão, limiteInicial, limiteFinal)} u.a")
