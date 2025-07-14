class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stop..")  

class Toyoto(Car):
    def __init__(self, name):
        self.name = name
        print(self.name)

class Fortuner(Toyoto):
    def __init__(self, name):
        self.name = name
        print(self.name)

car1 = Toyoto("Fortune") 
car1.name
car1.start()