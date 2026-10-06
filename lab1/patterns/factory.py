from domain.unit import Unit, UnitType
from patterns.builder import UnitBuilder


class UnitFactory:
    """Abstract base factory for creating units"""
    def create_unit(self, name):
        raise NotImplementedError("Subclasses must implement create_unit()")


class InfantryFactory(UnitFactory):
    """Factory for creating Infantry units"""
    def create_unit(self, name):
        unit = (UnitBuilder()
            .set_name(name)
            .set_unit_type(UnitType.INFANTRY)
            .set_hp(100)
            .set_damage(30)
            .set_armor(10)
            .set_range(100)
            .set_speed(12)
            .set_ai_type("defensive")
            .build())
        return unit


class ArmoredFactory(UnitFactory):
    """Factory for creating Armored units"""
    def create_unit(self, name):
        unit = (UnitBuilder()
            .set_name(name)
            .set_unit_type(UnitType.ARMORED)
            .set_hp(200)
            .set_damage(50)
            .set_armor(40)
            .set_range(80)
            .set_speed(6)
            .set_ai_type("charge")
            .build())
        return unit


class AirFactory(UnitFactory):
    """Factory for creating Air units"""
    def create_unit(self, name):
        unit = (UnitBuilder()
            .set_name(name)
            .set_unit_type(UnitType.AIR)
            .set_hp(60)
            .set_damage(70)
            .set_armor(5)
            .set_range(300)
            .set_speed(25)
            .set_ai_type("tactical")
            .build())
        return unit
