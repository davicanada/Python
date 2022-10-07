from math import sqrt, log10
import time

print("Método de Newton \n")
# x0=float(input("Entre com o numero real x0: "))
# e=float(input("Digite o valor da tolerância máxima "))
# k=float(input("Digite o valor de k: "))
# Re=float(input("Digite o valor de Re: "))

k= 0.0
Re=10**6
x0 =0.02115
e =0.0001


def f(x):
   return 1/sqrt(x) + 2*log10((k/(3.7)) + (2.51/(Re*sqrt(x))))

def f_linha(x):
    return (sqrt(x)*(-0.5*k*Re-2.01665)-4.6435)/(k*Re*(x**2)+9.287*(x**1.5))

def newton(x0):
    i = 0
    while abs(f(x0)) > e:
        x0 = x0 - (f(x0)/f_linha(x0))
        i += 1
    return (x0, i, abs(f(x0)))
    
    
start = time.time()                      

(raiz, iteracoes,erro) = newton(x0)

time.sleep(1)
end = time.time()  

print('\nRaiz = ', raiz)
print('Iterações = ', iteracoes)
print('Erro = ', erro)

duracao = (end - start - 1)
print ("O tempo de execução foi de: {} segundos".format(duracao))