import json
from attributes import *

haldir = Character('haldir')
self = haldir


class Character:
    def __init__(self, name, strength :int = None, dexterity :int = None, constitution :int = None, intelligence :int = None, wisdom :int = None, charisma :int = None):
        self.name = name
        with open('characters.json','r') as f:
            char_config = json.load(f)

        if self.name in char_config:
            attributes = char_config[self.name].get('attributes')
            self._set_attributes(**attributes)



    def _init_attributes(self, **attributes):
        raise NotImplementedError("Init attributes not implemented")

    def _get_attribute(self, attribute_values, Attribute_Holder):
        # print(Attribute_Holder.__name__)
        att = Attribute_Holder(
            **{k : _convert_to_subattribute(v) for k,v in attribute_values.items()}
        )
        return att

    def _set_attributes(self, **atributes):
        self.strength = self._get_attribute(attributes['strength'],Strength)
        self.dexterity = self._get_attribute(attributes['dexterity'],Dexterity)
        self.constitution = self._get_attribute(attributes['constitution'],Constitution)
        self.intelligence = self._get_attribute(attributes['intelligence'],Intelligence)
        self.wisdom = self._get_attribute(attributes['wisdom'],Wisdom)
        self.charisma = self._get_attribute(attributes['charisma'],Charisma)
