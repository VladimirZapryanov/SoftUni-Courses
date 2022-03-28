from unittest import TestCase, main
from mammal.project.mammal import Mammal


class MammalTest(TestCase):

    def test_init__when_valid__expect_to_be_initialized_correct(self):
        mammal = Mammal("Gosho", "dog", "woof")
        self.assertEqual("Gosho", mammal.name)
        self.assertEqual("dog", mammal.type)
        self.assertEqual("woof", mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound__when_valid__expect_to_return_str_with_animal_name_and_animal_sound(self):
        mammal = Mammal("Gosho", "dog", "woof")
        self.assertEqual(f"{mammal.name} makes {mammal.sound}", mammal.make_sound())

    def test_get_kingdom__when_valid__expect_to_return_str_with_kingdom(self):
        mammal = Mammal("Gosho", "dog", "woof")
        mammal_kingdom = mammal._Mammal__kingdom
        self.assertEqual(mammal_kingdom, mammal.get_kingdom())

    def test_info__when_valid_expect_to_return_str_with_animal_name_and_animal_type(self):
        mammal = Mammal("Gosho", "dog", "woof")
        self.assertEqual(f"{mammal.name} is of type {mammal.type}", mammal.info())


if __name__ == '__main__':
    main()
