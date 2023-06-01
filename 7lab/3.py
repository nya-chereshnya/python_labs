from abc import ABC, abstractmethod

class IShootable(ABC):
    @abstractmethod
    def aim(self):
        pass

    @abstractmethod
    def shoot(self):
        pass

    @abstractmethod
    def reload(self):
        pass

class Gun(IShootable):
    def __init__(self, stock):
        self.stock = stock

    def aim(self):
        print("Aiming the gun")

    def shoot(self):
        if self.stock > 0:
            print("Shooting")
            self.stock -= 1
        else:
            print("Out of stock")

    def reload(self):
        print("Reloading")
        self.stock = 10

    def get_stock(self):
        return self.stock

class Camera(IShootable):
    def __init__(self, stock):
        self.stock = stock

    def aim(self):
        print("Focusing the camera")

    def shoot(self):
        if self.stock > 0:
            print("Taking a photo")
            self.stock -= 1
        else:
            print("Out of stock")

    def reload(self):
        print("Replacing the memory card")
        self.stock = 32

    def get_stock(self):
        return self.stock
