import pygad
import numpy as np
import random
from app import GA_optimizer

def fitness_func(instance, solution, solution_idx):
    product_group = solution[:5]
    sum_group = solution[5:]

    product_value = np.prod(product_group)
    sum_value = np.sum(sum_group)

    product_fitness = 1 / (1 + abs(360 - product_value))
    sum_fitness = 1 / (1 + abs(36 - sum_value))

    fitness = product_fitness + sum_fitness
    return fitness

num_cards = 10
chromosome_genes = [i for i in range(1, num_cards + 1)]

initial_population = np.array([random.sample(chromosome_genes, len(chromosome_genes)) for _ in range(10)])

# opt = GA_optimizer(chromosome_genes, num_cards, fitness_func)

# opt.run()

# print(opt.display())

ga_instance = pygad.GA(num_generations=100,
    num_parents_mating=5,
    fitness_func=fitness_func,
    sol_per_pop=20,
    num_genes=num_cards,
    gene_type=int,
    crossover_type="single_point",
    mutation_type="swap",
    gene_space={"low": 1, "high": num_cards},
    initial_population=initial_population
)

# ga_instance = pygad.GA(num_generations=100,
#     num_parents_mating=5,
#     fitness_func=fitness_func,
#     sol_per_pop=20,
#     num_genes=num_cards,
#     gene_type=int,
#     parent_selection_type="tournament",
#     crossover_type="single_point",
#     mutation_type="random",
#     gene_space={"low": 1, "high": num_cards},
#     initial_population=initial_population
# )
ga_instance.run()

best_solution = ga_instance.best_solution()

best_solution_chromosome = best_solution[0]
best_solution_fitness = best_solution [1]

first_group= best_solution_chromosome[:5]

second_group = best_solution_chromosome [5:]


product_first_group = np.prod(first_group)
sum_second_group = np.sum(second_group)

print("Best solution:", best_solution_chromosome)


print("Best solution fitness:", best_solution_fitness)


print(first_group, np.prod (first_group))
print(second_group, np.sum (second_group))
