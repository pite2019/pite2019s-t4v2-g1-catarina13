import logging
import time
from random import gauss
import math
from os import sys


class Plane:

    def __init__(self):
        self.sigma = math.sqrt(90)
        self.angle = 0

    def correction(self):
        sigma = self.sigma
        if 0.75*sigma < self.angle < 0.75*sigma:
            self.angle = 0
        else:
            if self.angle > 0:
                self.angle -= 0.75*sigma
            else:
                self.angle += 0.75*sigma


class Environment:

    def __init__(self, plane):
        self.plane = plane

    def simulation(self):
        while True:
            turbulance = gauss(0, 3)
            self.plane.angle += turbulance
            self.plane.correction()
            if -90 < self.plane.angle < 90:
                yield turbulance, self.plane.angle
            else: 
                break


if __name__ == '__main__':

    plane = Plane()
    enviornment = Environment(plane)

    logging.basicConfig(filename='flight_simulation.log', level=logging.DEBUG) 

    for i in enviornment.simulation():
        try:
            logging.info("Turbulance: " + str(i[0]) + "; Orientation after correction: " + str(i[1]))
            if -90 < i[1] < -60:
                logging.warning("WARNING: Unstable position, please go over -60 degrees")
            elif 60 < i[1] < 90:
                logging.warning("WARNING: Unstable position, please go under 60 degrees")

            time.sleep(2)
        except KeyboardInterrupt:
            exit(0)
        
    logging.error("PLANE IS GOING TO FALL \n")

        

        

    
        
    