import random

PRAVILNO = '+'
NAPACNO = '-'
osebe = ['IO', 'TU', 'LUI/LEI', 'NOI', 'VOI', 'LORO']

class Kviz:
    def __init__(self, glagol, oseba):
        self.glagol = glagol
        self.oseba = oseba

    def koren_glagola(self):
        return self.glagol[:-3]

    def koncnica_glagola(self):
        return self.glagol[-3:]

    def spregana_koncnica(self):
        koncnice = {
            'ARE': ['O', 'I', 'A', 'IAMO', 'ATE', 'ANO'],
            'ERE': ['O', 'I', 'E', 'IAMO', 'ETE', 'ONO'],
            'IRE': ['O', 'I', 'E', 'IAMO', 'ITE', 'ONO']
            }
        indeks = osebe.index(self.oseba)
        koncnica = koncnice[self.koncnica_glagola()][indeks]
        return koncnica

    def spregan_glagol(self):
        return self.koren_glagola() + self.spregana_koncnica()

    def preverba(self, beseda):
        beseda = beseda.upper()
        if beseda == self.spregan_glagol():
            return PRAVILNO
        else:
            return NAPACNO


with open('enostavni_pravilniglagoli.txt', encoding='utf-8') as datoteka:
    bazen_besed = [glagol.strip().upper() for glagol in datoteka]

def nova_igra():
    glagol = random.choice(bazen_besed)
    oseba = random.choice(osebe)
    return Kviz(glagol, oseba)