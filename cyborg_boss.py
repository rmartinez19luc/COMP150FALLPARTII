import random
import random

class CyborgBoss:
    def __init__(self, name="Cyborg Boss", health=120, attack_power=15):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.special_moves = [
            {"name": "Laser Beam", "damage": 20},
            {"name": "EMP Shock", "damage": 15, "effect": "stun"},
            {"name": "Repair Mode", "heal": 25}
        ]

    def attack(self):
        """Regular attack."""
        damage = random.randint(10, self.attack_power)
        print(f"{self.name} attacks for {damage} damage!")
        return damage

    def use_special_move(self):
        """Randomly uses a special move."""
        move = random.choice(self.special_moves)
        if "damage" in move:
            print(f"{self.name} uses {move['name']} for {move['damage']} damage!")
            return {"type": "damage", "value": move["damage"]}
        elif "heal" in move:
            print(f"{self.name} activates {move['name']} and heals for {move['heal']} health!")
            self.health += move["heal"]
            return {"type": "heal", "value": move["heal"]}

    def is_alive(self):
        """Check if the boss is still alive."""
        return self.health > 0

# Example usage
if __name__ == "__main__":
    # Create a Cyborg Boss instance
    boss = CyborgBoss()

    print(f"A wild {boss.name} appears!")
    print(f"{boss.name} has {boss.health} health and {boss.attack_power} attack power.")

    # Simulate the boss using a special move
    move_result = boss.use_special_move()

    if move_result["type"] == "damage":
        print(f"The boss inflicted {move_result['value']} damage.")
    elif move_result["type"] == "heal":
        print(f"The boss healed for {move_result['value']} health.")



def cyborg_boss_battle():
    print("/n=== Cyborg Boss Battle ===")
    print("A towering Cyborg Boss appears, ready to fight!")

    player_health = 100
    boss_health = 120

    while player_health > 0 and boss_health > 0:
      print(f"\nYour Health: {player_health}")
      print(f"Cyborg Boss Health: {boss_health}")

      print("\nChoose your action:")
      print("1. Attack")
      print("2. Defend")
      print("3. Run")

      action = input("Enter 1, 2, or 3: ")

      if action == "1":
        damage = random.randint(10, 20)
        print(f"You strike the Cyborg Boss for {damage} damage!")
        boss_health -= damage
      elif action == "2":
        print("You brace for the boss's attack")
      elif action == "3":
        print("You run away from the fight!")
        return
      else:
        print("Invalid action. You lose your turn!")

      if boss_health > 0:
        boss_damage = random.randint(5, 15)
        print(f"The Cyborg Boss strikes you for {boss_damage} damage!")
        player_health -= boss_damage

  if player_health > 0:
    print("\nYou defeated the Cyborg Boss!")
  else:
    print("\nThe Cyborg Boss defeated you!")

        