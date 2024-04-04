class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def double_speed(self):
        self.speed *= 2

warrior = Character(100, 10, 5)
mage = Character(80, 15, 7)

print(f"Warrior: {warrior}"),
print(f"Warrior's speed: {warrior.speed}")
print(f"Warrior's health: {warrior.health}")


warrior.double_speed()
print(f"Warrior's speed: {warrior.speed}")



#pylint: disable-all