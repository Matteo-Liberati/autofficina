def visualizza_veicoli():
    veicoli = [
        ("marca","modello","anno"),
        ("marca","modello","anno"),
        ("marca","modello","anno")
    ]
    
    
    for veicolo in veicoli:
        print(f"Marca: {veicolo[0][0]}, Modello: {veicolo[0][1]}, Anno: {veicolo[0][2]}")


def visualizza_assegnazioni():
    assegnazioni = [
        ("nome","marca","data"),
        ("nome","marca","data"),
        ("nome","marca","data")
    ]
    
    
    for assegnazione in assegnazioni():
        print(f"Nome: {assegnazione[0][0]}, Marca: {assegnazione[0][1]}, Data: {assegnazione[0][2]}")