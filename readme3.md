# 🧪 Código: Simulação de Polaridade Quântica com Qubit
Este código em Python simula visualmente o comportamento de um qubit ao ser submetido a diferentes portas quânticas (X, Y e Z). A ideia é representar, de forma gráfica e conceitual, como um qubit pode ser manipulado e como isso reflete a Lei da Polaridade em termos quânticos.

## Conceito Base
Um qubit pode existir em um estado de superposição, onde ele não é apenas |0⟩ ou |1⟩, mas uma combinação dos dois, com amplitudes complexas. O código representa esse estado usando:

- amplitude_real

- amplitude_imaginaria

- fase (em radianos)

## Funções Implementadas

aplicar_porta_x(estado)
Aplica a porta X ao qubit, que inverte seu estado (como um NOT).

 Transforma |0⟩ em |1⟩.

aplicar_porta_z(estado)
Aplica a porta Z, que altera apenas a fase do estado.

Inverte o sinal da amplitude real, simulando um giro no eixo Z.

aplicar_porta_y(estado)
Aplica a porta Y, combinando efeitos de X e Z.

Coloca o qubit em superposição perfeita, com componentes real e imaginária iguais em módulo, formando o valor aproximado 0.707.

## 📈 Visualização Gráfica
A função mostrar_estado() plota os vetores resultantes no plano complexo, permitindo observar como cada porta altera a direção e o módulo do qubit.

Azul: Estado inicial |0⟩

Vermelho: Após Porta X

Verde: Após Porta Z

Roxo: Após Porta Y (superposição)

![visupo](https://github.com/user-attachments/assets/b076b26b-2cbc-41d0-a9a7-d819154bd693)

A Polaridade e o 0.707
Quando aplicamos a porta Y, o qubit atinge um estado de equilíbrio quântico, com os valores:
```
amplitude_real ≈ 0.707
amplitude_imaginaria ≈ -0.707
```

Esse ponto é a superposição perfeita, onde o qubit vibra no centro da dualidade, podendo se tornar 0 ou 1 com igual probabilidade. Representa o auge do potencial quântico.


