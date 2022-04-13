<<<<<<< HEAD
from worker import Worker
import unittest


class WorkerTest(unittest.TestCase):
    valid_name = "Vlado 89"
    valid_salary = 1000
    valid_energy = 100
    money = 0

    def test_init__when_valid_name_salary_energy__expect_correctly_initialized(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        self.assertEqual(self.valid_name, worker.name)
        self.assertEqual(self.valid_salary, worker.salary)
        self.assertEqual(self.valid_energy, worker.energy)

    def test_rest__when_valid__expect_energy_to_be_incremented(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.rest()
        worker.rest()
        self.assertEqual(self.valid_energy + 2, worker.energy)

    def test_work__when_energy_is_0__expect_to_raise(self):
        worker = Worker(self.valid_name, self.valid_salary, 0)
        with self.assertRaises(Exception) as context:
            worker.work()

    def test_work__when_energy_is_negative__expect_to_raise(self):
        worker = Worker(self.valid_name, self.valid_salary, -1)
        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertEqual("Not enough energy.", str(context.exception))

    def test_work__when_energy_is_positive__expect_to_increase_money_by_salary(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.work()
        worker.work()
        self.assertEqual(self.money + self.valid_salary * 2, worker.money)

    def test_work__when_energy_is_positive__expect_to_decrease_energy(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.work()
        worker.work()
        self.assertEqual(self.valid_energy - 2, worker.energy)

    def test_get_info__when_valid__expect_str_with_correct_values(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.get_info()
        self.assertEqual(f'{self.valid_name} has saved {self.money} money.', worker.get_info())


if __name__ == '__main__':
    unittest.main()
=======
from worker import Worker
import unittest


class WorkerTest(unittest.TestCase):
    valid_name = "Vlado 89"
    valid_salary = 1000
    valid_energy = 100
    money = 0

    def test_init__when_valid_name_salary_energy__expect_correctly_initialized(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        self.assertEqual(self.valid_name, worker.name)
        self.assertEqual(self.valid_salary, worker.salary)
        self.assertEqual(self.valid_energy, worker.energy)

    def test_rest__when_valid__expect_energy_to_be_incremented(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.rest()
        worker.rest()
        self.assertEqual(self.valid_energy + 2, worker.energy)

    def test_work__when_energy_is_0__expect_to_raise(self):
        worker = Worker(self.valid_name, self.valid_salary, 0)
        with self.assertRaises(Exception) as context:
            worker.work()

    def test_work__when_energy_is_negative__expect_to_raise(self):
        worker = Worker(self.valid_name, self.valid_salary, -1)
        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertEqual("Not enough energy.", str(context.exception))

    def test_work__when_energy_is_positive__expect_to_increase_money_by_salary(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.work()
        worker.work()
        self.assertEqual(self.money + self.valid_salary * 2, worker.money)

    def test_work__when_energy_is_positive__expect_to_decrease_energy(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.work()
        worker.work()
        self.assertEqual(self.valid_energy - 2, worker.energy)

    def test_get_info__when_valid__expect_str_with_correct_values(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.get_info()
        self.assertEqual(f'{self.valid_name} has saved {self.money} money.', worker.get_info())


if __name__ == '__main__':
    unittest.main()
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
