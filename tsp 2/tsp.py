import numpy as np
import random , operator
# import module 
import csv
from module import crossover, distance, fitness, init_pop, mutate, select
from cities import city_dic


num_city = len(city_dic)
# Gene = ... #city
# Chromosome =  ... #single route satisyfing the constraints
initialPopulationSize = 250
topSol = 100 ### used for elitism 
Population = init_pop(initialPopulationSize, num_city) # a collection of possible routes
# parernts = ... #routs that are comined to create offsprings 
bestSolutions = []
Distances = []
for i in range(1):
    Fitness = {}
    for i in range(len(Population)):
        Fitness[fitness(Population[i])] = i
        Distances.append(fitness(Population[i]))

    Distances.sort(reverse=True)
    TopParent = select(Fitness, Distances, Population, topSol)
    bestSolutions.append(TopParent)
    offSprings  = crossover(TopParent)
    offSprings = mutate(offSprings[:10])

    for i in range(len(bestSolutions)-1):
        if fitness(offSprings[i]) < fitness(bestSolutions[i]):
            bestSolutions[i] = offSprings[i]
Fitness = {}
for i in range(len(bestSolutions)-1):
    Fitness[fitness(bestSolutions[i])] = i
    Distances.append(fitness(bestSolutions[i]))
Distances.sort(reverse=True)
print(Distances[0])
with open('solution.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for city in bestSolutions[0]:
		writer.writerow([city])