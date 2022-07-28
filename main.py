import spellchecker


checker = spellchecker.SpellChecker()
print("Введите текст без знаков препинания и заглавных букв:")
s = input()
print("Введите, сколько первых ошибок найти (введите '-', если все)")
n = int(input())
checker.spell_check(s, n)
