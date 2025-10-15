class Passeggero:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.cabina = None  # sarà assegnata successivamente

    def __str__(self):
        if self.cabina:
            return f'{self.codice} : {self.nome} {self.cognome} - CABINA: {self.cabina.codice}'
        else:
            return f"{self.codice}: {self.nome} {self.cognome} - Nessuna cabina assegnata"

    def __eq__(self, altro):
        return self.codice == altro.codice