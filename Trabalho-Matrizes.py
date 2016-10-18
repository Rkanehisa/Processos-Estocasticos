from numpy import linalg as LA
import numpy as np
import matplotlib.pyplot as plt
#Uso do arquivo de input:
# Escreva APENAS os números
# Na primeira linha digite o número de iterações ex: 5
# Na segunda linha digite os valores do vetor de inicialização separados por espaço, utilize '.'(ponto) para separação decimal ex: 1.0 0.0
# Na terceira linha digite os valores da matriz de transição separados por espaço para as colunas.
# Utilize ';'(ponto e vírgula) para separação de linhas ex: 0.9 0.1; 0.5 0.5
# 0.9 0.1; 0.5 0.5 representa a matriz:
# [0.9 0.1]
# [0.5 0.5]

t = int(input())
initVector = np.matrix(input())
A = np.matrix(input())
result = initVector*(A**t)

_, cols = result.shape
L = [float(result[:,i]) for i in range(cols)]
print(L)
explode = (0.1, 0, 0, 0)
plt.pie(L,autopct='%1.2f%%', shadow=True, startangle=140)
plt.show()
