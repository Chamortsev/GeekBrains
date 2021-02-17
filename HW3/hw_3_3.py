names_catalog = {
    "И": ["Иван", "Илья"],
    "М": ["Мария", 'Михаил', 'Митрофан'],
    "П": ["Петр"],
    "А": ["Андрей", "Антон", "Алексей"]
}


def thesaurus(*names):
    unic = []
    for i in sorted(names):
        letter = i[0]
        if letter not in unic:
            unic.append(letter)
            print(names_catalog.fromkeys(letter, names_catalog.get(letter)))


thesaurus('Иван', 'Илья', 'Антон')
