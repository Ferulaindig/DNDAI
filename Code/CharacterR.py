from typing import List, Dict

class BodyModifier:
    def __init__(self, title: str, description: str = "", hpmod: int = 0, strmod: int = 0):
        self.title = title
        self.description = description
        self.hpmod = hpmod
        self.strmod = strmod

class BodyPart:
    def __init__(self, hp: int, hpmax: int, strength: int) -> None:
        self.hp = hp
        self.hpmax = hpmax
        self.strength = strength
        self.modifiers: Dict[str, BodyModifier] = {}

    def addmodifier(self, modifier: BodyModifier):
        self.modifiers[modifier.title] = modifier

    def removemodifier(self, title: str):
        if title in self.modifiers:
            del self.modifiers[title]