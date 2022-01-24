lista_zakupow = {
    'Piekarnia': ['Chleb', 'Pączek', 'Bułki'],
    'Warzywniak': ['Marchew', 'Seler', 'Rukola']
}

ile_produktów = sum([len(lista_zakupow[i]) for i in lista_zakupow])

for i, j in lista_zakupow.items():
    print(f"Idę do {i} kupuję tu następujące rzeczy: {j} ")

print(f"W sumie kupuję {ile_produktów} produktów.")