from typing import List, Dict

class BodyModifier:
    def __init__(self, title: str, description: str, hpmod: int = 0, strmod: int = 0):
        """
        A body modifer for conditions which would lead to 
        permanent or temp modifcations to values of a body part
        hpmod is for Health point additions or reductions.
        strmod is for Strength point additions or reductions
        A positive or negative value is expected
        """
        self.title = title
        self.description = description
        self.hpmod = hpmod
        self.strmod = strmod

class BodyPart:
    def __init__(self, hp: int = 100, hpmax: int = 100, strength: int = 10) -> None:
        """
        hp is for Health Points
        hpmax is maximum health points a body part can have at optimal conditions
        strength is that body parts ability to exert it's specific influence
        modifiers is a list of conditions affecting the body part
        """
        self.hp = hp
        self.hpmax = hpmax
        self.strength = strength
        self.modifiers: Dict[str, BodyModifier] = {}

    def addmodifier(self, modifier: BodyModifier):
        """
        Adds a modifer to a BodyPart within a Dict titled modifiers
        """
        self.modifiers[modifier.title] = modifier

    def removemodifier(self, title: str):
        """
        Removes a modifier from the BodyPart.modifiers Dict
        """
        if title in self.modifiers:
            del self.modifiers[title]