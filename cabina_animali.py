from cabina import Cabina

class CabinaAnimali(Cabina):
    def __init__(self, codice, letti, ponte, prezzo_base, max_animali):
        super().__init__(codice, letti, ponte, prezzo_base)
        self.max_animali = int(max_animali)

    def prezzo_finale(self):
        return self.prezzo_base * (1 + 0.10 * self.max_animali)

    def __str__(self):
        stato = 'CAMERA DISPONIBILE' if self.disponibile else 'CAMERA OCCUPATA'

        return (f'{self.codice}: Animali | letti: {self.letti} - ponte: {self.ponte}'
                f'- prezzo: {self.prezzo_finale():.2f} euro - max animali: {self.max_animali} - {stato}')