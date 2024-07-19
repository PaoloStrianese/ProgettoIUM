import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carica i dati da CSV
df = pd.read_csv('dati_matrice.csv')

# Espandi i valutatori in righe separate
df_expanded = df.set_index('ID').ID_VALUTATORI.str.split(', ', expand=True).stack().reset_index(level=1, drop=True).reset_index(name='ID_VALUTATORE')

# Crea la matrice problema valutatori
matrice_problema = df_expanded.pivot_table(index='ID_VALUTATORE', columns='ID', aggfunc=lambda x: 1, fill_value=0)

# Riordina le colonne in base ai valutatori
valutatori = ['EU1', 'EU2', 'ED1', 'ED2', 'ED3', 'ED4']
matrice_problema = matrice_problema.reindex(index=valutatori, fill_value=0)

# Crea la heatmap con linee tra le celle, colormap arancione e senza legenda
plt.figure(figsize=(14, 6))  # Aumenta la larghezza (x) e diminuisci l'altezza (y)
sns.heatmap(matrice_problema, cmap="Oranges", cbar=False, linewidths=1, linecolor='gray')
plt.title('Matrice Problema Valutatori')
plt.xlabel('ID Problema')
plt.ylabel('ID Valutatore')

# Salva e mostra l'immagine
plt.savefig('matrice_problema_valutatori.png')
plt.show()
