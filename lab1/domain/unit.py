"""
Domain Model: Unit class for Tactical Simulation Engine
Represents a military unit with various configurable attributes.
"""

from enum import Enum
from copy import deepcopy


class UnitType(Enum):
    """Enumeration of different unit types"""
    INFANTRY = "Infantry"
    ARMORED = "Armored"
    AIR = "Air"
    SUPPORT = "Support"


class Unit:
    """
    Base Unit class representing a tactical unit in the simulation.
    
    Attributes:
        name (str): Unit identifier
        unit_type (UnitType): Category of unit
        hp (int): Hit points / Health
        damage (int): Damage output per attack
        armor (int): Defensive armor rating
        range (int): Attack range in units
        speed (int): Movement speed
        ai_type (str): AI behavior type (e.g., 'aggressive', 'defensive', 'tactical')
    """
    
    def __init__(self):
        self.name = "Unit"
        self.unit_type = UnitType.INFANTRY
        self.hp = 100
        self.damage = 30
        self.armor = 10
        self.range = 100
        self.speed = 10
        self.ai_type = "defensive"
    
    def __str__(self):
        return (f"[{self.unit_type.value}] {self.name} | "
                f"HP: {self.hp} | DMG: {self.damage} | "
                f"ARM: {self.armor} | RNG: {self.range} | "
                f"SPD: {self.speed} | AI: {self.ai_type}")
    
    def __repr__(self):
        return self.__str__()
    
    def take_damage(self, damage):
        """Calculate and apply damage after armor reduction"""
        actual_damage = max(1, damage - (self.armor // 2))
        self.hp -= actual_damage
        return actual_damage
    
    def is_alive(self):
        """Check if unit is still alive"""
        return self.hp > 0
    
    def clone(self):
        """Create a deep copy of this unit (for Prototype pattern)"""
        return deepcopy(self)
