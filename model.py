import random

PRAVILNO = '+'
NAPACNO = '-'


class Kviz:
    def __init__(self, glagol, oseba):
        self.glagol = glagol
        self.oseba = oseba

    def koren_besede(self):
        return self.glagol[:-3]

    def koncnica_besede(self):
        return self.glagol[-3:]

    def spregana_koncnica(self):
        osebe = ['IO', 'TU', 'LUI/LEI', 'NOI', 'VOI', 'LORO']
        koncnice = {
            'ARE': ['O', 'I', 'A', 'IAMO', 'ATE', 'ANO'],
            'ERE': ['O', 'I', 'E', 'IAMO', 'ETE', 'ONO'],
            'IRE': ['O', 'I', 'E', 'IAMO', 'ITE', 'ONO']
            }
        indeks = osebe.index(self.oseba)
        koncnica = koncnice[self.koncnica_besede()][indeks]
        return koncnica

    def spregan_glagol(self):
        return self.koren_besede() + self.spregana_koncnica()

    def preverba(self, beseda):
        beseda = beseda.upper()
        if beseda == self.spregan_glagol():
            return PRAVILNO
        else:
            return NAPACNO


with open('enostavni_pravilniglagoli.txt', encoding='utf-8') as datoteka:
    bazen_besed = [glagol.strip().upper() for glagol in datoteka]

osebe = ['IO', 'TU', 'LUI/LEI', 'NOI', 'VOI', 'LORO']

def nova_igra():
    glagol = random.choice(bazen_besed)
    oseba = random.choice(osebe)
    return Kviz(glagol, oseba)