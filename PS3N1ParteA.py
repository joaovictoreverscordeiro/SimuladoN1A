import matplotlib.pyplot as plt
import numpy as np
import random

#variáveis a descobrir
omega0=6.7*(10**6)
a=0.134

#cabeçalho
print('='*15,'Parte A','='*15)
print()

#frquência
ofreq=str(input('Digite a ordem de grandeza da frequência (k, M, G): ').strip())

if ofreq=='k':
    mfreq=10**3
elif ofreq=='M':
    mfreq=10**6
elif ofreq=='G':
    mfreq=10**9
else:
    input('ERRO. Opção inválida para ordem de grandeza, as opções válidas são k, M e G. Clique ENTER para encerrar o programa. ')
    exit()

nfreq=float(input('Digite a frequência (sem unidade; range: 1 a 1000): ').strip())
freq=(1+random.uniform(-0.05,0.05))*2*np.pi*nfreq*mfreq

if nfreq>1000 or nfreq<1:
    input('ERRO. Valor fora do range possível, que compreende 1 a 1000. Clique ENTER para encerrar o programa. ')
    exit()
else:
    pass

#voltagem
volt0=float(input('Digite a amplitude de voltagem V0 (sem unidade; range: 0 a 15.0): ').strip())
volt=(1+random.uniform(-0.05,0.05))*volt0

if volt0>15:
    input('ERRO. Valor fora do range possível, que compreende 0 a 15. Clique ENTER para encerrar o programa. ')
    exit()
else:
    pass

voff=(1+random.uniform(-0.05,0.05))*a*volt*np.exp(-freq/omega0)

#função
def V(t):
    return voff+volt*np.cos(freq*t)

#eixos/intervalos
valuedt=['1','5','10','25','50','100','250','500']
escolhadt=str(input('Digite uma das escalas permitidas para o tempo: ').strip())
splitescolha=escolhadt.split()

if len(splitescolha)==2:
    pass
else:
    input('ERRO. Escala de tempo inserida da forma incorreta, revise os espaços. Ex. correto: 50 ms. Clique ENTER para encerrar o programa. ')
    exit()

if splitescolha[1]=='ms':
    mdt=10**(-3)
elif splitescolha[1]=='us':
    mdt=10**(-6)
elif splitescolha[1]=='ns':
    mdt=10**(-9)
elif splitescolha[1]=='ps':
    mdt=10**(-12)
else:
    input('ERRO. Escala inválida, as opções válidas são ms, us, ns, ps. Clique ENTER para encerrar o programa. ')
    exit()

for i in range(8):
    if splitescolha[0]==valuedt[i]:
        ndt=int(splitescolha[0])
    else:
        pass

if bool(ndt)==False:
    input('ERRO. Valor inválido, as opções possíveis são 1, 5, 10, 25, 50, 100, 250, 500. Clique ENTER para encerrar o programa. ')
    exit()
else:
    pass

dt=ndt*mdt

valuesdv=['0.1','0.25', '0.5', '0.75', '1','2','1.5']
strdv=str(input('Digite uma das escalas permitidas para a voltagem: ').strip())

for i in range(7):
    if strdv==valuesdv[i]:
        dv=float(valuesdv[i])
    else:
        pass

if bool(dv)==False:
    input('ERRO. Escala para V inválida, os valores válidos são 0.1, 0.25, 0.5, 0.75 1, 1.5, 2. Clique ENTER para encerrar o programa. ')
    exit()
else:
    pass

#ranges

t1=np.arange(0,5*dt,0.002*dt)

plt.plot(t1, V(t1), 'k')
plt.axis((0, 5*dt, -10*dv, 10*dv))
plt.xlabel('t (s)')
plt.ylabel('V (V)')
plt.show()

print()

input('Clique ENTER para encerrar o programa. ')