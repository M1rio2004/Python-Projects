import random

# Restituisce una lista contenente i risultati di un lancio di dadi, dove abbiamo dadi
# numero di elementi impostati su valori selezionati casualmente tra 1 e il numero di lati dei dadi.
def dadi_roll(dadi, lati):
  
  # Iniziamo con una lista vuota
  roll = []
  
  # Creiamo un loop che eseguirà 'dadi' volte, per lanciare ogni dado. 
  # Usiamo il metodo randint() del modulo random per ottenere un intero casuale
  # tra 1 e lati, la 'faccia' del dado che è stato 'lanciato'. 
  # Quindi appendiamo questo nuovo risultato alla lista roll.
  for i in range(0, dadi):
    faccia = random.randint(1, lati)
    roll.append(faccia)
  
  # Restituiamo la lista completa dei risultati del lancio di dadi
  return roll

while True:
  # Chiediamo all'utente di inserire il numero di dadi da lanciare, convertiamo la stringa
  # inserita in un int e memorizziamo l'int nella variabile dadi
  dadi = int(input("Dadi: "))

  # Non possiamo lanciare i dadi se non c'è almeno un dado, quindi se l'intero dei dadi
  # è minore o uguale a zero stampiamo un messaggio di errore e continuamo con il loop
  if (dadi <= 0):
    print("Devi avere almeno un dado!")
    continue

  # Chiediamo all'utente di inserire il numero di lati per ogni dado, convertiamo la stringa
  # inserita in un int e memorizziamo l'int nella variabile lati
  lati = int(input("Lati: "))

  # Non possiamo lanciare un dado se non c'è almeno un lato, quindi se l'intero dei lati
  # è minore o uguale a zero stampiamo un messaggio di errore e continuamo con il loop
  if (lati <= 0):
    print("Devi avere almeno un lato!")
    continue

  # Eseguiamo il lancio di dadi utilizzando la funzione dice_roll(), passando i valori di dadi e
  # lati forniti dall'utente come argomenti, assegniamo la lista restituita a roll
  roll = dadi_roll(dadi, lati)

  # Stampiamo il risultato del lancio di dadi
  print(roll)

  # Chiediamo all'utente se vuole lanciare nuovamente i dadi
  risposta = input("Vuoi lanciare nuovamente i dadi? (y/n) ")
  
  # Se l'utente non inserisce 'y', usciamo dal loop e terminiamo il programma
  if risposta.lower() != "y":
    break
