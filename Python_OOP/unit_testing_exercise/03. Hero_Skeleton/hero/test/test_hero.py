from unittest import TestCase, main
from hero.project.hero import Hero


class HeroTests(TestCase):

    def test_init_when_valid__expect_to_be_initialized_correctly(self):
        hero = Hero("Hero1", 10, 100, 20)
        self.assertEqual("Hero1", hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(20, hero.damage)

    def test_str__when_valid__expect_str_with_hero_info(self):
        hero = Hero("Hero1", 10, 100, 20)
        self.assertEqual(f"Hero {hero.username}: {hero.level} lvl\n"f"Health: {hero.health}\n"f"Damage: {hero.damage}\n", hero.__str__())

    def test_battle__when_hero_one_name_is_the_same_with_hero_two_name__expect_to_raise(self):
        hero = Hero("Hero1", 10, 100, 20)
        hero_2 = Hero("Hero1", 10, 100, 20)
        with self.assertRaises(Exception) as context:
            hero.battle(hero_2)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_battle__when_hero_health_is_zero__expect_to_raise(self):
        hero = Hero("Hero1", 10, 0, 20)
        hero_2 = Hero("Hero2", 10, 100, 20)
        with self.assertRaises(ValueError) as context:
            hero.battle(hero_2)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_battle__when_hero_health_is_les_then_zero__expect_to_raise(self):
        hero = Hero("Hero1", 10, -10, 20)
        hero_2 = Hero("Hero2", 10, 100, 20)
        with self.assertRaises(ValueError) as context:
            hero.battle(hero_2)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_battle__when_enemy_health_is_zero__expect_to_raise(self):
        hero = Hero("Hero1", 10, 100, 20)
        hero_2 = Hero("Hero2", 10, 0, 20)
        with self.assertRaises(ValueError) as context:
            hero.battle(hero_2)
        self.assertEqual(f"You cannot fight {hero_2.username}. He needs to rest", str(context.exception))

    def test_battle__when_enemy_health_is_les_then_zero__expect_to_raise(self):
        hero = Hero("Hero1", 10, 100, 20)
        hero_2 = Hero("Hero2", 10, -10, 20)
        with self.assertRaises(ValueError) as context:
            hero.battle(hero_2)
        self.assertEqual(f"You cannot fight {hero_2.username}. He needs to rest", str(context.exception))

    def test_battle__when_both_heroes_died__expect_to_return_draw(self):
        hero = Hero("Hero1", 10, 100, 20)
        hero_2 = Hero("Hero2", 10, 100, 20)
        result = hero.battle(hero_2)
        self.assertEqual("Draw", result)

    def test_battle__when_you_win__expect_to_increase_your_skills_and_return_str(self):
        hero = Hero("Hero1", 10, 100, 20)
        hero_2 = Hero("Hero2", 1, 100, 1)
        result = hero.battle(hero_2)
        self.assertEqual(11, hero.level)
        self.assertEqual(104, hero.health)
        self.assertEqual(25, hero.damage)
        self.assertEqual("You win", result)

    def test_battle__when_you_lose__expect_to_increase_enemy_skills_and_return_str(self):
        hero = Hero("Hero1", 1, 100, 1)
        hero_2 = Hero("Hero2", 10, 100, 20)
        result = hero.battle(hero_2)
        self.assertEqual(11, hero_2.level)
        self.assertEqual(104, hero_2.health)
        self.assertEqual(25, hero_2.damage)
        self.assertEqual("You lose", result)


if __name__ == '__main__':
    main()
