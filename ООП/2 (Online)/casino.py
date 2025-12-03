import random

class Player:
    hp: int = 100
    balance: int = 1000
    age: int
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def dep(self, amount: int, bet: int):
        difference = Casino.bet(amount, bet)
        self.balance += difference
        

class Goose(Player):    
    stamina: float = 100
    speed: float
    honk_volume: int
    
    def __init__(self, name, speed, honk_volume):
        self.name = name
        self.speed = speed
        self.honk_volume = honk_volume
        
    def attack(self, player: Player):
        ...
        
    def honk(self):
        ...
        
        
class Casino:
    budget: int = 1_000_000
    players: list[Player]
    gooses: list[Goose]
    
    @classmethod
    def bet(cls, amount, bet):
        result = random.randint(1, 10)
        difference = 0
        if bet == result:
            difference += amount * 2
        else:
            difference -= amount
        cls.budget -= difference
        return difference
    
    def take_money(self, amount):
        ...
        
    def clash_with_goose(self, health, player_name, goose_name):
        ...
    
    