import model

def izpis_igre(kviz):
    return(
        f'Spregajte {kviz.glagol} v zapisani osebi: {kviz.oseba}\n'
    )

def vnos_besede():
    beseda = input('> ')
    if beseda.isalpha():
        return beseda
    else:
        print('Neveljaven vnos. Poskusite še enkrat:')
        return vnos_besede()

def izpis_zmage():
    return('Bravo!')

def izpis_poraza():
    return('Narobe!')


def zazeni_kviz():
    kviz = model.nova_igra()
    print('Pozdravljeni v kvizu iz italijanskih pravilnih glagolov!')

    print(izpis_igre(kviz))
    zapis = vnos_besede()
    stanje = kviz.preverba(zapis)
    if stanje == model.PRAVILNO:
        print(izpis_zmage())
    elif stanje == model.NAPACNO:
        print(izpis_poraza())
    else:
        print('Bwo')


zazeni_kviz()