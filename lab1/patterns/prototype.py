from copy import deepcopy
from domain.unit import Unit


class UnitRegistry:
    """Registry for storing and cloning unit prototypes"""

    def __init__(self):
        self.templates = {}

    def register_template(self, key, unit):
        """Register a unit as a template for cloning"""
        self.templates[key] = unit

    def clone_unit(self, template_key, new_name):
        """Clone a registered template and give it a new name"""
        if template_key not in self.templates:
            raise ValueError(f"Template '{template_key}' not found in registry")

        original = self.templates[template_key]
        cloned = deepcopy(original)
        cloned.name = new_name
        return cloned

    def get_template(self, template_key):
        """Get a template without cloning"""
        return self.templates.get(template_key)

    def list_templates(self):
        """List all registered template keys"""
        return list(self.templates.keys())
