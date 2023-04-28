import os
from PIL import Image
#Creato da M

# Specifica la cartella di origine e di destinazione
origin_folder = ".Webp"
destination_folder = "Png"

# Scorri tutti i file nella cartella di origine
for filename in os.listdir(origin_folder):
    # Controlla che il file sia in formato webp
    if filename.endswith(".webp"):
        # Costruisci il percorso del file di origine
        filepath = os.path.join(origin_folder, filename)
        # Apri l'immagine in formato webp
        with Image.open(filepath) as im:
            # Crea il nuovo percorso del file di destinazione con l'estensione png
            new_filepath = os.path.join(destination_folder, os.path.splitext(filename)[0] + ".png")
            # Salva l'immagine in formato png
            im.save(new_filepath)
            print("File convertiti con successo!")
            print()
input("Premi Invio per uscire.")