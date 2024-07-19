import pandas as pd
from scipy.stats import chisquare
import logging

# Configura le loggate
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # Leggi il CSV
        df = pd.read_csv('TRENORD_.csv')
        logging.info(f"CSV letto correttamente con {df.shape[0]} righe e {df.shape[1]} colonne.")
    except Exception as e:
        logging.error(f"Errore durante la lettura del CSV: {e}")
        return

    # Inizializza una lista per salvare i risultati
    results = []

    # Esegui il test chi-quadro per ogni colonna
    for column in df.columns:
        try:
            # Conta le occorrenze di ciascun valore
            counts = df[column].value_counts().sort_index()

            # Aggiungi i valori mancanti come zero
            for i in range(5):
                if i not in counts:
                    counts.loc[i] = 0

            # Ordina i conteggi
            counts = counts.sort_index()

            # Esegui il test chi-quadro
            chi2, p = chisquare(counts)
            logging.info(f"Test chi-quadro per la colonna {column}: chi2={chi2}, p_value={p}")

            # Determina se il risultato è significativo
            is_significant = p < 0.05

            # Aggiungi i dettagli al risultato
            result_details = {
                'problema': column,
                'significativo': is_significant,
                'valori': counts.values.tolist(),
                'chi2': chi2,
                'p_value': p
            }
            results.append(result_details)
        except Exception as e:
            logging.error(f"Errore durante il test chi-quadro per la colonna {column}: {e}")

    # Converti i risultati in un DataFrame
    results_df = pd.DataFrame(results)
    results_df.to_csv('results_dettagliati.csv', index=False)

if __name__ == "__main__":
    main()
