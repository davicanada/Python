from math import sqrt, log10
import time

print("Método Numérico da Bisseção\n")

a=0.002115
b=0.2115
e=0.0001
k=0.05
Re=10**8

def f(x): 
    return 1/sqrt(x) + 2*log10((k/3.7)+(2.51/(Re*sqrt(x))))

def bissecao(a,b):      
    i=0
    # se o intervalo a b for menor q a precisão 
    # a resposta é o valor médio de a b
    if b-a<e:
        x=(a+b)/2
        return (x, i, abs(a-b))
    else:
        while True:
            i+=1 #incrementa o contador para medir o número de iterações
            x=(a+b)/2 #pega x como o ponto central do intervalo a b
            fxa=f(a) #calcula fx no ponto a
            fxb=f(b) #calcula fx no ponto b
            fx=f(x)  #calcula fx no ponto x
            if fx==0.0: #se fx de x for menor q a precisão o programa acabar pegando x como resposta
                return (x, i, abs(a-b))
            elif fxa*fx<0: #verifica se houve troca de sinal no valor de y a de a para x, se sim x é novo b
                b=x
            elif fxa*fx>0: #caso contrário x é o novo a
                a=x
            if b-a<e:  # se o intervalo a b for menor q a precisão o programa acaba pegando o valor médio de a b
                x = (a + b) / 2
                return (x, i, abs(a-b))

start = time.time()                      

(raiz, iteracoes,erro) = bissecao(a,b)

time.sleep(1)
end = time.time()  

print('\nRaiz = ', raiz)
print('Iterações = ', iteracoes)
print('Erro = ', erro)

duracao = (end - start - 1)
print ("O tempo de execução foi de: {} segundos".format(duracao))