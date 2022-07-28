import spellchecker


checker = spellchecker.SpellChecker()
print("Введите текст без знаков препинания и заглавных букв:")
s = input()
checker.spell_check(s)
