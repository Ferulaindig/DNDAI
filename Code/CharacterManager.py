from typing import Dict
from datetime import datetime
import Code.Creatures.Humanoids as Humanoid

class EntityManager:
    

    def __init__(self) -> None:
        self.humanoidsdict: Dict[str, Humanoid.Human] = {}

    def entityCreate(self, human: Humanoid.Human):
        humanid: str = datetime.now() + human.firstname + human.lastname
        self.humanoidsdict[humanid] = human

    def entityDestroy(self, idtodelete):
        if idtodelete in self.humanoidsdict:
            del self.humanoidsdict[idtodelete]