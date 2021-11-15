import math
import numpy as np
import random
from cities import city_dic



#calculate distance 
def distance(city1, city2):
    x_dis = city1[0] - city2[0]
    y_dis =  city1[1] - city2[1]
    distance = math.sqrt(abs((x_dis ** 2) + (y_dis ** 2)))
    return distance


#generate random population
def init_pop(len, num_city):
    initialPopulation = []
    for i in range(len):
        chromosome = [[i, city_dic[i]] for i in range(1, num_city+1)]
        random.shuffle(chromosome)
        initialPopulation.append(chromosome)
    return initialPopulation


#calaulate the total distance travled for a given route 
def fitness(chromosome):
    distanceTravled = 0
    for i in range(1, len(chromosome)+1):
        if i!=len(chromosome):
            distanceTravled += distance(chromosome[i-1][1], chromosome[i][1])
        distanceTravled += distance(chromosome[0][1], chromosome[-1][1])
    return distanceTravled

# select the top given number chromosomes
def select(fit, distances, population, topSolu):
    TopPopualtion = []
    for i in range(topSolu):
        TopPopualtion.append(population[fit[distances[i]]])

    return TopPopualtion

def mutate(population):
    parents = []
    for chromosme in population:
        if random.random() > 0.5:
            k = random.sample(chromosme, len(chromosme))
            parents.append(k)
        else:
            parents.append(chromosme)
    # raise NotImplemented
    return parents

def crossover(parents):
    offsprings = []
    parents_len = len(parents)
    for parent in parents:
        index = random.randint(0,parents_len-1)
        parent2 = parents[index]
        crossover_point1 = random.randint(1,parents_len -1)
        crossover_point2 = random.randint(1,parents_len -1)
        parent[crossover_point1] = parent2[index]
        parent2[crossover_point2] = parent[crossover_point1]
        offsprings.append(parent)
        offsprings.append(parent2)
    return offsprings 
