<<<<<<< HEAD
from cat import Cat
import unittest


class CatTests(unittest.TestCase):
    name = "Kitty"

    def test_eat__when_cat_eat__expect_increase_cat_size_by_one(self):
        cat = Cat(self.name)
        expected = cat.size + 1
        cat.eat()
        self.assertEqual(expected, cat.size)

    def test_eat__when_cat_is_hungry__expect_cat_to_be_fed(self):
        cat = Cat(self.name)

        cat.eat()
        self.assertTrue(cat.fed)

    def test_eat__when_cat_is_fed__expect_to_raise(self):
        cat = Cat(self.name)
        cat.eat()
        with self.assertRaises(Exception) as context:
            cat.eat()
        self.assertIsNotNone(context.exception)

    def test_sleep__when_cat_is_hungry__expect_to_raise(self):
        cat = Cat(self.name)
        with self.assertRaises(Exception) as context:
            cat.sleep()
        self.assertIsNotNone(context.exception)

    def test_sleep__when_cat_is_sleeping__expect_returns_true(self):
        cat = Cat(self.name)
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()
=======
from cat import Cat
import unittest


class CatTests(unittest.TestCase):
    name = "Kitty"

    def test_eat__when_cat_eat__expect_increase_cat_size_by_one(self):
        cat = Cat(self.name)
        expected = cat.size + 1
        cat.eat()
        self.assertEqual(expected, cat.size)

    def test_eat__when_cat_is_hungry__expect_cat_to_be_fed(self):
        cat = Cat(self.name)

        cat.eat()
        self.assertTrue(cat.fed)

    def test_eat__when_cat_is_fed__expect_to_raise(self):
        cat = Cat(self.name)
        cat.eat()
        with self.assertRaises(Exception) as context:
            cat.eat()
        self.assertIsNotNone(context.exception)

    def test_sleep__when_cat_is_hungry__expect_to_raise(self):
        cat = Cat(self.name)
        with self.assertRaises(Exception) as context:
            cat.sleep()
        self.assertIsNotNone(context.exception)

    def test_sleep__when_cat_is_sleeping__expect_returns_true(self):
        cat = Cat(self.name)
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
