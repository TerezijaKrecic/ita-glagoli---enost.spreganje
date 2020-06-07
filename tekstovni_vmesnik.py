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
    return('Bravo!\n')

def izpis_poraza():
    return('Narobe! Poskusite še enkrat:')


def zazeni_kviz():
    print('Pozdravljeni v kvizu iz italijanskih pravilnih glagolov!')
    while True:
        kviz = model.nova_igra()
        print(50 * '=')
        print(izpis_igre(kviz))
        zapis = vnos_besede()
        stanje = kviz.preverba(zapis)
        while stanje != model.PRAVILNO:
            print(izpis_poraza())
            zapis = vnos_besede()
            stanje = kviz.preverba(zapis)
        print(izpis_zmage())



zazeni_kviz()