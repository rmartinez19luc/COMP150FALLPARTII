import random

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

        