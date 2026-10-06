# Solves: Spawn waves of identical units without rebuilding
from copy import deepcopy

class UnitRegistry:
    def __init__(self):
        self.templates = {}
    
    def register_template(self, key, unit):
        self.templates[key] = unit
    
    def clone_unit(self, template_key, new_name):
        original = self.templates[template_key]
        cloned = deepcopy(original)
        cloned.name = new_name
        cloned.hp = original.hp  # Reset stats
        return cloned

# Usage: Spawn 50 soldiers instantly
registry = UnitRegistry()
registry.register_template("soldier_template", soldier)

wave = [registry.clone_unit("soldier_template", f"Soldier-{i}") for i in range(50)]
