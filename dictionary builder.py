import regex as re

dictionary = set([w for s in open("dictionary.txt", encoding='utf-8', newline='').readlines() for w in s.split()])
special = re.compile("[,.?/…!\"\'*–();:«»1234567890\[\]]")


def add_words(collection):
    dict_file = open("dictionary.txt", 'a', encoding='utf-8')
    for word in collection:
        word_fixed = re.sub(special, "", word).lower()
        if word_fixed not in dictionary:
            dictionary.add(word_fixed)
            dict_file.write(word_fixed + "\n")
    dict_file.close()


print('Введите адрес файла:')
file = open(input(), encoding='utf-8', newline='')
add_words(file.read().split())
