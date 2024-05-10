# Importing dependencies
import pygad

# Main class
class GA_optimizer:
    # Properities
    pop_size = 0    
    num_generations = 100
    GA_geneset = [i for i in range(2, 21)]
    GA_num_generations = 10
    GA_num_samples = 10

    # GA attributes
    attributes = [
        "parent_selection_type",
        "crossover_type",
        "mutation_type"
    ]

    # Gene sets for all GA attributes
    genesets = {
        "parent_selection_type": ["rws", "sss", "rank", "random", "tournament"],
        "crossover_type": ["single_point", "two_points", "uniform"],
        "mutation_type": ["random", "swap", "inversion"]
    }
    
    # GA attributes' values
    default_attributes = {
        "parent_selection_type": "roulette_wheel",
        "crossover_type": "single_point",
        "mutation_type": "random"
    }

    # Class constructor
    def __init__(self, genset, chromosome_length, fitness_function):
        self.genset = genset    # All properties and arguments in this constructor use aliasing
        self.chro_len = chromosome_length
        self.fitness_function = fitness_function

    # Method for decoding chrosome form to attributes
    def _decode(self, GA_chromosome):   # Using _privateMethod naming concept
        lst = []
        for i in range(len(GA_chromosome)):
            lst.append(self.genesets[self.attributes[i]][GA_chromosome[i]%len(self.genesets[self.attributes[i]])])

        return lst

    # Method to change the default attributes
    def _change(self, GA_chromosome):
        GA_chromosome = self._decode(GA_chromosome)
        for i in range(len(self.attributes)):
            self.default_attributes[self.attributes[i]] = GA_chromosome[i]

    # Method to get the best solution of the generated GA
    def _getSolution(self, nu):
        ga_instance = pygad.GA(
            num_generations=self.num_generations,
            num_parents_mating=2,
            fitness_func=self.fitness_function,
            sol_per_pop=8,
            num_genes=nu,
            gene_type=int,
            gene_space=self.genset,
            crossover_type=self.default_attributes["crossover_type"],
            mutation_type=self.default_attributes["mutation_type"],
            mutation_num_genes=1,
            parent_selection_type=self.default_attributes["parent_selection_type"]
        )

        ga_instance.run()

        sol, fit, idx = ga_instance.best_solution()

        return sol, fit, idx

    # Fitness function
    def GAFitness(self, instance, sol, idx):
        self._change(sol)

        fits = [0] * self.GA_num_samples

        for i in range(self.GA_num_samples):
            tmp1, fits[i], tmp2 = self._getSolution(self.chro_len)

        return (sum(fits) / len(fits))
    
    # Run method
    def run(self):
        ga_instance = pygad.GA(
            num_generations=self.GA_num_generations,
            num_parents_mating=2,
            fitness_func=self.GAFitness,
            sol_per_pop=8,
            num_genes=len(self.attributes),
            gene_type=int,
            gene_space=self.GA_geneset,
            crossover_type="single_point",
            mutation_type="random",
            mutation_num_genes=1
        )

        ga_instance.run()

        sol, fit, idx = ga_instance.best_solution()

        self._change(sol)
    
    # Method to display attributes
    def display(self):
        return self.default_attributes