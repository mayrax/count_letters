# conteggio parole di un messaggio con la funzione setDefault dei dizionari

messaggio = "le grigliate vegetariane sono cose furlane"
conteggio = {}

for lettera in messaggio:
	conteggio.setdefault(lettera,0)
	conteggio[lettera] = conteggio[lettera] + 1
print(conteggio)	
