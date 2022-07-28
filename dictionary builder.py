import regex as re

dictionary = dict()
for line in open("dictionary.txt", encoding='utf-8', newline='').readlines():
    line_pair = line.split()
    if len(line_pair) == 2:
        dictionary[line_pair[0]] = int(line_pair[1])
special = re.compile("[,.?/…!\"\'*–—();:«»„“1234567890\[\]]")


def add_words(collection):
    dict_file = open("dictionary.txt", 'r+', encoding='utf-8')
    for word in collection:
        word_fixed = re.sub(special, "", word).lower()
        if word_fixed in dictionary:
            dictionary[word_fixed] += 1
        else:
            dictionary[word_fixed] = 1
    for pair in sorted(dictionary.items(), key=lambda item: -item[1]):
        dict_file.write(pair[0] + " " + str(pair[1]) + "\n")
    dict_file.close()


print('Введите адрес файла:')
file = open(input(), encoding='utf-8', newline='')
add_words(file.read().split())
