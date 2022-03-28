from unittest import TestCase, main
from vehicle.project.vehicle import Vehicle


class VehicleTests(TestCase):

    def test_init__when_valid__expect_to_be_initialized_correct(self):
        car = Vehicle(100, 150)

        self.assertEqual(100, car.fuel)
        self.assertEqual(100, car.capacity)
        self.assertEqual(150, car.horse_power)
        self.assertEqual(1.25, car.fuel_consumption)

    def test_drive__when_we_have_enough_fuel__expect_to_decrease_fuel(self):
        car = Vehicle(100, 150)
        car.drive(50)
        self.assertEqual(37.5, car.fuel)

    def test_drive__when_we_dont_have_enough_fuel__expect_to_raise(self):
        car = Vehicle(100, 150)
        with self.assertRaises(Exception) as context:
            car.drive(10000000000000)
        self.assertEqual("Not enough fuel", str(context.exception))

    def test_refuel__when_have_enough_capacity__expect_to_increase_fuel(self):
        car = Vehicle(100, 150)
        car.drive(50)
        car.refuel(10)
        self.assertEqual(47.5, car.fuel)

    def test_refuel__when_we_dont_have_enough_capacity__expect_to_raise(self):
        car = Vehicle(100, 150)
        with self.assertRaises(Exception) as context:
            car.refuel(10)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_str__when_valid__expect_to_return_info_about_car(self):
        car = Vehicle(100, 150)
        self.assertEqual(f"The vehicle has {car.horse_power} horse power with {car.fuel} fuel left and {car.fuel_consumption} fuel consumption", car.__str__())


if __name__ == '__main__':
    main()