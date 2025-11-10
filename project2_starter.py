"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [D'ante Davis]
Date: [11/7/2025]

AI Usage: AI was used to help refine concepts such as to class structure,inheritance,and method overriding in Python.

"""


# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """

    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2

    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")

        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()

        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)

        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)

        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()

        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")


# ============================================================================
# CHARACTER CLASSES IMPLEMENTATION
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """

    def __init__(self, name, health, strength, magic):
        """
        Initialize a Character object.

        Parameters:
            name (str): Character's name.
            health (float): Character's starting health points.
            strength (float): Character's physical power.
            magic (float): Character's magical power.

        Returns:
            None
        """
        self.name = name  # Store character's name
        self.health = max(0, health)  # Ensure health is not negative
        self.strength = strength  # Store character's physical power
        self.magic = magic  # Store character's magical ability

    def attack(self, target):
        """
        Perform a basic attack on a target using strength.

        Parameters:
            target (Character): The character being attacked.

        Returns:
            None
        """
        damage = self.strength  # Base damage equal to strength
        target.take_damage(damage)  # Apply damage to target
        print(f"{self.name} attacks {target.name} for {damage} damage!")  # Display attack info

    def take_damage(self, damage):
        """
        Apply damage to the character, reducing health but not below zero.

        Parameters:
            damage (float): Amount of damage taken.

        Returns:
            None
        """
        if damage < 0:  # Ensure no negative damage
            damage = 0  # Convert negative to zero
        self.health = max(0, self.health - damage)  # Reduce health safely
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")  # Display health update

    def display_stats(self):
        """
        Display the character's current stats.

        Parameters:
            None

        Returns:
            None
        """
        print(f"Name: {self.name} | Health: {self.health} | Strength: {self.strength} | Magic: {self.magic}")  # Print stats


class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """

    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a Player object.

        Parameters:
            name (str): Player's name.
            character_class (str): Type of player (e.g., Warrior, Mage).
            health (float): Player's starting health.
            strength (float): Player's physical strength.
            magic (float): Player's magical power.

        Returns:
            None
        """
        super().__init__(name, health, strength, magic)  # Initialize from Character
        self.character_class = character_class  # Store player's class
        self.level = 1  # Start all players at level 1

    def display_stats(self):
        """
        Display the player's current stats, including class and level.

        Parameters:
            None

        Returns:
            None
        """
        super().display_stats()  # Call base class stats display
        print(f"Class: {self.character_class} | Level: {self.level}")  # Show player-specific info


class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """

    def __init__(self, name):
        """
        Initialize a Warrior object.

        Parameters:
            name (str): Warrior's name.

        Returns:
            None
        """
        super().__init__(name, "Warrior", 120, 15, 5)  # Initialize Warrior with specific stats

    def attack(self, target):
        """
        Perform a warrior-specific attack that deals extra physical damage.

        Parameters:
            target (Character): The character being attacked.

        Returns:
            None
        """
        damage = self.strength + 5  # Add bonus physical damage
        target.take_damage(damage)  # Apply damage to target
        print(f"{self.name} slashes {target.name} for {damage} damage!")  # Display attack info

    def power_strike(self, target):
        """
        Perform a powerful strike that deals heavy damage.

        Parameters:
            target (Character): The character being attacked.

        Returns:
            None
        """
        damage = self.strength * 1.5  # Multiply damage for power attack
        target.take_damage(damage)  # Apply powerful damage
        print(f"{self.name} uses Power Strike on {target.name} for {damage} damage!")  # Display special move info


class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """

    def __init__(self, name):
        """
        Initialize a Mage object.

        Parameters:
            name (str): Mage's name.

        Returns:
            None
        """
        super().__init__(name, "Mage", 80, 8, 20)  # Initialize Mage with stats

    def attack(self, target):
        """
        Perform a magic-based attack using the mage's power.

        Parameters:
            target (Character): The character being attacked.

        Returns:
            None
        """
        damage = self.magic * 0.8  # Calculate attack damage using magic
        target.take_damage(damage)  # Apply damage
        print(f"{self.name} casts a spell on {target.name} for {damage} damage!")  # Display spell info

    def fireball(self, target):
        """
        Cast a powerful fireball that deals increased magic damage.

        Parameters:
            target (Character): The character being attacked.

        Returns:
            None
        """
        damage = self.magic * 1.5  # Strong fireball damage
        target.take_damage(damage)  # Apply damage
        print(f"{self.name} hurls a fireball at {target.name} for {damage} damage!")  # Display fireball info


class Rogue(Player):
    """
    Rogue class - agile and stealthy fighter.
    Inherits from Player.
    """

    def __init__(self, name):
        """
        Initialize a Rogue object.

        Parameters:
            name (str): Rogue's name.

        Returns:
            None
        """
        super().__init__(name, "Rogue", 90, 12, 10)  # Initialize Rogue with balanced stats

    def attack(self, target):
        """
        Perform a rogue-specific attack that can critically strike.

        Parameters:
            target (Character): The character being attacked.

        Returns:
            None
        """
        damage = self.strength + (self.magic * 0.2)  # Base rogue attack mixes strength and magic
        if self.strength % 2 == 0:  # Deterministic "crit" based on even strength
            damage *= 1.5  # Critical hit multiplier
        target.take_damage(damage)  # Apply final damage
        print(f"{self.name} strikes {target.name} for {damage} damage!")  # Display attack info

    def sneak_attack(self, target):
        """
        Perform a sneak attack that always critically hits.

        Parameters:
            target (Character): The character being attacked.

        Returns:
            None
        """
        damage = (self.strength + self.magic) * 1.5  # Always critical sneak hit
        target.take_damage(damage)  # Apply damage
        print(f"{self.name} performs a Sneak Attack on {target.name} for {damage} damage!")  # Display sneak info


class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """

    def __init__(self, name, damage_bonus):
        """
        Initialize a Weapon object.

        Parameters:
            name (str): Weapon's name.
            damage_bonus (float): Additional damage bonus value.

        Returns:
            None
        """
        self.name = name  # Store weapon name
        self.damage_bonus = damage_bonus  # Store extra damage value

    def display_info(self):
        """
        Display information about the weapon.

        Parameters:
            None

        Returns:
            None
        """
        print(f"Weapon: {self.name} | Damage Bonus: {self.damage_bonus}")  # Show weapon info


# ============================================================================
# MAIN PROGRAM FOR MANUAL TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)

    # Create one of each character type
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")

    # Display their stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    # Test polymorphism - same method call, different behavior
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)

    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy health

    # Test special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)

    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)

    # Test composition with weapons
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)

    sword.display_info()
    staff.display_info()
    dagger.display_info()

    print("\n✅ Testing complete!")

