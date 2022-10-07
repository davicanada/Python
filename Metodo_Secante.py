from math import sqrt, log10
import time

print("Método Numérico da Secante\n")

e=0.0001
k=0.05
Re=10**8
x0=0.02114
x1=0.02116

def f(x):
  return 1/sqrt(x) + 2*log10((k/(3.7)) + (2.51/(Re*sqrt(x)))) 

def secante(x0, x1, Erro):
  i = 0                           
  Er = 9999                     
  xa1 = x0
  x = x1
  while(Er >= e):          
    xa2 = xa1
    xa1 = x
    x = xa1 - f(xa1)*(xa2 - xa1)/(f(xa2) - f(xa1))  
    Er = abs((x - xa1)/x)
    i = i + 1
  return (x, i, Er)

start = time.time()                      

(raiz, iteracoes,erro) = secante(x0, x1, e)

time.sleep(1)
end = time.time()  

print('\nRaiz = ', raiz)
print('Iterações = ', iteracoes)
print('Erro = ', erro)

duracao = (end - start)
print ("O tempo de execução foi de: {} segundos".format(duracao))

