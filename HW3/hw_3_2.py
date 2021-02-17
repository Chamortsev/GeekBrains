word_in = str(input())

translate_words = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'досемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(n):
    if str.istitle(n):
        word = translate_words.get(n.lower())
        print(word.title())
    else:
        word = translate_words.get(n.lower())
        print(word)


num_translate_adv(word_in)
