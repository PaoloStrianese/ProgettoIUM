import pandas as pd
import os

# Percorsi dei file CSV
file_path_trenord = 'trenord_final_data.csv'
file_path_trainline = 'trainline_final_data.csv'

# Leggi i dati dai file CSV
data_trenord = pd.read_csv(file_path_trenord, header=None)
data_trainline = pd.read_csv(file_path_trainline, header=None)

# Creazione della cartella per salvare il file CSV
tables_folder = 'tables'
os.makedirs(tables_folder, exist_ok=True)

# Lista per memorizzare i dati delle statistiche
stats_data = []

# Funzione per calcolare le statistiche
def get_stats(data, label):
    stats = data.describe()
    return [
        label,
        stats['min'],
        stats['25%'],
        stats['50%'],
        stats['75%'],
        stats['max'],
        round(stats['mean'], 2)  # Arrotonda la media a due cifre decimali
    ]

# Itera attraverso ciascuna colonna e raccogli le statistiche
num_columns = data_trenord.shape[1]

for i in range(num_columns):
    # Dati per Trenord e Trainline per la colonna specificata
    trenord_col_data = data_trenord[i]
    trainline_col_data = data_trainline[i]
    
    # Calcolo delle statistiche
    trenord_stats = get_stats(trenord_col_data, f'Colonna {i+1} - Trenord')
    trainline_stats = get_stats(trainline_col_data, f'Colonna {i+1} - Trainline')
    
    # Aggiungi le statistiche alla lista
    stats_data.append(trenord_stats)
    stats_data.append(trainline_stats)

# Crea un DataFrame con le statistiche
stats_df = pd.DataFrame(stats_data, columns=['Descrizione', 'Minimo', 'Primo quartile', 'Mediana', 'Terzo quartile', 'Massimo', 'Media'])

# Salva il DataFrame come CSV
stats_df.to_csv(os.path.join(tables_folder, 'statistiche.csv'), index=False)

print("Le statistiche sono state salvate nel file 'statistiche.csv' nella cartella 'tables'.")
