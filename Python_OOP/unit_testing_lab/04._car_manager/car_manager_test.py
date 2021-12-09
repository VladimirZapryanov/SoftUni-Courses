from car_manager import Car
from unittest import TestCase, main


class CarManagerTests(TestCase):

    def test_init__when_params_are_valid__expect_valid_initialized(self):
        car = Car("Subaru", "Forester", 10, 100)
        self.assertEqual("Subaru", car.make)
        self.assertEqual("Forester", car.model)
        self.assertEqual(10, car.fuel_consumption)
        self.assertEqual(100, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_init__when_make_are_empty_or_none__expect_to_raise(self):
        with self.assertRaises(Exception) as context:
            car = Car("", "Forester", 10, 100)
        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_init__when_model_are_empty_or_none__expect_to_raise(self):
        with self.assertRaises(Exception) as context:
            car = Car("Subaru", "", 10, 100)
        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_init__when_fuel_consumption_are_zero_or_negative__expect_to_raise(self):
        with self.assertRaises(Exception) as context:
            car = Car("Subaru", "Forester", -10, 100)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_init__when_fuel_capacity__are_zero_or_negative__expect_to_raise(self):
        with self.assertRaises(Exception) as context:
            car = Car("Subaru", "Forester", 10, -50)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_refuel__when_valid__expect_to_increase_fuel_amount(self):
        car = Car("Subaru", "Forester", 10, 100)
        car.refuel(50)
        self.assertEqual(50, car.fuel_amount)

    def test_refuel__when_capacity_is_less_then_the_refuel__expect_to_increase_fuel_amount_to_fuel_capacity(self):
        car = Car("Subaru", "Forester", 10, 100)
        car.refuel(car.fuel_capacity * 2)
        self.assertEqual(100, car.fuel_amount)

    def test_refuel__when_we_refuel_with_negative_or_zero_amount__expect_to_raise(self):
        car = Car("Subaru", "Forester", 10, 100)
        with self.assertRaises(Exception) as context:
            car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_drive__when_fuel_is_enough__expect_to_decrease_fuel_amount(self):
        car = Car("Subaru", "Forester", 10, 100)
        car.refuel(100)
        car.drive(10)
        self.assertEqual(99, car.fuel_amount)

    def test_drive__when_fuel_is_not_enough__expect_to_raise(self):
        car = Car("Subaru", "Forester", 10, 100)
        car.refuel(10)
        with self.assertRaises(Exception) as context:
            car.drive(100000)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))


if __name__ == "__main__":
    main()


