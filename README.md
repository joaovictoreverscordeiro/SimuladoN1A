# Instruções para o uso do simulador
## O aplicativo utilizado na simulação está dentro da pasta executável. Para encontrar o texto-problema você pode acessar [Drive de arquivos](https://drive.google.com/drive/folders/1tATW8H_67tJav8JZPOMwUHlEejGmKdrR?usp=sharing)

O objetivo dessa simulação é descobrir os parâmetros $a$ e $\omega_0$ de uma determinada fonte de tensão alternada (gerador de sinal). A expressão da tensão forncida em função do tempo é:

$$
V(t)=V_{off}+V_0\cos\omega t
$$

Porém, a expressão da voltagem offset é dada por:

$$
V_{off}=aV_0\exp\left(-\frac{\omega}{\omega_0}\right)
$$

Para tanto, usaremos a seguinte interface de simulação (já com um exemplo): 
```
=============== Parte A ===============
Digite a ordem de grandeza da frequência (k, M, G): k
Digite a frequência (sem unidade; range: 1 a 1000): 1
Digite a amplitude de voltagem V0 (sem unidade; range: 0 a 15.0): 7
Digite uma das escalas permitidas para o tempo: 1 ms
Digite uma das escalas permitidas para a voltagem: 2

Clique ENTER para encerrar o programa.
```

Abaixo, cada item corresponde a uma linha do `Terminal` acima.

- A ordem de grandeza da frequência $f$ da onda senoidal pode ser $\mathrm{k}=10^3$ (kilo), $\mathrm{M}=10^6$ (Mega) ou $\mathrm{G}=10^9$ (Giga) (atente-se para as letras minúsculas/maiúsculas, você deve digitá-las levando em conta isso). Portanto, a frequência será dada em $\mathrm{kHz}$ ou $\mathrm{MHz}$ ou $\mathrm{GHz}$.
- Aqui, coloque o valor numérico da frequência, já levando em conta a ordem de grandeza introduzida no programa. No exemplo acima, a frequência colocada corresponde a $1\ \mathrm{kHz}$. Aqui, só introduza números no intervalo $[1,100]$ (contendo os próprios $1$ e $100$).
- Introduza o valor de $V_0$ já em Volts e dentro do range $0\ \mathrm{V}\le V_0\le 15\ \mathrm{V}$.
- O osciloscópio digital irá gerar um gráfico de $V(t)\times t$. Portanto, assim como em um osciloscópio real, você precisa escolher a escala dos eixos que serão mostrados na tela. As unidades permitidas são $\mathrm{ms}\ (10^{-3}\mathrm{s})$, $\mathrm{us}\ (10^{-6}\mathrm{s})$, $\mathrm{ns}\ (10^{-9}\mathrm{s})$ e $\mathrm{ps}\ (10^{-12}\mathrm{s})$. Já os valores permitidos são $1,5,10,25,50,100,250,500$. Ou seja, para escrever a escala do tempo, escreva:
```
valor válido__unidade válida
```
O underline representa um espaço! Ou seja, **o valor deve ser separado da unidade por espaço**. Além disso, a unidade deve estar em minúsculo e não podem haver pontos separadores de decimais no valor. Por exemplo, o sistema não reconhece $5.0\ \text{ms}$ ou $5\ \text{MS}$, o correto seria $5\ \text{ms}$. Para cada escala, o simulador irá gerar um gráfico no intervalor $0$ até $5\Delta t$.
- Aqui, você irá colocar a escala para o eixo da voltagem. As possibilidades são $0.1,\ 0.25,\ 0.5,\ 0.75,\ 1,\ 1.5,\ 2$. Todos esses valores já estão em Volts e você não pode colocar a unidade no programa, senão ele não poderá ser executado corretamente. O osciloscópio irá gerar um gráfico no intervalo de $V$ que vai de $-10\Delta V$ até $10\Delta V$.
- Ao encerrar a página do MatPlotLib, aperte `Enter` para encerrar o programa.
