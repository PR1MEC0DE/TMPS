from patterns.builder import UnitBuilder
from patterns.factory import InfantryFactory, ArmoredFactory, AirFactory
from patterns.prototype import UnitRegistry

def main():
    print("=" * 60)
    print("TMPS Lab 1: Creational Design Patterns Demo")
    print("Domain: Tactical Unit Simulation Engine")
    print("=" * 60)
    
    # ========== PATTERN 1: BUILDER ==========
    print("\n[PATTERN 1: BUILDER] - Complex Unit Construction")
    print("-" * 60)
    
    elite_sniper = (UnitBuilder()
        .set_name("Elite Sniper")
        .set_hp(80)
        .set_damage(80)
        .set_armor(5)
        .set_range(500)
        .set_ai_type("tactical")
        .build())
    
    print(f"Built: {elite_sniper}")
    
    # ========== PATTERN 2: FACTORY METHOD ==========
    print("\n[PATTERN 2: FACTORY METHOD] - Polymorphic Creation")
    print("-" * 60)
    
    infantry_factory = InfantryFactory()
    armored_factory = ArmoredFactory()
    air_factory = AirFactory()
    
    soldier = infantry_factory.create_unit("Private-1")
    tank = armored_factory.create_unit("Tank-Alpha")
    jet = air_factory.create_unit("Fighter-Jet-1")
    
    print(f"Infantry: {soldier}")
    print(f"Armored: {tank}")
    print(f"Air: {jet}")
    
    # ========== PATTERN 3: PROTOTYPE ==========
    print("\n[PATTERN 3: PROTOTYPE] - Runtime Cloning & Registry")
    print("-" * 60)
    
    registry = UnitRegistry()
    registry.register_template("soldier", soldier)
    registry.register_template("tank", tank)
    
    print("Spawning wave of 5 soldiers...")
    soldier_wave = [registry.clone_unit("soldier", f"Soldier-{i}") for i in range(1, 6)]
    for unit in soldier_wave:
        print(f"  - {unit}")
    
    print("\nSpawning wave of 3 tanks...")
    tank_wave = [registry.clone_unit("tank", f"Tank-{chr(64+i)}") for i in range(1, 4)]
    for unit in tank_wave:
        print(f"  - {unit}")
    
    # ========== INTEGRATED WORKFLOW ==========
    print("\n[INTEGRATED WORKFLOW] - All patterns working together")
    print("-" * 60)
    print("Scenario: Deploy a mixed force for mission")
    force = soldier_wave[:3] + tank_wave[:2] + [elite_sniper]
    print(f"Total units deployed: {len(force)}")
    for unit in force:
        print(f"  [{unit.unit_type}] {unit.name} - HP: {unit.hp}, DMG: {unit.damage}")

if __name__ == "__main__":
    main()
