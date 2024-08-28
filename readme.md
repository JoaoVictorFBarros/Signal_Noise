# Visualização de Sinais com Atenuação e Ruído

Este projeto permite visualizar e ajustar sinais com diferentes características, como atenuação, ruído, amplitude e comprimento de onda. A interação em tempo real com esses parâmetros ajuda a entender como eles afetam o sinal.

### Clone o repositório
```bash
git clone https://github.com/JoaoVictorFBarros/Signal_Noise.git
```


### Instalação das Dependências

Se ainda não tiver as bibliotecas instaladas, use:

```
pip install numpy matplotlib
```

### Executando o Projeto

```
python3 main.py
```
<div align="center">
<img src=print.png width=80%>
</div>


## Conceitos e Efeitos dos Parâmetros

### 1. Atenuação

A atenuação é a redução da amplitude do sinal. Em termos práticos, isso significa que o sinal se torna mais fraco à medida que a atenuação aumenta. A atenuação é frequentemente usada para simular a perda de sinal em sistemas de comunicação ou para ajustar o volume de um sinal de áudio. No gráfico, a atenuação reduz a altura das ondas representadas.

### 2. Ruído

O ruído é uma variação aleatória adicionada ao sinal original. Na prática, o ruído pode representar interferências ou imprecisões que ocorrem durante a transmissão de dados ou medição. O ruído adicionado ao sinal faz com que o sinal exibido seja mais irregular e menos claro, imitando a presença de perturbações reais em um sistema.

### 3. Amplitude

A amplitude é a altura máxima do sinal. Em termos reais, é uma medida da força ou intensidade do sinal. Ajustar a amplitude altera a largura do sinal na visualização, permitindo ver como mudanças na intensidade afetam o sinal.

### 4. Comprimento de Onda

O comprimento de onda é a distância entre dois picos consecutivos de uma onda. Em sistemas de comunicação e física, isso determina a periodicidade do sinal. Um comprimento de onda menor resulta em uma frequência maior, e vice-versa. Alterar o comprimento de onda muda a "densidade" das ondas exibidas no gráfico.

### 5. Tipo de Curva

O tipo de curva determina a forma do sinal:
- **Senoide**: Representa um sinal contínuo e suave, comum em ondas de áudio e sinais elétricos.
- **Gaussiana**: Representa uma distribuição de probabilidade e é usada para simular sinais com variação gradual.
- **Quadrada**: Representa um sinal que alterna abruptamente entre dois níveis, útil para simular sinais digitais ou pulsos.

## Interatividade

O sistema permite que você ajuste todos esses parâmetros e veja imediatamente como cada um afeta o sinal. Esta interatividade é crucial para entender a relação entre os parâmetros e a forma do sinal gerado.

