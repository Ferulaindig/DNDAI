from typing import List, Optional

class Influencer:
    def __init__(self, description: str = "", affects: str = "", value: str = ""):
        self.description = description
        self.affects = affects
        self.value = value

class BodyPart:
    def __init__(self, condition: int, hp: int, hpmax: int, strength: int, influencers: Optional[List[Influencer]] = None):
        self.condition = condition
        self.hp = hp
        self.hpmax = hpmax
        self.strength = strength
        self.influencers = influencers if influencers is not None else []

class UpperBody:
    def __init__(self):
        self.head = BodyPart()
        self.left_arm = BodyPart()
        self.right_arm = BodyPart()
        self.left_hand = BodyPart()
        self.right_hand = BodyPart()

class LowerBody:
    def __init__(self):
        self.left_leg = BodyPart()
        self.right_leg = BodyPart()

class Torso:
    def __init__(self):
        self.liver = BodyPart()
        self.stomach = BodyPart()

class Body:
    def __init__(self):
        self.upper_body = UpperBody()
        self.lower_body = LowerBody()
        self.torso = Torso()

class Interaction:
    def __init__(self, timestamp: str = "", subjective: str = "", objective: str = "", impacts: str = "", value: str = ""):
        self.timestamp = timestamp
        self.subjective = subjective
        self.objective = objective
        self.impacts = impacts
        self.value = value

class Skill:
    def __init__(self, name: str = "", description: str = "", level: int = 0, category: str = ""):
        self.name = name
        self.description = description
        self.level = level
        self.category = category

class Memory:
    def __init__(self, timestamp: int, description: str = ""):
        self.timestamp = timestamp
        self.description = description

class Personality:
    def __init__(self, openness: int, conscientiousness: int, extraversion: int, agreeableness: int, neuroticism: int):
        self.openness = openness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism

class CoreBelief:
    def __init__(self, title: str = "", description: str = "", influence: str = ""):
        self.title = title
        self.description = description
        self.influence = influence

class Psyche:
    def __init__(self):
        self.personality = Personality()
        self.core_beliefs = []

class Character:
    def __init__(self, char_id: str = "", char_type: str = "", long_opinion: str = "", short_opinion: str = ""):
        self.char_id = char_id
        self.char_type = char_type
        self.long_opinion = long_opinion
        self.short_opinion = short_opinion
        self.interactions = []
        self.skills = []
        self.memories = []
        self.psyche = Psyche()
        self.body = Body()