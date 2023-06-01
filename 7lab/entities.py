from abc import ABC, abstractmethod


class Building(ABC):

    @abstractmethod
    def take_damage(self, damage): pass

    @abstractmethod
    def heal(self, amount): pass

    @abstractmethod
    def upgrade(self, player):
        pass

    @abstractmethod
    def HP(self): pass

    @abstractmethod
    def level(self): pass


class TownHall(Building):
    def __init__(self, current_health=1200, max_health=1200, armor=0, cost=1200, level=1):
        super().__init__()
        self._current_health = current_health
        self._max_health = max_health
        self._armor = armor
        self._cost = cost
        self._level = level

    def heal(self, amount):
        if self._current_health + amount > self._max_health:
            self._current_health = self._max_health
            return 1
        self._current_health += amount
        return 1

    def take_damage(self, damage):
        if damage < 0:
            return 0
        if self._current_health - damage < 0:
            self._current_health = 0
            return 1
        actual_damage = damage - self._armor
        if actual_damage > 0:
            self._current_health -= actual_damage
            return 1
        return 0

    def upgrade(self, player):
        if player.gold < self._cost:
            return 0
        player.gold -= self._cost
        self.__class__ = Keep
        self._cost = 2000
        self._current_health = 1400
        self._max_health = 1400
        self._level = 2
        return 1

    @property
    def level(self):
        return self._level

    @property
    def HP(self):
        return self._current_health


class Keep(TownHall):
    def __init__(self, current_health=1500, max_health=1500, armor=0, cost=2000, level=2):
        super().__init__()
        self._current_health = current_health
        self._max_health = max_health
        self._armor = armor
        self._cost = cost
        self._level = level

    def upgrade(self, player):
        if player.gold < self._cost:
            return 0
        player.gold -= self._cost
        self.__class__ = Castle
        self._cost = 2500
        self._current_health = 1600
        self._max_health = 1600
        self._level = 3
        return 1


class Castle(Keep):
    def __init__(self, current_health=2000, max_health=2000, armor=0, cost=2500, level=3):
        super().__init__()
        self._current_health = current_health
        self._max_health = max_health
        self._armor = armor
        self._cost = cost
        self._level = level

    def upgrade(self, player):
        return 0


class Player:
    def __init__(self, gold=0, units=None) -> None:
        self.gold = 0
        self.units = []

    def add_unit(self):
        self.units.append(TownHall())

    def delete_unit(self, id):
        try:
            self.units.pop(id)
        except IndexError:
            return 0

    def get_gold(self, amount=0):
        self.gold = min(self.gold + amount, 99999)
        return self.gold

    def deal_damage(self, unit, damage):
        self.units[unit].take_damage(damage)

    def buy_improvement(self, unit):
        self.units[unit].upgrade(self)

    def heal(self, unit, HP_amount):
        self.units[unit].heal(HP_amount)
