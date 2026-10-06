# TMPS Lab 1: Creational Design Patterns

## Overview

This laboratory work demonstrates the implementation of **3 Creational Design Patterns** within a cohesive, real-world domain: **Tactical Unit Simulation Engine**.

The project simulates a strategy game or military simulation system where units are created, configured, and deployed. This domain naturally showcases how creational patterns solve practical problems.

## Domain: Tactical Unit Simulation Engine

### Problem Statement
In a tactical simulation or strategy game, we need to:
1. **Build** complex military units with many configurable attributes (HP, damage, armor, range, AI behavior, etc.)
2. **Create** different categories of units (Infantry, Armored, Air Support) without hardcoding their implementation details
3. **Spawn** waves of identical or slightly modified units at runtime without expensive reconstruction

### Solution: Three Complementary Creational Patterns

---

## Patterns Implemented

### 1. **Builder Pattern** - Complex Object Construction

**Purpose**: Simplify construction of complex objects with many optional parameters.

**When Used**: Building a fully configured `Unit` with dozens of optional attributes.

**Problem Solved**:
- Avoids "telescoping constructors" (constructors with many parameters)
- Provides fluent, readable API for object construction
- Allows step-by-step configuration

**Key Components**:
- `UnitBuilder`: Constructs `Unit` objects step-by-step
- `Unit`: Complex domain object being built

**Example**:
```python
elite_sniper = (UnitBuilder()
    .set_name("Elite Sniper")
    .set_hp(80)
    .set_damage(80)
    .set_armor(5)
    .set_range(500)
    .set_ai_type("tactical")
    .build())
