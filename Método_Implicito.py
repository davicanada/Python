from math import sqrt, log10, pow
import time

print("Método Iterativo \n")
# x0=float(input("Entre com o numero real x0: "))
# e=float(input("Digite o valor da tolerância máxima "))
# k=float(input("Digite o valor de k: "))
# Re=float(input("Digite o valor de Re: "))

k=0.05
Re=10**8
x0 =0.02115
e =0.0001


def f0(x):
    return -(2*log10(((k)/3.7)+(2.51/(Re*sqrt(x)))))

def f1(x):
    return pow((1/x), 2)

def iterativo(x0):
    i = 0
    while (True):
        i+=1
        result_f0 = f0(x0)
        result_f1 = f1(result_f0)

        x1 = result_f1
        diff = abs(x1 - x0)        
        x0 = x1
        
        if  diff < e:
            return (x1,i, diff)

start = time.time()                      

(raiz, iteracoes,erro) = iterativo(x0)

time.sleep(1)
end = time.time()  

print('\nRaiz = ', raiz)
print('Iterações = ', iteracoes)
print('Erro = ', erro)
        
duracao = (end - start - 1)
print ("O tempo de execução foi de: {} segundos".format(duracao))