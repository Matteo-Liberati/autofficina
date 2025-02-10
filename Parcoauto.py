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