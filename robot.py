from dinosaur import Dinosaur
from weapon import Weapon


attack_one = Weapon('Rocket Punch', 35)
attack_two = Weapon('Rocket Kick', 65)
attack_three = Weapon('Lazer Beam', 95)
attack_four = Weapon('Skip Turn', 0)


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = attack_one
    

    def choose_weapon(self):
        

        print(f'If you plan on winning, you are going to need a weapon!')
        print(f'You have 3 choices. They are: Rocket Punch(1), Rocket Kick(2) & Lazer Beam(3)! ' )
        user_choice = input(f'Which of these 3 attacks would you like to use against your opponenet? ')

        if user_choice == ("Rocket Punch",'1'):
            attack_one ==self.active_weapon
        elif user_choice == ("Rocket Kick",'2'):
            attack_two == self.active_weapon
        elif user_choice == ('3'):
            attack_three == self.active_weapon
        elif user_choice == ("Skip Turn", "4"):
            self.active_weapon==attack_four

    def attack(self,dinosaur):
        print(f'{self.name} attacked {dinosaur.name} with {self.active_weapon.name} and caused {self.active_weapon.attack_power}')
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{dinosaur.name} has {dinosaur.health} health!')
        print("")


        