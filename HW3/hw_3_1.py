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


def num_translate(n):
    word = translate_words.get(n.lower())
    print(word)


num_translate(word_in)
