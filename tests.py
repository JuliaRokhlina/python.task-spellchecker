import unittest
import spellchecker as sc


class GridTestMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spellchecker = sc.SpellChecker()

    def test_everything_correct(self):
        original = "всё правильно"
        expected = "всё правильно"
        self.assertEqual(self.spellchecker.spell_check(original), expected)

    def test_replace_letters(self):
        original = "обишка"
        expected = "ошибка"
        self.assertEqual(self.spellchecker.spell_check(original), expected)

    def test_wrong_letter(self):
        original = "ошибкб"
        expected = "ошибка"
        self.assertEqual(self.spellchecker.spell_check(original), expected)

    def test_extra_letter(self):
        original = "ошшибка"
        expected = "ошибка"
        self.assertEqual(self.spellchecker.spell_check(original), expected)

    def test_missing_letter(self):
        original = "ошбаетесь"
        expected = "ошибаетесь"
        self.assertEqual(self.spellchecker.spell_check(original), expected)

    def test_two_typos(self):
        original = "ошибаитес"
        expected = "ошибаетесь"
        self.assertEqual(self.spellchecker.spell_check(original), expected)

    def test_missing_spaces(self):
        original = "этонемноготруднее"
        expected = "это немного труднее"
        self.assertEqual(self.spellchecker.spell_check(original), expected)

    def test_extra_hyphen(self):
        original = "нечто-лишнее"
        expected = "нечто лишнее"
        self.assertEqual(self.spellchecker.spell_check(original), expected)

    def test_typo_with_hyphen(self):
        original = "что-та"
        expected = "что-то"
        self.assertEqual(self.spellchecker.spell_check(original), expected)

    def test_empty_string(self):
        original = ""
        expected = ""
        self.assertEqual(self.spellchecker.spell_check(original), expected)

    def test_not_fixable(self):
        original = "ъхврварпв ваопикц"
        expected = "ъхврварпв ваопикц"
        self.assertEqual(self.spellchecker.spell_check(original), expected)

    def test_first_n_typos(self):
        original = "нойти певые четырре ашибки страки"
        expected = "найти первые четыре ошибки страки"
        num = 4
        self.assertEqual(self.spellchecker.spell_check(original, num), expected)


if __name__ == '__main__':
    unittest.main()
