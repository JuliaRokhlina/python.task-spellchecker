import spellchecker


checker = spellchecker.SpellChecker()
print("Введите текст без знаков препинания:")
s = input()
print("Введите, сколько первых ошибок найти (введите '-', если все)")
n = input()
int_n = 9e999 if n == "-" else int(n)
checker.spell_check(s, int_n)
