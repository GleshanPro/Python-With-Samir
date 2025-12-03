from src.simulation.player import Player
from src.simulation.goose import Goose

from collections import UserDict

"""
ПЛОХО - наследовать от базовых типов

class CasinoBalance(dict): 
    ...
"""

# UserDict - определена нужная база (см. исходный код)
class CasinoBalance(UserDict):
    def __setitem__(self, key: str, value: int):
        print(f"[CasinoBalance] {key} balance -> {value}")
        super().__setitem__(key, value)
        
class GooseLedger(UserDict):
    def __setitem__(self, key: str, value: int):
        print(f"[GooseLedger] {key} balance -> {value}")
        super().__setitem__(key, value)
    

class Casino:
    def __init__(self, players: list[Player], ledger: GooseLedger | None) -> None:
        self.players: dict[str, Player] = {player.name: player for player in players}
        self.balances: CasinoBalance = CasinoBalance({player.name: player.balance for player in players})
        self.goose_ledger = ledger
        
    def register_goose(self, goose: Goose) -> None:
        if goose.name not in self.goose_ledger:
            self.goose_ledger[goose.name] = 0
            
    def steal_from_player(self, goose: Goose, player_name: str, amount: int) -> None:
        player = self.players[player_name]
        print(f"{goose.name} tries to steal {amount} from {player.name}")
        self.balances[player.name] -= amount
        self.goose_ledger[goose.name] = self.goose_ledger.get(goose.name, 0) + amount
        print(f"{goose.name} successfully stole {amount} from {player.name}.")
        
    def show_state(self) -> None:
        print('\n--- CASINO STATE ---')
        print("Players:")
        for name, bal in self.balances.items():
            print(f"    {name}: {bal}")
        print("Goose:")
        for name, bal in self.goose_ledger.items():
            print(f"    {name}: {bal}")
        print('==================\n')