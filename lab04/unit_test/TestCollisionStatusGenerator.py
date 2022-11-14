import unittest

from CollisionStatusGenerator import CollisionStatusGenerator


class TestCollisionStatusGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.__collision_status_generator = CollisionStatusGenerator(0)

    def test_zero_collision(self):
        self.__collision_status_generator.set_collision_probability(0)
        self.assertEqual(self.__collision_status_generator.is_collision_occurred(), False)

    def test_collision_occurrence(self):
        self.__collision_status_generator.set_collision_probability(100)
        self.assertEqual(self.__collision_status_generator.is_collision_occurred(), True)


if __name__ == "__main__":
    unittest.main()
