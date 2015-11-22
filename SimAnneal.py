#!/usr/bin/env python
# Uses python 3.4
from City import City
import random
import math
__author__ = "will"


def tour_length(tour):
    """
    Calculates the length of the tour
    :param tour: list of City objects
    """
    length_so_far = 0
    for i in range(0, len(tour) - 2):
        length_so_far += tour[i].distance_to(tour[i + 1])
    return length_so_far


def two_opt_swap(tour, i, k):
    """
    takes the tour input and return a new tour identical to the input tour except the items
    from i to k are in reverse order
    :param tour: list of City Objects
    :param i: first index
    :param k: second index
    :rtype a new tour, which is a list of City objects
    """
    new_tour = []
    new_tour.extend(tour[:i])
    cutlet = tour[i:k]
    new_tour.extend(cutlet[::-1])
    new_tour.extend(tour[k:])

    return new_tour


def get_perturbed_path(tour):
    number_of_cities_in_a_tour = len(tour)
    i = random.randint(1, number_of_cities_in_a_tour - 2)
    k = random.randint(1, number_of_cities_in_a_tour - 2)
    if i == k:
        k -= 1
    elif k < i:
        temp = i
        i = k
        k = temp
    new_tour = two_opt_swap(tour, i, k)
    return new_tour


def get_simple_perturbed_path(tour):
    perturbed_tour_to_return = tour[:]
    pos1 = random.randint(1, cities_in_a_tour - 2)
    pos2 = random.randint(1, cities_in_a_tour - 2)
    while pos1 == pos2:
        pos2 = random.randint(1, cities_in_a_tour - 2)
    temp = perturbed_tour_to_return[pos1]
    perturbed_tour_to_return[pos1] = perturbed_tour_to_return[pos2]
    perturbed_tour_to_return[pos2] = temp
    return perturbed_tour_to_return

cities_list = []
f = open("cities.txt", "r")

for row in f:
    comps = row.rstrip("\n")
    comps = comps.split("\t")
    x = int(comps[0])
    y = int(comps[1])
    cities_list.append(City(x, y))

f.close()

best_tour = cities_list[:30]
best_tour.append(cities_list[0])  # makes a full tour
current_tour = best_tour[:]
cities_in_a_tour = len(current_tour)
temperature = 1000.0
cooling_rate = 0.9999
while temperature > 10:
    # must perturb the current_tour
    perturbed_tour = get_perturbed_path(current_tour)

    perturbed_tour_len = tour_length(perturbed_tour)
    current_tour_len = tour_length(current_tour)
    if perturbed_tour_len < current_tour_len:
        current_tour = perturbed_tour
    else:
        x = random.random()
        p = math.exp(float(current_tour_len - perturbed_tour_len) / temperature)
        if p > x:
            current_tour = perturbed_tour

    if tour_length(current_tour) < tour_length(best_tour):
        best_tour = current_tour

    temperature *= cooling_rate
    print(temperature)

for city in best_tour:
    print(city)


