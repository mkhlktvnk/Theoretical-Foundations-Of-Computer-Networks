import random


class CollisionStatusGenerator:
    def __init__(self, collision_probability: int):
        self.__collision_probability = collision_probability

    def set_collision_probability(self, collision_probability):
        self.__collision_probability = collision_probability

    def is_collision_occurred(self) -> bool:
        weights = [self.__collision_probability / 100, 1 - (self.__collision_probability / 100)]
        return random.choices([True, False], weights)[0]
