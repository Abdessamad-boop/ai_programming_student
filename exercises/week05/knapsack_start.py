"""
Oefening 2: Knapsack Probleem met pygad
=========================================
Los het knapsack probleem op met een genetisch algoritme.
"""
import pygad
import numpy as np

# Data
capaciteit = 10
gewichten = np.array([5, 4, 6, 3])
waarden = np.array([10, 40, 30, 50])
n_voorwerpen = len(gewichten)


def fitness_func(ga_instance,solution, solution_idx):
    # TODO: bereken totale waarde, straf als gewicht > capaciteit
    totaal_gewicht = np.sum(solution * gewichten)
    
    # 2. Bereken de totale waarde van de gekozen voorwerpen
    totale_waarde = np.sum(solution * waarden)
    
    # 3. Deel de straf uit als de rugzak te zwaar is
    if totaal_gewicht > capaciteit:
        return 0  # Straf! De rugzak scheurt, dus de score is 0.
    else:
        return totale_waarde  # Alles is oké, de score is gewoon de waarde.
    


# TODO: configureer pygad.GA (zie OneMax.py uit de cursus)
ga_instance = pygad.GA(
    num_generations=50,            
    sol_per_pop=10,                
    num_parents_mating=4,           
    fitness_func=fitness_func,      
    num_genes=n_voorwerpen,         
    gene_space=[0, 1],              
    mutation_percent_genes=10       
)
ga_instance.run()

# Oplossing tonen
solution, solution_fitness, _ = ga_instance.best_solution()
print("Gekozen voorwerpen:", solution)
print("Totale waarde:", solution_fitness)