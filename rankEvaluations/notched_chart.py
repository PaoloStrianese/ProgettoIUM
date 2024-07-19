import pandas as pd
import matplotlib.pyplot as plt
import os

# Lista delle coppie di parole
word_pairs = [
    ('incresioso', 'gradito'),
    ('incomprensibile', 'comprensibile'),
    ('creativo', 'privo di fantasia'),
    ('facile da capire', 'difficile da capire'),
    ('di grande valore', 'di poco valore'),
    ('noioso', 'appassionante'),
    ('non interessante', 'interessante'),
    ('imprevedibile', 'prevedibile'),
    ('veloce', 'lento'),
    ('originale', 'convenzionale'),
    ('ostruttiva', 'di supporto'),
    ('bene', 'male'),
    ('complicato', 'facile'),
    ('repellente', 'attraente'),
    ('usuale', 'moderno'),
    ('sgradevole', 'piacevole'),
    ('sicuro', 'insicuro'),
    ('attivante', 'soporifero'),
    ('aspettativo', 'non aspettativo'),
    ('inefficiente', 'efficiente'),
    ('chiaro', 'confuso'),
    ('non pragmatico', 'pragmatico'),
    ('ordinato', 'sovraccarico'),
    ('attrattivo', 'non attrattivo'),
    ('simpatico', 'antipatico'),
    ('conservativo', 'innovativo')
]

# Percorsi dei file CSV
file_path_trenord = 'trenord_final_data.csv'
file_path_trainline = 'trainline_final_data.csv'

# Leggi i dati dai file CSV
data_trenord = pd.read_csv(file_path_trenord, header=None, na_values=['NaN', ''])  # Gestione dei dati mancanti
data_trainline = pd.read_csv(file_path_trainline, header=None)

# Creazione della cartella per salvare i grafici
output_folder = 'charts'
os.makedirs(output_folder, exist_ok=True)

# Creazione del box plot per ciascuna colonna
num_columns = data_trenord.shape[1]

# Colori fissi per Trenord e Trainline
color_trenord = '#FF9999'  # Rosso chiaro
color_trainline = '#66B2FF'  # Blu chiaro

# Itera attraverso ciascuna colonna e crea un notched box plot per entrambe le app
for i in range(num_columns):
    # Imposta la dimensione della figura
    plt.figure(figsize=(12, 8))  # Larghezza 12 pollici, Altezza 8 pollici
    
    # Dati per Trenord e Trainline per la colonna i
    data = [data_trenord[i].dropna(), data_trainline[i]]  # Rimuove i dati mancanti da data_trenord
    labels = ['Trenord', 'Trainline']
    
    # Creazione del box plot con colori fissi e larghezza aumentata
    boxplot = plt.boxplot(data, notch=True, patch_artist=True, labels=labels, widths=0.5)
    
    # Assegna colori fissi ai boxplot
    boxplot['boxes'][0].set_facecolor(color_trenord)
    boxplot['boxes'][1].set_facecolor(color_trainline)
    
    # Titolo con la coppia di parole e il numero associato
    title = f"{word_pairs[i][0]}(1) - {word_pairs[i][1]}(7)"
    
    plt.title(f'Notched Box Plot per la Colonna {i + 1}: {title}', fontsize=18, fontweight='bold')
    plt.xlabel('App', fontsize=16)
    plt.ylabel('Valori', fontsize=16)
    
    # Salva il grafico
    plt.savefig(os.path.join(output_folder, f'notched_box_plot_colonna_{i + 1}.png'))
    plt.close()

print("I grafici sono stati salvati nella cartella 'charts'.")
