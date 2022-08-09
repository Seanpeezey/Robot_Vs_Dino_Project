from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
        
    def create_fleet(self):
        robo_1 = Robot("")
        robo_2 = Robot("")
        robo_3 = Robot("")
        self.robots.append(robo_1)
        self.robots.append(robo_2)
        self.robots.append(robo_3)