import json
from dataclasses import dataclass

@dataclass
class SubAttribute:
    value: int
    proficient: bool

@dataclass
class Attribute:
    value: int
    modifier: int
    saving_throw: SubAttribute

@dataclass
class Strength(Attribute):
    athletics: SubAttribute

@dataclass
class Dexterity(Attribute):
    acrobatics: SubAttribute
    sleight_of_hand: SubAttribute
    stealth: SubAttribute

@dataclass
class Constitution(Attribute):
    pass

@dataclass
class Intelligence(Attribute):
    arcana: SubAttribute
    history: SubAttribute
    investigation: SubAttribute
    nature: SubAttribute
    religion: SubAttribute

@dataclass
class Wisdom(Attribute):
    animal_handling: SubAttribute
    insight: SubAttribute
    medicine: SubAttribute
    perception: SubAttribute
    survival: SubAttribute

@dataclass
class Charisma(Attribute):
    deception: SubAttribute
    intimidation: SubAttribute
    performance: SubAttribute
    persuasion: SubAttribute


def _convert_to_subattribute(value):
    if type(value) == dict:
        return SubAttribute(**value)
    else:
        return value

# strength = attributes['strength']
# s = Strength(**{k : _convert_to_subattribute(v) for k,v in strength.items()})
# s
