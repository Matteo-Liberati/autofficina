from collections import Counter

# Classe per gestire i veicoli
class Veicolo:
    def __init__(self, id_veicolo, marca, modello, tipo, anno):
        self.id_veicolo = id_veicolo
        self.marca = marca
        self.modello = modello
        self.tipo = tipo
        self.anno = anno

# Classe per gestire i dipendenti
class Dipendente:
    def __init__(self, id_dipendente, nome, cognome, reparto):
        self.id_dipendente = id_dipendente
        self.nome = nome
        self.cognome = cognome
        self.reparto = reparto

# Classe per gestire le assegnazioni
class Assegnazione:
    def __init__(self, id_assegnazione, id_dipendente, id_veicolo):
        self.id_assegnazione = id_assegnazione
        self.id_dipendente = id_dipendente
        self.id_veicolo = id_veicolo

# Strutture per memorizzare veicoli, dipendenti e assegnazioni
veicoli = {}  # Dizionario con ID veicolo come chiave e oggetto Veicolo come valore
dipendenti = {}  # Dizionario con ID dipendente come chiave e oggetto Dipendente come valore
assegnazioni = []  # Lista di oggetti Assegnazione

# Funzione per aggiungere un nuovo veicolo
def aggiungi_veicolo(id_veicolo, marca, modello, tipo, anno):
    veicolo = Veicolo(id_veicolo, marca, modello, tipo, anno)
    veicoli[id_veicolo] = veicolo
    print(f"Veicolo {id_veicolo} aggiunto al parco auto.")

# Funzione per aggiungere un nuovo dipendente
def aggiungi_dipendente(id_dipendente, nome, cognome, reparto):
    dipendente = Dipendente(id_dipendente, nome, cognome, reparto)
    dipendenti[id_dipendente] = dipendente
    print(f"Dipendente {id_dipendente} aggiunto.")

# Funzione per assegnare un veicolo a un dipendente
def assegna_veicolo(id_assegnazione, id_dipendente, id_veicolo):
    if id_dipendente in dipendenti and id_veicolo in veicoli:
        assegnazione = Assegnazione(id_assegnazione, id_dipendente, id_veicolo)
        assegnazioni.append(assegnazione)
        print(f"Veicolo {id_veicolo} assegnato a {id_dipendente} con ID assegnazione {id_assegnazione}.")
    else:
        print("ID dipendente o veicolo non valido.")

# Funzione per visualizzare tutti i veicoli disponibili nel parco
def visualizza_veicoli():
    if veicoli:
        for id_veicolo, veicolo in veicoli.items():
            print(f"ID: {id_veicolo}, Marca: {veicolo.marca}, Modello: {veicolo.modello}, Tipo: {veicolo.tipo}, Anno: {veicolo.anno}")
    else:
        print("Nessun veicolo disponibile nel parco auto.")

# Funzione che visualizza tutte le assegnazioni effettuate
def visualizza_assegnazioni():
    if assegnazioni:
        for assegnazione in assegnazioni:
            print(f"ID Assegnazione: {assegnazione.id_assegnazione}, ID Dipendente: {assegnazione.id_dipendente}, ID Veicolo: {assegnazione.id_veicolo}")
    else:
        print("Nessuna assegnazione effettuata.")

# Funzione che visualizza tutti i veicoli assegnati a un dipendente specifico
def visualizza_veicoli_dipendente(id_dipendente):
    veicoli_assegnati = [assegnazione.id_veicolo for assegnazione in assegnazioni if assegnazione.id_dipendente == id_dipendente]
    if veicoli_assegnati:
        print(f"Veicoli assegnati al dipendente {id_dipendente}:")
        for id_veicolo in veicoli_assegnati:
            veicolo = veicoli[id_veicolo]
            print(f"ID: {id_veicolo}, Marca: {veicolo.marca}, Modello: {veicolo.modello}, Tipo: {veicolo.tipo}, Anno: {veicolo.anno}")
    else:
        print(f"Nessun veicolo assegnato al dipendente {id_dipendente}.")

# Rimuovere duplicati nel parco auto
def rimuovi_duplicati():
    veicoli_unici = {id_veicolo: info for id_veicolo, info in veicoli.items()}
    return veicoli_unici

# Contare il numero di veicoli per tipo
def conta_veicoli_per_tipo():
    tipi = [veicolo['tipo'] for veicolo in veicoli.values()]
    counter = Counter(tipi)
    for tipo, count in counter.items():
        print(f"{tipo}: {count} veicoli")

# Trovare il veicolo più utilizzato 
def veicolo_piu_utilizzato():
    contatore_veicoli = Counter([assegnazione['id_veicolo'] for assegnazione in assegnazioni])
    id_veicolo_piu_utilizzato = contatore_veicoli.most_common(1)[0][0]
    veicolo = veicoli[id_veicolo_piu_utilizzato]
    print(f"Il veicolo più utilizzato è {veicolo['marca']} {veicolo['modello']} ({veicolo['tipo']}, {veicolo['anno']})")

# Richiama la funzione e stampa
veicolo_piu_utilizzato()