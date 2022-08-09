from dinosaur import Dinosaur
from weapon import Weapon

attack_one = Weapon('Rocket Punch', 35)
attack_two = Weapon('Rocket Kick', 65)
attack_three = Weapon('Lazer Beam', 95)
choice_of_attacks = [attack_one,attack_two,attack_three]

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = ''

    def choose_weapon(self):
        print(f'If you plan on fighting, you are going to need a weapon!')
        print(f'You have 3 choices. They are: Rocket Punch, Rocket Kick & Lazer Beam!')
        user_choice = input(f'Which of these 3 attacks would you like to use against your opponenet? ')
        print("")
        if user_choice == "Rocket Punch":
            choice_of_attacks[0]
        elif user_choice == "Rocket Kick":
            choice_of_attacks[1]
        elif user_choice == "Lazer Beam":
            choice_of_attacks[2]

    def attack(self,dinosaur):
        pass



        