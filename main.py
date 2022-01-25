lista_zakupow = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'parzywniak': ['marchew', 'seler', 'rukola']
}

for i , j in lista_zakupow.items():
    print(f"Idę do {i.capitalize()} kupuję tu następujące rzeczy: {[x.capitalize() for x in j]} ")

print(f"W sumie kupuję {sum([len(lista_zakupow[i]) for i in lista_zakupow])} produktów.")

print(f"Zmiana tekstu")
