import regex

dictionary = set([w for s in open("dictionary.txt", encoding='utf-8', newline='').readlines() for w in s.split()])

def add_words(collection):
    dict_file = open("dictionary.txt", 'w', encoding='utf-8')
    for word in collection:
        word_fixed = word.replace(regex.)
        if not(word in dictionary):
            dictionary.add(word)
            dict_file.write(word + "\n")
    dict_file.close()


print('Введите адрес файла')
file = open(input(), encoding='utf-8', newline='')
add_words(file.read().split())
