#!/usr/bin/env python
import math


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    '''
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    '''
    def distance_to(self, city):
        x_dist = math.fabs(self.x - city.x)
        y_dist = math.fabs(self.y - city.y)
        dist = math.sqrt(math.pow(x_dist, 2) + math.pow(y_dist, 2))
        return dist

    def __str__(self):
        return str(self.x) + "," + str(self.y)
