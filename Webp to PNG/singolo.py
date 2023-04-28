import os
from PIL import Image
#Creato da M

# Chiedi all'utente il percorso del file da convertire
filepath = input("trascina qui il file da convertire: ")

# Estrai il nome del file dal percorso
filename = os.path.basename(filepath)

# Controlla che il file sia in formato webp
if not filename.endswith(".webp"):
    print("Il file deve essere in formato webp.")
else:
    # Apri l'immagine in formato webp
    with Image.open(filepath) as im:
        # Crea il nuovo nome del file con l'estensione png
        new_filename = os.path.splitext(filename)[0] + ".png"
        # Salva l'immagine in formato png
        im.save(new_filename)
        print("File convertito con successo!")
        print("Il file convertito si trova nella directory in cui si trova il programma")
        print()

input("Premi Invio per uscire.")