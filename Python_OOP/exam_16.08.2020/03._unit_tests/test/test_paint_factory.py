from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(TestCase):
    def test_init__when_valid__expect_to_be_initialized_correctly(self):
        pf = PaintFactory("Name", 15)
        self.assertEqual("Name", pf.name)
        self.assertEqual(15, pf.capacity)
        self.assertEqual({}, pf.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], pf.valid_ingredients)

    def test_add_ingredient__when_product_type_and_quantity_is_valid__expect_to_add_product_and_his_quantity(self):
        pf = PaintFactory("Name", 15)
        pf.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, pf.ingredients)
        pf.add_ingredient("white", 2)
        self.assertEqual({"white": 4}, pf.ingredients)
        pf.add_ingredient("red", 5)
        pf.add_ingredient("white", 6)
        self.assertEqual({"white": 10, "red": 5}, pf.ingredients)

    def test_add_ingredient__when_capacity_is_full__expect_to_raises(self):
        pf = PaintFactory("Name", 15)
        pf.add_ingredient("white", 2)
        with self.assertRaises(ValueError) as context:
            pf.add_ingredient("white", 15)
        self.assertEqual("Not enough space in factory", str(context.exception))

    def test_add_ingredient__when_product_type_is_not_valid__expect_to_raises(self):
        pf = PaintFactory("Name", 15)
        pf.add_ingredient("white", 2)
        with self.assertRaises(TypeError) as context:
            product_type = "black"
            pf.add_ingredient(product_type, 3)
        self.assertEqual(f"Ingredient of type {product_type} not allowed in {pf.__class__.__name__}", str(context.exception))

    def test_remove_ingredient__when_product_type_and_quantity_is_valid__expect_to_decrease_product_quantity(self):
        pf = PaintFactory("Name", 15)
        pf.add_ingredient("white", 10)
        pf.add_ingredient("red", 5)
        pf.remove_ingredient("red", 3)
        self.assertEqual({"white": 10, "red": 2}, pf.ingredients)
        pf.remove_ingredient("white", 10)
        self.assertEqual({"white": 0, "red": 2}, pf.ingredients)

    def test_remove_ingredient__when_quantity_is_more_of_what_we_have__expect_to_raises(self):
        pf = PaintFactory("Name", 15)
        pf.add_ingredient("white", 10)
        with self.assertRaises(ValueError) as context:
            pf.remove_ingredient("white", 20)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))

    def test_remove_ingredient__when_product_type_not_valid__expect_to_raises(self):
        pf = PaintFactory("Name", 15)
        pf.add_ingredient("white", 10)
        with self.assertRaises(KeyError) as context:
            pf.remove_ingredient("black", 20)
        self.assertEqual("'No such ingredient in the factory'", str(context.exception))

    def test_products__when_valid__expect_to_return_dict_with_all_ingredients_and_quantity(self):
        pf = PaintFactory("Name", 15)
        pf.add_ingredient("white", 10)
        pf.add_ingredient("red", 5)

        self.assertDictEqual(pf.products, pf.ingredients)

    def test_repr__when_valid__expect_to_return_repr_info(self):
        pf = PaintFactory("Name", 15)
        pf.add_ingredient("white", 10)
        pf.add_ingredient("red", 5)
        result = ""
        result += f"Factory name: {pf.name} with capacity {pf.capacity}.\n"
        for ingredient in pf.ingredients:
            result += f"{ingredient}: {pf.ingredients[ingredient]}\n"
        self.assertEqual(result, pf.__repr__())

    def test_can_add__when_value_is_les_then_capacity__expect_to_return_true(self):
        pf = PaintFactory("Name", 15)
        pf.add_ingredient("white", 2)
        pf.add_ingredient("red", 2)
        self.assertTrue(pf.capacity - sum(pf.ingredients.values()) - 11 >= 0)

    def test_can_add__when_value_is_more_then_capacity__expect_to_return_false(self):
        pf = PaintFactory("Name", 15)
        pf.add_ingredient("white", 2)
        pf.add_ingredient("red", 2)
        self.assertFalse(pf.capacity - sum(pf.ingredients.values()) - 20 >= 0)

    def test_abstract_method_checking(self):
        self.assertTrue('add_ingredient' in dir(PaintFactory))
        self.assertTrue('remove_ingredient' in dir(PaintFactory))
        self.assertTrue('__init__' in dir(PaintFactory))


if __name__ == '__main__':
    main()
