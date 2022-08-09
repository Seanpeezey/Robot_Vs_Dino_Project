from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

dinosaur_one = Dinosaur('Rexxy', 30)
robot_one = Robot('Mr. Robato')

class Battlefield:
    def __init__(self):
        self.run_game()

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("")
        print('Welcome to Robot Vs. Dinosaur! The best battle simulator on the internet.')
        print("")

    def battle_phase(self):
        while dinosaur_one.health > 0 and robot_one.health > 0:
            robot_one.choose_weapon()
            robot_one.attack(dinosaur_one)
            dinosaur_one.attack(robot_one)
            if robot_one.health == 0 or dinosaur_one.health == 0:
             break    
        

    def display_winner(self):
        if robot_one.health <= 0:
            print(f'The factory who created {self.name} robot should be dissapointed! {dinosaur_one} Wins this battle!')
        elif dinosaur_one.health <= 0:
            print(f'I knew an overgrown lizard was no match for human technology! {robot_one.name} Wins!')