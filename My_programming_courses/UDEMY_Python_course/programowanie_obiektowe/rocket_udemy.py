from random import randint
import re
import numpy as np


class Rocket:
    """Anything
    """
    id = 0

    def __init__(self, speed=1, altitude=0, x=0):
        """

        Args:
            speed (int): speed of the rocket
            altitude (int): altitude of rocket
            x (int): position
        """
        self.altitude = altitude
        self.speed = speed

        self.x = x

        self.petrol = 100
        Rocket.id += 1
        self.id = Rocket.id

    def moveUp(self):
        """This function enable to move up (altitude) with speed (speed)
        """
        self.altitude += self.speed

    def __str__(self):
        return "The rocket is currently at altitude: " + str(self.altitude)


class RocketBoard:
    """The Rocket Board"""

    def __init__(self, amountOfRockets=5):
        self.rockets = [Rocket(randint(1, 6), randint(
            1, 6), randint(1, 6)) for _ in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].moveUp()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

    @staticmethod
    def get_distance(rocket1: Rocket, rocket2: Rocket) -> float :
        ab = (rocket1.altitude - rocket2.altitude) ** 2
        bc = (rocket1.x - rocket2.x) ** 2
        return np.sqrt(ab + bc)
    
    def get_amount_of_rockets(self):
        return len(self.rockets)

    def __len__(self):
        return self.get_amount_of_rockets()
    
    def show_id_of_rockets(self):
        for rocket in self.rockets:
            print(rocket.id)
    
