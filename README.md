###### COMP 131: Artificial Intelligence
###### Homework 4: Genetic Algorithms -- Knapsack Problem

### Code Details

### Author(s): Ercan Sen and Brandon Bell

### IMPLEMENTATION
  This is our implementation of the knapsack problem using a Genetic Algorithm
  as described by the specification on canvas.

  * The knapsack problem simulates the placement of items in a knapsack.

  * Each knapsack item has the following properties: a weight attribute value,
    and an importance attribute value.

### ARCHITECTURE
  This implementation uses genetic algorithms as an optimization to return the
  ideal combination of items in the backpack with
  the total weight not exceeding the maximum capacity of 120, and the total
  value of items in the backpack being as large as possible.

  class Knapsack()
  The Knapsack itself is represented by a class with the following attributes

    * self.dimen - items to select from 7
    * self.maxweight - max capacity of bag 120
    * self.population - array of 100 genomes, initialized empty
    * self.fit - array of 100 corresponding fitness values
    * self.weight - each of 7 items weight
    * self.importance - each of 7 items importance value

#### FUNCTION(S) IMPLEMENTED INCLUDE:

  ##### Auxiliary Functions

    def crossover(parent1, parent2) -- FRINGE OP
      * takes two parent genomes and returns two children genomes

    def generator()
      * takes no argument and returns a randomly generated genome where
      a genome is represented by an array of 7 bits representing a binary
      choice for each item there is to choose from

    def sort_list(tup_list)
      * takes a list of tuples and returns the list sorted in
      descending order by the second tuple element's value
      (in this case fitness)

  ##### Knapsack Class Member Functions

    def fitness(self, genome) -- FITNESS FUNCTION
      * takes a reference to self and a genome and returns the fitness
      value of that genome by summing its fitness values

    def pool(self) -- mate and cull GA, SOLUTION TEST
      * takes a reference to self, contains the main functionality of the GA
      which creates a population of different knapsack placements and culls
      it by 50% leaving only the fittest according to fitness value,
      then mating these fittest to replenish the 50% culled.

    def mutation(self, genome) -- FRINGE OP
      * takes a reference to self and implements a 10% chance of mutation in
      which one of the 7 bits in a genome array are flipped.

### METHODOLOGY

  Our program is implemented according to the parameters of Genetic algorithms
  specified in both the assignment handout and the class slides.

  A genome or chromosome is represented by a bit array of length 7
  corresponding to a binary choice of whether each of 7 items is in the
  knapsack.

  A fitness function is implemented which returns the total importance value
  of a given genome according to which items it contains.

  Fringe operations, crossover and mutation encompass the mating process
  of this GA.

  The pool function contains an array of the most updated population with
  the solution, or optimal individual at the front.

  This pool function can be run in a loop as many times as specified on a
  given Knapsack object. The more runtime, the better the optimization.
