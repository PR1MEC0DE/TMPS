from domain.unit import Unit


class UnitBuilder:
    """Builder for constructing complex Unit objects with fluent interface"""
    
    def __init__(self):
        self.unit = Unit()
    
    def set_name(self, name):
        self.unit.name = name
        return self
    
    def set_unit_type(self, unit_type):
        self.unit.unit_type = unit_type
        return self
    
    def set_hp(self, hp):
        self.unit.hp = hp
        return self
    
    def set_damage(self, damage):
        self.unit.damage = damage
        return self
    
    def set_armor(self, armor):
        self.unit.armor = armor
        return self
    
    def set_range(self, range_val):
        self.unit.range = range_val
        return self
    
    def set_speed(self, speed):
        self.unit.speed = speed
        return self
    
    def set_ai_type(self, ai_type):
        self.unit.ai_type = ai_type
        return self
    
    def build(self):
        """Return the constructed Unit"""
        return self.unit
