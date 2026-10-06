# Solves: Complex Unit with many optional attributes
class UnitBuilder:
    def __init__(self):
        self.unit = Unit()
    
    def set_name(self, name):
        self.unit.name = name
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
    
    def set_ai_type(self, ai_type):
        self.unit.ai_type = ai_type
        return self
    
    def build(self):
        return self.unit

# Usage: Fluent, readable construction
elite_unit = (UnitBuilder()
    .set_name("Elite Infantry")
    .set_hp(150)
    .set_damage(45)
    .set_armor(20)
    .set_ai_type("aggressive")
    .build())
