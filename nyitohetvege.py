#eredetiCim;magyarCim;bemutato;forgalmazo;bevel;latogato

naplopo = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def napszam(datum):
    ev  = int(datum[0:4])
    honap  = int(datum[5:7])
    nap = int(datum[8:])
    gyujto = 0
    for ho in range(1, honap):
        gyujto += naplopo[ho]
    gyujto += nap
    gyujto += (ev-2000) * 365
    return gyujto
         


class Mozi:
    def __init__(self, sor):
        sor = sor.strip().split(';')
        self.eredetiCim = sor[0]
        self.magyarCim  = sor[1]
        self.bemutato   = sor[2]
        self.forgalmazo = sor[3]
        self.bevel      = int(sor[4])
        self.latogato   = int(sor[5])
        



with open('nyitohetvege.txt', 'r', encoding='UTF-8') as f:
    fejlec = f.readline()
    lista = [Mozi(sor) for sor in f]
    
#3. feladat

print(f'3. feladat: {len(lista)}')

#4. feladat

bevetel = sum([sor.bevel for sor in lista if sor.forgalmazo == 'UIP'])

print(f'4. feladat: UIP Duna Film forgalmazó 1. hetes bevételeinek összege: {bevetel} Ft')

#5. feladat

latogato, sor = max([(sor.latogato, sor) for sor in lista ])
print(sor.eredetiCim, sor.magyarCim, sor.forgalmazo, sor.bevel, sor.latogato)

#6. feladat



for sor in lista:
    eredeticim = sor.eredetiCim.split()
    magyarcim  = sor.magyarCim.split()
#    print(eredeticim, magyarcim)
    eredetizaszlo = True
    for szo in eredeticim:
        if szo[0] not in ('W', 'w'):
            eredetizaszlo = False
#          print(eredeticim, szo, eredetizaszlo)
            break
        else:
            print('-----', szo, eredetizaszlo)
    magyarzaszlo  = True
    for szo in magyarcim:
        if szo[0] not in ('W', 'w'):
            magyarzaszlo = False
            break
        else:
            print('******', szo, magyarzaszlo)
    if eredetizaszlo and magyarzaszlo:
        print('Ilyen film volt!')
        break

# 7. feladat. stat.csv

forgalmazok = [sor.forgalmazo for sor in lista]

forgalmazok_halmaz = set(forgalmazok)

f = open('stat.csv', 'w', encoding='UTF-8')
print(f'forgalmazo;filmekSzama', file=f)

for forgalmazo in forgalmazok_halmaz:
    db = forgalmazok.count(forgalmazo)
    if db > 1:
        print(f'{forgalmazo};{db}', file=f)
f.close()



# 8. feladat.

bemutatok = [napszam(sor.bemutato) for sor in lista if sor.forgalmazo == 'InterCom']

dif = []

for i in range(len(bemutatok)-1):
    dif.append(bemutatok[i+1]-bemutatok[i])
print(max(dif))
        

    




