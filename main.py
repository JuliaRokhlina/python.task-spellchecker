from math import log

f = open("dictionary.txt", encoding='utf-8', newline='')
words = [line.strip() for line in f.readlines()]
word_popular = dict((word, log(i + 1)) for i, word in enumerate(words))
max_word = max(len(x) for x in words)
len_dict = dict([(i, []) for i in range(1, max_word + 1)])
for w in words:
    if len(w) != 0:
        len_dict[len(w)].append(w)


def distance(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n
    current_row = range(n + 1)  # 0 ряд - только вставки
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]


def spell_check(s):
    result = s.split()
    old = s.split()
    for i in range(len(result)):
        found = False
        word = result[i]
        length = len(word)
        for j in range(max(length - 2, 1), min(length + 3, max_word)):
            for candidate in len_dict[j]:
                if distance(word, candidate) < 3:
                    result[i] = candidate
                    found = True
                    break
            if found:
                break
        if not found:
            result[i] = infer_spaces(result[i])
    fancy_print(result, old)


def fancy_print(new, old):
    print("Ваша строка: " + " ".join(old))
    print("Результат: " + " ".join(new))
    print()
    for i in range(len(new)):
        if new[i] != old[i]:
            print(old[i] + " -> " + new[i])


def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming popularity has
    # been built for the i-1 first characters.
    # Returns a pair (match_popular, match_length).
    def best_match(i):
        candidates = enumerate(reversed(popular[max(0, i - max_word):i]))
        return min((c + word_popular.get(s[i-k-1:i], 9e999), k+1) for k, c in candidates)

    # Build the popular array.
    popular = [0]
    for i in range(1, len(s) + 1):
        c, k = best_match(i)
        popular.append(c)

    # Backtrack to recover the most popular string.
    out = []
    i = len(s)
    while i > 0:
        c, k = best_match(i)
        assert c == popular[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))


spell_check('енутый блятб')
