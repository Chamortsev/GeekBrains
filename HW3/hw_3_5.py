from random import randrange

a = int(input('Использовать повторы? (0-нет 1- да)'))

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

nounsone = nouns.copy()
adverbsone = adverbs.copy()
adjectivesone = adjectives.copy()


def get_jokes(n, continuemetod):
    """
    Put numbers of Jokes in to function
    Function check continue metod (1- we can use all names in list, 0 - one name can use only one time)
    then  check len of first list if i less  take random word from first list and get it out from copy list.
    Then makes this procedure with the second and third lists. When list is empty print No Jokes.
     """
    if continuemetod == 1:
        for i in range(n):
            if i < len(nouns):
                first = nounsone[randrange(len(nounsone))]
                second = adverbsone[randrange(len(adverbsone))]
                third = adjectivesone[randrange(len(adjectivesone))]
                gf = nounsone.pop(nounsone.index(first))
                gs = adverbsone.pop(adverbsone.index(second))
                gt = adjectivesone.pop(adjectivesone.index(third))

                print(gf, gs, gt)
            else:
                print('Шутки кончились')
                break
    else:
        for i in range(n):
            if i < len(nouns):
                first = nounsone[randrange(len(nounsone))]
                second = adverbsone[randrange(len(adverbsone))]
                third = adjectivesone[randrange(len(adjectivesone))]

                print(first, second, third)


get_jokes(7, a)
