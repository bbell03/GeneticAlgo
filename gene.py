###### COMP 131: Artificial Intelligence
###### Homework 4: Genetic Algorithms -- Knapsack Problem

import random

def crossover(parent1, parent2):
    length_seg = random.randint(1,6)
    child1 = []
    child2 = []

    for k in range(length_seg):
        child1.append(parent1[k])
        child2.append(parent2[k])

    for l in range(7 - length_seg):
        child1.append(parent2[l+length_seg])
        child2.append(parent1[l+length_seg])

    return child1, child2

def generator():
    genome = []
    for i in range(7):
        genome.append(random.randint(0,1))
    return genome

def sort_list(tup_list):
    return sorted(tup_list, key = lambda x: x[0], reverse = True)

class Knapsack():
    def __init__(self):
        self.dimen = 7
        self.maxweight = 120
        self.population = []
        self.fit = []
        self.weight = [20, 30, 60, 90, 50, 70, 30]
        self.importance = [6, 5, 8, 7, 6, 9, 4]

    def fitness(self, genome):
        sum_weight = 0
        sum_importance = 0

        for i in range(self.dimen):
            sum_weight += genome[i]*self.weight[i]
            sum_importance += genome[i]*self.importance[i]

        if sum_weight > self.maxweight:
            return (sum_importance - 200)
        else:
            return sum_importance

    def pool(self):

        if(len(self.population) == 0):
            for i in range(100):
                self.population.append(generator())
                self.fit.append(self.fitness(self.population[i]))
        else:
            for i in range(100):
                self.fit.append(self.fitness(self.population[i]))

        fittest = list(zip(self.fit,self.population))
        fittest = sort_list(fittest)

        for i in range(50):
            self.population[i] = fittest[i][1]

        for k in range(0, 49, 2):
            tuple = crossover(fittest[k][1], fittest[k+1][1])

            self.population[50+k] = tuple[0]
            self.population[50+k+1] = tuple[1]

        for l in range(50,100):
            self.population[l] = self.mutation(self.population[l])

        self.fit = []
        for i in range(100):
            self.fit.append(self.fitness(self.population[i]))
        fittest = list(zip(self.fit,self.population))
        fittest = sort_list(fittest)

        self.fit = []

    def mutation(self, genome):

        mutated = genome

        if(random.randint(1,100) < 10):
            i = random.randint(0,6)

            if (genome[i] == 0):
                mutated[i] = 1
            else:
                mutated[i] = 0

        if (self.fitness(genome) > self.fitness(mutated)):
            return genome
        else:
            return mutated


###MAIN
bag = Knapsack()
for i in range(15):
    bag.pool()
print(bag.population[0])
print(bag.population[99])
