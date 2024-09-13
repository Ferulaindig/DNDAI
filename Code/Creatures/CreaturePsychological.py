from typing import List, Dict

class Need:
    def __init__(self, title: str, description: str, maxsatisfaction: int, currentsatisfaction: int) -> None:
        self.title = title
        self.description = description
        self.maxsatisfaction = maxsatisfaction
        self.currentsatisfaction = currentsatisfaction

class Personality:
    def __init__(self, opennesstoexperience: int, conscientiousness: int, extraversion: int, agreeableness: int, neuroticism: int) -> None:
        self.opennesstoexperience = opennesstoexperience
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism

class CoreBelief:
    def __init__(self, title: str, description: str, influence: str) -> None:
        self.title = title
        self.description = description
        self.influence = influence

class Memory:
    def __init__(self, title: str, description: str, timestamp: int, expires: bool, expiration: int) -> None:
        self.title = title
        self.description = description
        self.timestamp = timestamp
        self.expires = expires
        self.expiration = expiration