import tkinter as tk
import pytube
import os

# Crea la finestra principale
window = tk.Tk()
window.title("YT Downloader by M1rio2004")

# Crea una lista per memorizzare gli URL dei video scaricati
downloaded_videos = []

# Crea una funzione per scaricare il video quando si preme il pulsante
def download_video():
    # Prendi l'URL del video dall'input dell'utente
    video_url = url_input.get()

    # Utilizza la libreria pytube per ottenere il video
    yt = pytube.YouTube(video_url)

    # Seleziona il video con la qualità più alta disponibile
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    
    # Recupera il percorso della cartella corrente
    current_dir = os.getcwd()
    
    # Crea una cartella chiamata "download" nella cartella corrente, se non esiste già
    download_dir = os.path.join(current_dir, "Downloads")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Scarica il video nella cartella "download"
    video.download(download_dir)
    
    # Aggiungi il titolo del video scaricato alla lista
    downloaded_videos.append(yt.title)
    
    # Aggiorna la listbox con gli elementi della lista downloaded_videos
    update_history_listbox()
    
    # Mostra un messaggio di conferma
    confirm_label.config(text="Il video è stato scaricato con successo!")

# Crea un'etichetta per l'URL del video
url_label = tk.Label(text="Inserisci l'URL del video di YouTube:")
url_label.pack()

# Crea un'area di input per l'URL del video
url_input = tk.Entry()
url_input.pack()

# Crea un pulsante per avviare il download del video
download_button = tk.Button(text="Scarica video", command=download_video)
download_button.pack()

# Crea un'etichetta per mostrare il messaggio di conferma
confirm_label = tk.Label(text="")
confirm_label.pack()

# Crea una listbox per mostrare la cronologia dei video scaricati
history_listbox = tk.Listbox()
history_listbox.pack()

# Aggiorna la listbox con gli elementi della lista downloaded_videos
def update_history_listbox():
    history_listbox.delete(0, tk.END)
    for video in downloaded_videos:
        history_listbox.insert(tk.END, video)

# Crea un pulsante per aggiornare la listbox
update_button = tk.Button(text="Aggiorna cronologia", command=update_history_listbox)
update_button.pack()

# Avvia il loop principale dell'interfaccia grafica
window.mainloop()