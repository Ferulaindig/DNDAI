import Code.Creatures.CreaturePhysical as CreaturePhysical

class UpperBody:
    def __init__(self) -> None:
        self.head = CreaturePhysical.BodyPart()
        self.chest = CreaturePhysical.BodyPart()
        self.abdomen = CreaturePhysical.BodyPart()
        self.rightarm = CreaturePhysical.BodyPart()
        self.leftarm = CreaturePhysical.BodyPart()
        self.righthand = CreaturePhysical.BodyPart()
        self.lefthand = CreaturePhysical.BodyPart()

class LowerBody:
    def __init__(self) -> None:
        self.rightleg = CreaturePhysical.BodyPart()
        self.leftleg = CreaturePhysical.BodyPart()
        self.rightfoot = CreaturePhysical.BodyPart()
        self.leftfoot = CreaturePhysical.BodyPart()

class PhysicalBody:
    def __init__(self) -> None:
        self.upperbody = UpperBody()
        self.lowerbody = LowerBody()


class Human:
    def __init__(self, id: str, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname