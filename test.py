class Character:
    def __init__(self, health , damage , speed , weapon):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.weapon = None

    def get_boots(self):
        self.speed *= 1.5

    def get_potion(self):
        self.health *= 1.2
        self.damage *= 1.1

shadow = Character(85 , 55 , 68 , None)
shogun = Character(108 , 65 , 40 , None)

print(shadow.speed , shadow.damage , shadow.health)
print(shogun.speed , shogun.damage , shogun.health)

shadow.get_potion()
shogun.get_boots()

print(shadow.speed , shadow.damage , shadow.health)
print(shogun.speed , shogun.damage , shogun.health)