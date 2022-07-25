from math import log

f = open("dictionary.txt")
words = [line.strip() for line in f.readlines()]
word_popular = dict((word, log(i + 1)) for i, word in enumerate(words))
max_word = max(len(x) for x in words)


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


print(infer_spaces("bergamotorcycle"))
