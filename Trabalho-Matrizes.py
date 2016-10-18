#Uso do arquivo de input:
# Escreva APENAS os números
# Na primeira linha digite o número de iterações ex: 5
# Na segunda linha digite os valores do vetor de inicialização separados por espaço, utilize '.'(ponto) para separação decimal ex: 1.0 0.0
# Na terceira linha digite os valores da matriz de transição separados por espaço para as colunas.
# Utilize ';'(ponto e vírgula) para separação de linhas ex: 0.9 0.1; 0.5 0.5
# 0.9 0.1; 0.5 0.5 representa a matriz:
# [0.9 0.1]
# [0.5 0.5]

#from numpy import linalg as LA
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

t = int(input())
initVector = np.matrix(input())
A = np.matrix(input())
result = initVector*(A**t)

_, cols = result.shape
L = [float(result[:,i]) for i in range(cols)]
print(L)

#Gráfico de Barras
fig, ax = plt.subplots()
width = 0.5
ind = np.arange(len(L))

ax.set_title('Trabalho de PE')
ax.set_ylabel('Probabilidade')
ax.set_xlabel('Estado')
rects = ax.bar(ind,L,width,align="center")

ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
ax.set_xticks(ind)
for i in range(len(L)):
	# L[i] = ('%.2f' % L[i])
	# Changed to i, so now Row shows State number
	L[i] = i
ax.set_xticklabels (L)
plt.xlim([-1,len(L)])
plt.ylim([0,1.1])
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        
        ax.text(rect.get_x() + rect.get_width()/2, 1.05*height,'%1.2f%s' % (float(height*100),'%'),ha='center', va='bottom',fontsize=18)
autolabel(rects)

#Gráfico de Pizza
#plt.bar(L,autopct='%1.2f%%', shadow=True, startangle=140)
plt.show()
