import unittest
from car import Car

car = Car(30)

class TestCarSideEffects(unittest.TestCase):

    def test_accelerate(self):
        car.accelerate()
        from time import sleep
        sleep(1)
        assert car.speed == 35

    def test_brake(self):
        car.brake()
        assert car.speed == 30

    def test_brake_again(self):
        car.brake()
        assert car.speed == 25

    def test_brake_another_time(self):
        car.brake()
        assert car.speed == 25
