# # Documentazione Script Analisi Proporzioni e Prioritizzazione Problemi

# ## Descrizione dello Script

# Questo script esegue un'analisi delle proporzioni sui dati forniti in un file CSV e assegna priorità ai problemi basandosi sul numero di successi. Inoltre, garantisce che solo un massimo del 20% dei problemi possa essere classificato nella fascia di priorità più alta ('A'). I risultati dell'analisi vengono salvati in due file CSV.

# ## Funzionalità Principali

# 1. **Caricamento dei Dati**: Il file CSV contenente i dati viene caricato in un DataFrame pandas.
# 2. **Test di Proporzioni (Z-test)**: Vengono confrontate tutte le coppie di gruppi nel DataFrame utilizzando il test delle proporzioni per ottenere la statistica z e il valore p per ciascuna coppia.
# 3. **Calcolo dei Successi**: Per ciascun gruppo, viene calcolato il numero di successi (presenza di almeno un 1).
# 4. **Assegnazione delle Fasce di Gravità**: Le fasce di gravità vengono assegnate ai problemi in base al numero di successi, con un massimo del 20% dei problemi che possono essere nella fascia 'A'.
# 5. **Salvataggio dei Risultati**: I risultati dell'analisi e la lista dei problemi con le rispettive priorità vengono salvati in due file CSV.

# ## Utilizzo dello Script

# ### Prerequisiti

# - Python 3.x
# - Pandas
# - NumPy
# - Statsmodels

# ### Installazione delle Dipendenze

# Prima di eseguire lo script, assicurarsi di avere installato le dipendenze necessarie. È possibile installarle utilizzando pip:

# ```bash
# pip install pandas numpy statsmodels

import pandas as pd
import numpy as np
from itertools import combinations
from statsmodels.stats.proportion import proportions_ztest

# Carica il file CSV
file_path = 'dati.csv'
df = pd.read_csv(file_path)

# Lista dei nomi delle colonne (gruppi) da confrontare
gruppi = df.columns.tolist()

# Lista per memorizzare i risultati dei test tra tutte le coppie di gruppi
results = []

# Confronta tutte le coppie di gruppi
for g1, g2 in combinations(gruppi, 2):
    col1 = df[g1]
    col2 = df[g2]
    
    successes1 = col1.sum()
    successes2 = col2.sum()
    nobs1 = len(col1)
    nobs2 = len(col2)
    
    # Esegui il test di proporzioni (test z)
    count = np.array([successes1, successes2])
    nobs = np.array([nobs1, nobs2])
    z_stat, p_value = proportions_ztest(count, nobs)
    
    # Salva i risultati
    results.append((g1, g2, z_stat, p_value))

# Calcola il numero di successi per ciascun problema
successi_problemi = {gruppo: (df[gruppo] > 0).sum() for gruppo in gruppi}

# Calcola il numero massimo di problemi che possono essere nella fascia 'A' (20%)
max_A = int(0.2 * len(gruppi))

# Ordina i problemi per numero di successi (decrescente)
problemi_ordinati = sorted(successi_problemi.items(), key=lambda x: x[1], reverse=True)

# Assegna le fasce di gravità in base alle nuove regole e al limite del 20% per la fascia 'A'
fasce = {}
for i, (gruppo, successi) in enumerate(problemi_ordinati):
    if i < max_A and successi >= 2:
        fasce[gruppo] = 'A'
    elif successi >= 1:
        fasce[gruppo] = 'B'
    else:
        fasce[gruppo] = 'C'

# Crea una lista dei problemi con il conteggio delle fasce, mantenendo l'ordine originale
problemi_fasce = [
    (gruppo, successi_problemi[gruppo], fasce[gruppo])
    for gruppo in gruppi
]

# Crea un DataFrame per i risultati dei test di proporzioni
df_results = pd.DataFrame(results, columns=['Gruppo 1', 'Gruppo 2', 'Z-statistic', 'P-value'])

# Crea un DataFrame per i problemi con priorità
df_problemi = pd.DataFrame(problemi_fasce, columns=['Problema', 'Numero Segnalazioni', 'Fascia di Gravità'])

# Salva i risultati dei test di proporzioni in un file CSV
df_results.to_csv('risultati_test_proporzioni_TRAINLINE.csv', index=False)

# Salva la lista dei problemi con priorità in un file CSV
df_problemi.to_csv('problemi_priorita_TRAINLINE.csv', index=False)

print("File generati con successo:")
print("1. risultati_test_proporzioni.csv")
print("2. problemi_priorita.csv")
