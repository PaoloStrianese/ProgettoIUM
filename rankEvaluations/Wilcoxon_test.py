import pandas as pd
import os
from scipy.stats import wilcoxon

# Percorsi dei file CSV
file_path_trenord = 'trenord_final_data.csv'
file_path_trainline = 'trainline_final_data.csv'

# Leggi i dati dai file CSV
data_trenord = pd.read_csv(file_path_trenord, header=None)
data_trainline = pd.read_csv(file_path_trainline, header=None)

# Creazione della cartella per salvare il file CSV
tables_folder = 'tables'
os.makedirs(tables_folder, exist_ok=True)

# Lista per memorizzare i risultati del test di Wilcoxon
wilcoxon_results = []

# Itera attraverso ciascuna colonna e applica il test di Wilcoxon
num_columns = data_trenord.shape[1]

for i in range(num_columns):
    # Dati per Trenord e Trainline per la colonna specificata
    trenord_col_data = data_trenord[i].dropna()
    trainline_col_data = data_trainline[i].dropna()
    
    # Assicurati che entrambe le colonne abbiano la stessa lunghezza
    min_length = min(len(trenord_col_data), len(trainline_col_data))
    trenord_col_data = trenord_col_data[:min_length]
    trainline_col_data = trainline_col_data[:min_length]
    
    # Applica il test di Wilcoxon
    stat, p_value = wilcoxon(trenord_col_data, trainline_col_data)
    
    # Aggiungi i risultati alla lista, arrotondando i valori del p-value a quattro cifre decimali
    wilcoxon_results.append([f'Colonna {i+1}', round(stat, 4), round(p_value, 4)])

# Crea un DataFrame con i risultati
wilcoxon_df = pd.DataFrame(wilcoxon_results, columns=['Colonna', 'Statistiche', 'P-value'])

# Salva il DataFrame come CSV
wilcoxon_df.to_csv(os.path.join(tables_folder, 'wilcoxon_results.csv'), index=False)

print("I risultati del test di Wilcoxon sono stati salvati nel file 'wilcoxon_results.csv' nella cartella 'tables'.")
