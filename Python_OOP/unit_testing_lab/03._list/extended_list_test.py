<<<<<<< HEAD
from extended_list import IntegerList
from unittest import TestCase, main


class IntegerListTests(TestCase):

    def test_init__when_args_are_int__expect_to_create_list_and_store_the_integer(self):
        list_integer = IntegerList(2, 3, 5, 10)
        self.assertEqual([2, 3, 5, 10], list_integer._IntegerList__data)

    def test_init__when_args_are_not_int__expect_to_not_add_args(self):
        list_integer = IntegerList("3", 5.6, 10.2)
        self.assertEqual([], list_integer._IntegerList__data)

    def test_add__when_element_is_int_expect_to_add_element(self):
        list_integer = IntegerList(2, 3, 5, 10)
        list_integer.add(17)
        self.assertEqual([2, 3, 5, 10, 17], list_integer._IntegerList__data)

    def test_add__when_element_is_not_int_expect_to_raise(self):
        list_integer = IntegerList(2, 3, 5, 10)
        with self.assertRaises(ValueError) as context:
            list_integer.add("15")
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_remove_index__when_index_is_valid__expect_to_remove_value_with_that_index(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 2
        index_value = list_integer._IntegerList__data[index]
        list_integer.remove_index(index)
        self.assertEqual(5, index_value)

    def test_remove_index__when_index_is_not_valid_negative__expect_to_raise(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = - 10
        with self.assertRaises(IndexError) as context:
            list_integer.remove_index(index)
        self.assertEqual("list index out of range", str(context.exception))

    def test_remove_index__when_index_is_not_valid_positive__expect_to_raise(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 10
        with self.assertRaises(IndexError) as context:
            list_integer.remove_index(index)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_get_when_index_is_in_range__expect_to_return_the_value_of_that_index(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 2
        index_value = list_integer._IntegerList__data[index]
        list_integer.get_data()[index]
        self.assertEqual(5, index_value)

    def test_get_when_index_is_not_in_range_negative__expect_to_raises(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = -10
        with self.assertRaises(IndexError) as context:
            list_integer.get_data()[index]
        self.assertEqual("list index out of range", str(context.exception))

    def test_get_when_index_is_not_in_range_positive__expect_to_raises(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 10
        with self.assertRaises(IndexError) as context:
            list_integer.get_data()[index]
        self.assertEqual("list index out of range", str(context.exception))

    def test_insert__when_index_and_value_are_valid__expect_to_insert_value_to_that_index(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 0
        value = 27
        list_integer.insert(index, value)
        self.assertEqual([27, 2, 3, 5, 10], list_integer._IntegerList__data)

    def test_insert__when_value_are_valid_index_not_valid_positive__expect_to_raise(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 10
        value = 27
        with self.assertRaises(IndexError) as context:
            list_integer.insert(index, value)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_insert__when_value_are_not_valid_and_index_is_valid__expect_to_raise(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 0
        value = "27"
        with self.assertRaises(ValueError) as context:
            list_integer.insert(index, value)
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_get_biggest__when_valid__expect_to_return_biggest_value(self):
        list_integer = IntegerList(2, 3, 5, 10)
        list_integer.get_biggest()
        self.assertEqual(10, list_integer.get_biggest())

    def test_get_index__when_valid__expect_to_return_index_of_that_value(self):
        list_integer = IntegerList(2, 3, 5, 10)
        value = 5
        list_integer.get_index(value)
        self.assertEqual(2, list_integer.get_index(value))


if __name__ == "__main__":
    main()
=======
from extended_list import IntegerList
from unittest import TestCase, main


class IntegerListTests(TestCase):

    def test_init__when_args_are_int__expect_to_create_list_and_store_the_integer(self):
        list_integer = IntegerList(2, 3, 5, 10)
        self.assertEqual([2, 3, 5, 10], list_integer._IntegerList__data)

    def test_init__when_args_are_not_int__expect_to_not_add_args(self):
        list_integer = IntegerList("3", 5.6, 10.2)
        self.assertEqual([], list_integer._IntegerList__data)

    def test_add__when_element_is_int_expect_to_add_element(self):
        list_integer = IntegerList(2, 3, 5, 10)
        list_integer.add(17)
        self.assertEqual([2, 3, 5, 10, 17], list_integer._IntegerList__data)

    def test_add__when_element_is_not_int_expect_to_raise(self):
        list_integer = IntegerList(2, 3, 5, 10)
        with self.assertRaises(ValueError) as context:
            list_integer.add("15")
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_remove_index__when_index_is_valid__expect_to_remove_value_with_that_index(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 2
        index_value = list_integer._IntegerList__data[index]
        list_integer.remove_index(index)
        self.assertEqual(5, index_value)

    def test_remove_index__when_index_is_not_valid_negative__expect_to_raise(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = - 10
        with self.assertRaises(IndexError) as context:
            list_integer.remove_index(index)
        self.assertEqual("list index out of range", str(context.exception))

    def test_remove_index__when_index_is_not_valid_positive__expect_to_raise(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 10
        with self.assertRaises(IndexError) as context:
            list_integer.remove_index(index)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_get_when_index_is_in_range__expect_to_return_the_value_of_that_index(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 2
        index_value = list_integer._IntegerList__data[index]
        list_integer.get_data()[index]
        self.assertEqual(5, index_value)

    def test_get_when_index_is_not_in_range_negative__expect_to_raises(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = -10
        with self.assertRaises(IndexError) as context:
            list_integer.get_data()[index]
        self.assertEqual("list index out of range", str(context.exception))

    def test_get_when_index_is_not_in_range_positive__expect_to_raises(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 10
        with self.assertRaises(IndexError) as context:
            list_integer.get_data()[index]
        self.assertEqual("list index out of range", str(context.exception))

    def test_insert__when_index_and_value_are_valid__expect_to_insert_value_to_that_index(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 0
        value = 27
        list_integer.insert(index, value)
        self.assertEqual([27, 2, 3, 5, 10], list_integer._IntegerList__data)

    def test_insert__when_value_are_valid_index_not_valid_positive__expect_to_raise(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 10
        value = 27
        with self.assertRaises(IndexError) as context:
            list_integer.insert(index, value)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_insert__when_value_are_not_valid_and_index_is_valid__expect_to_raise(self):
        list_integer = IntegerList(2, 3, 5, 10)
        index = 0
        value = "27"
        with self.assertRaises(ValueError) as context:
            list_integer.insert(index, value)
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_get_biggest__when_valid__expect_to_return_biggest_value(self):
        list_integer = IntegerList(2, 3, 5, 10)
        list_integer.get_biggest()
        self.assertEqual(10, list_integer.get_biggest())

    def test_get_index__when_valid__expect_to_return_index_of_that_value(self):
        list_integer = IntegerList(2, 3, 5, 10)
        value = 5
        list_integer.get_index(value)
        self.assertEqual(2, list_integer.get_index(value))


if __name__ == "__main__":
    main()
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
