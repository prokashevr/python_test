class Car:
    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self):
        self.speed += 55

    def brake(self):
        self.speed -= 5
