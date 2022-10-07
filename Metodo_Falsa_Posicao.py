from math import sqrt, log10
import time

print("Método Numérico da Falsa Posição\n")
# a=float(input("Digite o valor de a: "))
# b=float(input("Digite o valor de b: "))
# e=float(input("Digite o valor da tolerância máxima: "))
# E=float(input("Digite o valor de E: "))
# D=float(input("Digite o valor de D: "))
# Re=float(input("Digite o valor de Re: "))

a=0.002115
b=0.2115
k=0.03
e=0.0001
Re=10**4

def f(x):
    return 1/sqrt(x) + 2*log10((k/(3.7)) + (2.51/(Re*sqrt(x))))

def falsa_posicao(a,b):
    i = 0
    while True:
        i+=1
        fxa=f(a)
        fxb=f(b)
        x=(a*fxb-b*fxa)/(fxb-fxa)
        fx=f(x)
        if abs(fxa) < e:
            x=a
            return (x, i, abs(fx))
        elif abs(fxb) < e:
            x=b
            return (x, i, abs(fx))
        elif abs(fx) < e:
            return (x, i, abs(fx))
        elif fxa*fx<0:
            b=x
        elif fxa*fx >0:
            a=x
        elif b-a<e:
            x=(b+a)/2
        
        
start = time.time()                      

(raiz, iteracoes,erro) = falsa_posicao(a,b)

time.sleep(1)
end = time.time()  

print('\nRaiz = ', raiz)
print('Iterações = ', iteracoes)
print('Erro = ', erro)

end = time.time()
duracao = (end - start - 1)
print ("O tempo de execução foi de: {} segundos".format(duracao))