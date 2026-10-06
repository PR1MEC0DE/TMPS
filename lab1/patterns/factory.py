# Solves: Create different unit types without hardcoding
class UnitFactory:
    def create_unit(self, unit_type):
        pass

class InfantryFactory(UnitFactory):
    def create_unit(self, name):
        return (UnitBuilder()
            .set_name(name)
            .set_hp(100)
            .set_damage(30)
            .set_armor(10)
            .set_ai_type("defensive")
            .build())

class ArmoredFactory(UnitFactory):
    def create_unit(self, name):
        return (UnitBuilder()
            .set_name(name)
            .set_hp(200)
            .set_damage(50)
            .set_armor(40)
            .set_ai_type("charge")
            .build())

# Usage: Client doesn't know concrete classes
factory = InfantryFactory()
soldier = factory.create_unit("Soldier-1")

factory = ArmoredFactory()
tank = factory.create_unit("Tank-1")
