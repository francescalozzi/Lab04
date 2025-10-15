from cabina import Cabina

class CabinaDeluxe(Cabina):
    def __init__(self, codice, letti, ponte, prezzo_base, stile):
        super().__init__(codice, letti, ponte, prezzo_base)
        self.stile = stile

    def prezzo_finale(self):
        return self.prezzo_base * 1.20

    def __str__(self):
        stato = 'CAMERA DISPONIBILE' if self.disponibile else 'CAMERA OCCUPATA'

        return (f'{self.codice}: Deluxe ({self.stile}) | letti: {self.letti}'
                f'- ponte: {self.ponte} - Prezzo {self.prezzo_finale():.2f} euro - {stato}')