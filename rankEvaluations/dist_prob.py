import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
import matplotlib.patches as mpatches

# Carica i dati dal file CSV
data = pd.read_csv('dist_euristiche.csv')

# Definisci l'ordine delle euristiche
euristiche_ordered = [
    'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10'
]

# Mapping delle euristiche ai gruppi
group_mapping = {
    'E1-E3': ['E1', 'E2', 'E3'],
    'E4-E7': ['E4', 'E5', 'E6', 'E7'],
    'E8-E10': ['E8', 'E9', 'E10']
}

# Conta le occorrenze di ciascuna euristica in ciascun gruppo
group_counts = OrderedDict([(euristica, 0) for euristica in euristiche_ordered])

for index, row in data.iterrows():
    heuristics = row['ID_EURISTICHE'].split(',')
    for heuristic in heuristics:
        heuristic = heuristic.strip()
        for group, members in group_mapping.items():
            if heuristic in members:
                group_counts[heuristic] += 1
                break

# Prepara i dati per il grafico
heuristics = list(group_counts.keys())
occurrences = list(group_counts.values())

# Definisci una lista di colori per i gruppi
colors = {
    'E1-E3': 'skyblue',
    'E4-E7': 'lightgreen',
    'E8-E10': 'salmon'
}

# Assegna colori in base al gruppo
bar_colors = [colors[group] for heuristic in heuristics for group, members in group_mapping.items() if heuristic in members]

# Plotting
fig, ax = plt.subplots()
bars = ax.bar(heuristics, occurrences, color=bar_colors)

# Aggiungi le etichette sui bar
for bar in bars:
    height = bar.get_height()
    ax.annotate('{}'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 punti di offset verticale
                textcoords="offset points",
                ha='center', va='bottom')

# Crea le voci della legenda per ogni gruppo
legend_patches = [
    mpatches.Patch(color=colors['E1-E3'], label='Percezione'),
    mpatches.Patch(color=colors['E4-E7'], label='Cognizione'),
    mpatches.Patch(color=colors['E8-E10'], label='Errore')
]

# Aggiungi la legenda al grafico
ax.legend(handles=legend_patches, title='Gruppi di Euristiche', loc='upper right', fancybox=True, shadow=True)

# Personalizza il grafico
ax.set_ylabel('Numero di Occorrenze')
ax.set_title('Occorrenze delle Euristiche Raggruppate')
ax.set_ylim(0, max(occurrences) * 1.1)
ax.set_xticklabels(heuristics, rotation=45, ha="right")

plt.tight_layout()
plt.show()
