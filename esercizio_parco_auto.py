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