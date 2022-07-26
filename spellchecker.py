from math import log


class SpellChecker:
    def __init__(self, path="dictionary.txt"):
        f = open(path, encoding='utf-8', newline='')
        self.words = [line.split()[0] for line in f.readlines()]
        self.word_cost = dict((word, log(i + 1)) for i, word in enumerate(self.words))
        self.max_word = max(len(x) for x in self.words)
        self.len_dict = dict([(i, []) for i in range(1, self.max_word + 1)])
        for w in self.words:
            self.len_dict[len(w)].append(w)
        f.close()

    @staticmethod
    def distance(a, b):
        """Расстояние Левенштейна между словами a и b"""

        n, m = len(a), len(b)
        if n > m:
            n, m = m, n
            a, b = b, a
        current_row = range(n + 1)  # 0 ряд - только вставки
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add = previous_row[j] + 1
                delete = current_row[j - 1] + 1
                change = previous_row[j - 1]
                if a[j - 1] != b[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)
        return current_row[n]

    def spell_check(self, s, num=9e999):
        """Исправление первых num орфографических ошибок в строке s"""

        result = s.split()
        old = s.split()
        found_all = [True] * len(result)
        for i in range(len(result)):
            found = False
            word = result[i]
            if word in self.words:
                continue
            result[i] = self.check_capitals(word)
            if result[i] != word:
                continue
            length = len(word)
            possible_length = [length, min(length + 1, self.max_word), max(length - 1, 1),
                               min(length + 2, self.max_word), max(length - 2, 1)]
            possible = ""
            for j in possible_length:
                for candidate in self.len_dict[j]:
                    dist = self.distance(word, candidate)
                    if dist == 1:
                        result[i] = candidate
                        num -= 1
                        found = True
                        break
                    elif dist == 2 and possible == "":
                        possible = candidate
                        continue
                if found:
                    break
            if not found:
                if possible:
                    result[i] = possible
                    num -= 1
                elif self.hyphen_to_space(result[i]):
                    result[i] = result[i].replace("-", " ")
                else:
                    result[i] = self.infer_spaces(result[i])
                    for new_w in result[i].split():
                        if new_w not in self.words:
                            result[i] = old[i]
                            found_all[i] = False
            if num <= 0:
                break
        self.fancy_print(result, old, found_all)
        return " ".join(result)

    def hyphen_to_space(self, s):
        """Проверка, является ли слово s несколькими словами, соединёнными лишним дефисом"""

        new_words = s.split("-")
        for word in new_words:
            if word not in self.words:
                return False
        return True

    def infer_spaces(self, s):
        """Подбор разделения слова s на несколько"""
        # Решение  @srikavineehari:
        # https://stackoverflow.com/questions/47730524/spell-check-and-return-the-corrected-term-in-python

        # Find the best match for the i first characters, assuming costity has
        # been built for the i-1 first characters.
        # Returns a pair (match_cost, match_length).
        def best_match(i):
            candidates = enumerate(reversed(cost[max(0, i - self.max_word):i]))
            return min((c + self.word_cost.get(s[i-k-1:i], 9e999), k+1) for k, c in candidates)

        # Build the cost array.
        cost = [0]
        for i in range(1, len(s) + 1):
            c, k = best_match(i)
            cost.append(c)

        # Backtrack to recover the most cost string.
        out = []
        i = len(s)
        while i > 0:
            c, k = best_match(i)
            assert c == cost[i]
            out.append(s[i-k:i])
            i -= k

        return " ".join(reversed(out))

    def check_capitals(self, word):
        """Проверка написания слова с заглавной буквы/полностью заглавными"""

        first_letter = word.replace(word[0], word[0].upper())
        if first_letter in self.words:
            return first_letter
        all_letters = word.upper()
        if all_letters in self.words:
            return first_letter
        return word

    @staticmethod
    def fancy_print(new, old, found_all):
        """Вывод результатов проверки орфографии"""

        print("Ваша строка: " + " ".join(old))
        print("Результат: " + " ".join(new))
        print()
        for i in range(len(new)):
            if new[i] != old[i]:
                print(old[i] + " -> " + new[i])
            elif not found_all[i]:
                print(old[i] + " -> " + "[замена не найдена]")
