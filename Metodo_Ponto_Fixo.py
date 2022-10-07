from math import sqrt, log10
import time


print("Método Ponto Fixo\n")
# x0=float(input("Entre com o numero real x0: "))
# e=float(input("Digite o valor da tolerância máxima "))
# k=float(input("Digite o valor de k: "))
# Re=float(input("Digite o valor de Re: "

k=0.05
Re=10**8
x0 =0.02115
e =0.0001


def f(x):
    return 1/sqrt(x) + 2*log10((k/(3.7)) + (2.51/(Re*sqrt(x))))

def w(x):
    Wx= 1/(4*(log10((k/(3.7))+(2.51/(Re*sqrt(x))))**2))
    return Wx

def ponto_fixo(x0):
    i=0
    while True:
        i+=1
        x1=w(x0)
        if abs(f(x1)) < e:
            return (x1, i, abs(f(x1)))
        x0=x1
           
start = time.time()                      

(raiz, iteracoes,erro) = ponto_fixo(x0)

time.sleep(1)
end = time.time()  

print('\nRaiz = ', raiz)
print('Iterações = ', iteracoes)
print('Erro = ', erro)
        
duracao = (end - start - 1)
print ("O tempo de execução foi de: {} segundos".format(duracao))