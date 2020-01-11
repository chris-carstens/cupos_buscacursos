import matplotlib.pyplot as plt
#from matplotlib.font_manager import FontProperties
from math import ceil
from Cupos import resultados, año, semestre
from banner import actual

size = 0.4
#font = FontProperties()
fig1 = plt.figure(f"Cupos {año}-{semestre}")
fig1.subplots_adjust(hspace=0.5, wspace=0.5)

#font.set_weight('bold')

lim_inf = 1 if len(resultados) < 4 else (2 if len(resultados) < 7 else (3 if len(resultados) < 10 else 4))
lim_sup = len(resultados) if lim_inf == 1 else (ceil(len(resultados) / 2) if lim_inf == 2 else (ceil(len(resultados) / 3) if lim_inf == 3 else ceil(len(resultados) / 4)))
for i, curso in enumerate(resultados):
        labels = 'Ocupadas: ' + str(int(curso['c_total']) - int(curso['c_disponible'])), 'Libres: ' + str(int(curso['c_disponible']))
        sizes = [int(curso['c_total']) - int(curso['c_disponible']), int(curso['c_disponible'])]
        ax = fig1.add_subplot(lim_inf, lim_sup, i+1)
        ax.pie(sizes, startangle=90, wedgeprops=dict(width=size, edgecolor='w'), textprops=dict())
        ax.legend(labels, loc=0, bbox_to_anchor=(1, 0, 0.5, 1))
        ax.text(0, 0, curso["sigla"] + "-" + curso["seccion"], ha='center')


plt.suptitle("Banner: " + actual)
#plt.tight_layout()
plt.savefig("Banner" + actual + ".png")
plt.show()
