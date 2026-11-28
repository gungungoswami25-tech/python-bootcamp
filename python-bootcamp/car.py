
class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed = self.speed + amount
        print(self.brand, "speed:", self.speed)

    def brake(self, amount):
        self.speed = self.speed - amount

        if self.speed < 0:
            self.speed = 0

        print(self.brand, "speed:", self.speed)


car1 = Car("BMW")

car1.accelerate(50)
car1.accelerate(30)
car1.brake(20)
car1.brake(100)
