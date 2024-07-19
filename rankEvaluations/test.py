import pandas as pd
import numpy as np

# Leggere i dati dal file CSV
df = pd.read_csv('TRAINLINE_.csv')

# Calcolare la media e la deviazione standard per ciascuna colonna (PLINE1 - PLINE18)
df_mean = df.mean()
df_std = df.std()

# Calcolare la mediana per ciascuna colonna (PLINE1 - PLINE18)
df_median = df.median()

# Calcolare l'IQR per ciascuna colonna (PLINE1 - PLINE18)
df_iqr = df.apply(lambda x: np.percentile(x, 75) - np.percentile(x, 25))

# Creare un DataFrame per i risultati
df_results = pd.DataFrame({
    'Line': df.columns[1:],  # Escludiamo la prima colonna 'Problem'
    'Mean': df_mean.values[1:],
    'StdDev': df_std.values[1:],
    'Median': df_median.values[1:],
    'IQR': df_iqr.values[1:]
})

# Salvare i risultati in un nuovo file CSV
df_results.to_csv('results.csv', index=False)

print("I risultati sono stati salvati in 'results.csv'")
