import matplotlib.pyplot as plt
import numpy as np
import random

#variáveis a descobrir
omega0=6.7*(10**6)
a=0.134

def normal():
    # frquência
    ofreq = str(input('Digite a ordem de grandeza da frequência \33[1;37m(k, M, G)\33[m: ').strip())

    if ofreq == 'k':
        mfreq = 10 ** 3
    elif ofreq == 'M':
        mfreq = 10 ** 6
    elif ofreq == 'G':
        mfreq = 10 ** 9
    else:
        print()
        input('\33[31mERRO. Opção inválida para ordem de grandeza, as opções válidas são k, M e G. Clique ENTER para reiniciar a simulação.\33[m ')
        print()
        print('=' * 129)
        print()
        normal()

    nfreq = float(input('Digite a frequência (sem unidade; range: 1 a 1000): ').strip())
    freq = (1 + random.uniform(-0.05, 0.05)) * 2 * np.pi * nfreq * mfreq

    if nfreq > 1000 or nfreq < 1:
        print()
        input('\33[31mERRO. Valor fora do range possível, que compreende 1 a 1000. Clique ENTER para reiniciar a simulação.\33[m ')
        print()
        print('=' * 129)
        print()
        normal()
    else:
        pass

    # voltagem
    volt0 = float(input('Digite a amplitude de voltagem V0 (sem unidade; range: 0 a 15.0): ').strip())
    volt = (1 + random.uniform(-0.05, 0.05)) * volt0

    if volt0 > 15 or volt0 < 0:
        print()
        input('\33[31mERRO. Valor fora do range possível, que compreende 0 a 15. Clique ENTER para reiniciar a simulação.\33[m ')
        print()
        print('=' * 69)
        print()
        normal()
    else:
        pass

    voff = (1 + random.uniform(-0.05, 0.05)) * a * volt * np.exp(-freq / omega0)

    # função
    def V(t):
        return voff + volt * np.cos(freq * t)

    # eixos/intervalos
    valuedt = ['1', '5', '10', '25', '50', '100', '250', '500']
    escolhadt = str(input('Digite uma das escalas permitidas para o tempo: ').strip())
    splitescolha = escolhadt.split()

    if len(splitescolha) == 2:
        pass
    else:
        print()
        input('\33[31mERRO. Escala de tempo inserida da forma incorreta, revise os espaços. Ex. correto: 50 ms. Clique ENTER para reiniciar a simulação.\33[m ')
        print()
        print('=' * 129)
        print()
        normal()

    if splitescolha[1] == 'ms':
        mdt = 10 ** (-3)
    elif splitescolha[1] == 'us':
        mdt = 10 ** (-6)
    elif splitescolha[1] == 'ns':
        mdt = 10 ** (-9)
    elif splitescolha[1] == 'ps':
        mdt = 10 ** (-12)
    else:
        print()
        input('\33[31mERRO. Escala inválida, as opções válidas são ms, us, ns, ps. Clique ENTER para reiniciar a simulação.\33[m ')
        print()
        print('=' * 129)
        print()
        normal()

    for i in range(8):
        if splitescolha[0] == valuedt[i]:
            ndt = int(splitescolha[0])
        else:
            pass

    if bool(ndt) == False:
        print()
        input('\33[31mERRO. Valor inválido, as opções possíveis são 1, 5, 10, 25, 50, 100, 250, 500. Clique ENTER para reiniciar a simulação.\33[m ')
        print()
        print('=' * 129)
        print()
        normal()
    else:
        pass

    dt = ndt * mdt

    valuesdv = ['0.1', '0.25', '0.5', '0.75', '1', '2', '1.5']
    strdv = str(input('Digite uma das escalas permitidas para a voltagem: ').strip())

    for i in range(7):
        if strdv == valuesdv[i]:
            dv = float(valuesdv[i])
        else:
            pass

    if bool(dv) == False:
        print()
        input('\33[31mERRO. Escala para V inválida, os valores válidos são 0.1, 0.25, 0.5, 0.75 1, 1.5, 2. Clique ENTER para reiniciar a simulação.\33[m ')
        print()
        print('=' * 129)
        print()
        normal()
    else:
        pass

    # ranges
    t1 = np.arange(0, 5 * dt, 0.002 * dt)

    plt.plot(t1, V(t1), 'k')
    plt.axis((0, 5 * dt, -10 * dv, 10 * dv))
    plt.xlabel('t (s)')
    plt.ylabel('V (V)')
    plt.show()

    print()
    input('Clique ENTER para reiniciar a simulação. ')
    print()
    print('=' * 129)
    print()

#cabeçalho
print('='*60,'\33[1;32mParte A\33[m','='*60)
print()

while True:
    try:
        normal()
    except:
        print()
        input('\33[31mERRO! Você digitou alguma entrada inválida. Clique ENTER para reiniciar a simulação.\33[m ')
        print()
        print('='*129)
        print()