class Wizard:
    def __init__(self, name: str, stamina: int, intelligence: int) -> None:
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    # don't touch above this line

    def get_fireballed(self, fireball_damage: int) -> None:
        fireball_damage -= self.__stamina
        self.health -= fireball_damage
        
    def drink_mana_potion(self, potion_mana: int) -> None:
        potion_mana += self.__intelligence
        self.mana += potion_mana
