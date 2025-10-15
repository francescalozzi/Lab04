import csv
from cabina import Cabina
from cabina_animali import CabinaAnimali
from cabina_deluxe import CabinaDeluxe
from passeggero import Passeggero


class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""

        self._nome = nome
        self._cabine = []
        self._passeggeri = []

    """Aggiungere setter e getter se necessari"""

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""

        try:
            with open(file_path, 'r', encoding='utf-8') as infile:
                reader = csv.reader(infile)
                for riga in reader:
                    if not riga:
                        continue  # in tale modo vengono ignorate le righe vuote

                    codice = riga[0].strip()

                    # preoccupiamoci ora delle CABINE

                    if codice.startswith('CAB'):
                        if len(riga) == 4:
                            letti = int(riga[1])
                            ponte = int(riga[2])
                            prezzo = float(riga[3])
                            cabina = Cabina(codice, letti, ponte, prezzo)

                        elif len(riga) == 5 and riga[4].strip().isdigit():
                            letti = int(riga[1])
                            ponte = int(riga[2])
                            prezzo = float(riga[3])
                            max_animali = int(riga[4])
                            cabina = CabinaAnimali(codice, letti, ponte, prezzo, max_animali)

                        elif len(riga) == 5 and riga[4].strip().isalpha():
                            letti = int(riga[1])
                            ponte = int(riga[2])
                            prezzo = float(riga[3])
                            stile = riga[4].strip()
                            cabina = CabinaDeluxe(codice, letti, ponte, prezzo, stile)

                        else:
                            raise ValueError(f'formato non riconosciuto per cabina {riga}')

                        self._cabine.append(cabina)

                    elif codice.startswith('P'):
                        if len(riga) != 3:
                            raise ValueError(f'formato non valido per passeggero: {riga}')

                        nome = riga[1].strip()
                        cognome = riga[2].strip()
                        passeggero = Passeggero(codice, nome, cognome)

                        self._passeggeri.append(passeggero)

                    else:
                        raise ValueError(f'roga non riconosicuta')

            print(f'I DATI SONO STATI CARICATI DA {file_path}')

        except FileNotFoundError:
            print(f'il file {file_path} non è stato trovato')

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""

        # CERCHIAMO LA CABINA
        cabina = None
        for cab in self._cabine:
            if cab.codice == codice_cabina:
                cabina = cab
                break

        if cabina is None:
            raise ValueError(f'la cabina {codice_cabina} non è stata trovata')

        # CERCHIAMO IL PASSEGGERO
        passeggero = None
        for p in self._passeggeri:
            if p.codice == codice_passeggero:
                passeggero = p
                break

        if passeggero is None:
            raise ValueError(f'il passeggero {codice_passeggero} non è stato trovato')

        # ORA CONTROLLIAMO LE VARIE DISPONIBILITA'

        if not cabina.disponibile:
            raise ValueError(f'la cabina {codice_cabina} è occupata')

        # con la notazione puntata accedo a unattributo dell'oggetto
        if passeggero.cabina is not None:
            raise ValueError(f'il passeggero {codice_passeggero} ha già una cabina')

        # ORA POSSIAMO ASSEGNARE
        cabina.disponibile = False  # è stata assegnata
        cabina.passeggero = passeggero
        passeggero.cabina = cabina

        print(f'{passeggero.nome} {passeggero.cognome} asseganto alla cabina {cabina.codice}')

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        if not self._cabine:
            print('NON CI SONO CABINE CARICATE')
            return []

        cabine_ordinate = sorted(self._cabine)
        print('\n CABINE ORDINATE IN BASE AL PREZZO')

        for cabina in cabine_ordinate:
            print(cabina)

        return cabine_ordinate

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        if not self._passeggeri:
            print('NON CI SONO PASSEGGERI CARICATI')
            return []

        print('\n ELENCO PASSEGGERI')
        for passeggero in self._passeggeri:
            print(passeggero)
        return None