class Cabina:
    def __init__(self, codice, letti, ponte, prezzo_base):
        self.codice = codice
        self.letti = int(letti)
        self.ponte = int(ponte)
        self.prezzo_base = float(prezzo_base)
        self.disponibile = True
        self.passeggero = None  # viene inizializzato come vuoto

    def prezzo_finale(self):
        return self.prezzo_base

    def __str__(self):
        # inserisco uno stato della camera che permetta al cliente di
        # vedere se la cabina è libera o occupata

        stato = 'CAMERA DISPONIBILE' if self.disponibile else 'CAMERA OCCUPATA'

        return f'{self.codice}: Standard | letti: {self.letti} - ponte: {self.ponte} - prezzo: {self.prezzo_finale():.2f} euro - {stato}'

    def __lt__(self, altro):
        return self.prezzo_finale() < altro.prezzo_finale()

    # imponiamo che due cabine siano uguali se hanno lo stesso codice

    def __eq__(self, altro):
        return self.codice == altro.codice