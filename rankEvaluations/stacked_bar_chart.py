import matplotlib.pyplot as plt
import numpy as np

# Dati di esempio aggiornati
categories = ['Trenord', 'Trainline']
uomo = [17, 14]  # Numero di uomini per categoria
donna = [7, 4]  # Numero di donne per categoria
non_specificato = [2, 4]  # Numero di non specificati per categoria

# Calcolo delle percentuali
total = np.array(uomo) + np.array(donna) + np.array(non_specificato)
uomo_percent = np.array(uomo) / total * 100
donna_percent = np.array(donna) / total * 100
non_specificato_percent = np.array(non_specificato) / total * 100

# Posizione delle barre
barWidth = 0.5
r1 = np.arange(len(categories))

# Creazione del grafico a barre impilate
fig, ax = plt.subplots()
bars1 = plt.bar(r1, uomo_percent, color='#FF9999', edgecolor='white', width=barWidth, label='Alta')
bars2 = plt.bar(r1, donna_percent, bottom=uomo_percent, color='#66B2FF', edgecolor='white', width=barWidth, label='Media')
bars3 = plt.bar(r1, non_specificato_percent, bottom=uomo_percent + donna_percent, color='#99FF99', edgecolor='white', width=barWidth, label='Bassa')

# Aggiunta delle etichette con i valori assoluti sopra ciascun segmento
for i in range(len(r1)):
    plt.text(r1[i], uomo_percent[i] / 2, f'{uomo[i]}', ha='center', va='center', color='black', fontweight='bold')
    plt.text(r1[i], uomo_percent[i] + donna_percent[i] / 2, f'{donna[i]}', ha='center', va='center', color='black', fontweight='bold')
    plt.text(r1[i], uomo_percent[i] + donna_percent[i] + non_specificato_percent[i] / 2, f'{non_specificato[i]}', ha='center', va='center', color='black', fontweight='bold')

# Aggiunta di etichette e titolo
plt.xlabel('Categorie', fontweight='bold')
plt.ylabel('Percentuale', fontweight='bold')
plt.xticks(r1, categories)
plt.title('Grafico a Barre Impilate con Percentuali e Valori Assoluti')

# Aggiunta della legenda
plt.legend()

# Mostra il grafico
plt.show()
