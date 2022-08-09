
from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_heard()

    def create_heard(self):
        dino_1 = Dinosaur("", 0)
        dino_2 = Dinosaur("", 0)
        dino_3 = Dinosaur("", 0)
        self.dinosaurs.append(dino_1)
        self.dinosaurs.append(dino_2)
        self.dinosaurs.append(dino_3)
    
