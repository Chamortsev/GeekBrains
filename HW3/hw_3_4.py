names_catalog = {
    "А": {
        "П": "Петр Алексеев"
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}


def thesaurus_adv(*names):
    unic = []
    for i in sorted(names):
        detail = i.strip(' ').split(' ')
        surname = detail[1]
        letter = surname[0]
        if letter not in unic:
            unic.append(letter)
            print(names_catalog.fromkeys(letter, names_catalog.get(letter)))


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
