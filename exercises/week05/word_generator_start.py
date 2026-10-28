"""
Oefening 1: Word Generator (Genetisch Algoritme)
==================================================
Evolueer een populatie van willekeurige zinnen naar een doelzin.
"""
import random
import string


class WordPuzzle:
    def __init__(self, target_phrase, population_size=100, mutation_rate=0.01, num_generations=10000):
        self.target_phrase = target_phrase
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations

    def generate_phrase(self, length):
        return "".join(random.choice(string.printable) for _ in range(length))

    def calculate_fitness(self, phrase):
        score = 0
        for i in range(len(phrase)):
            if phrase[i] == self.target_phrase[i]:
                score += 1
        return score / len(self.target_phrase)

    def generate_population(self, size, phrase_length):
        return [self.generate_phrase(phrase_length) for _ in range(size)]

    def crossover(self, phrase1, phrase2):
        split_point = random.randint(0, len(phrase1) - 1)
        child = phrase1[:split_point] + phrase2[split_point:]
        return child

    def mutate(self, phrase, rate):
        mutated_phrase = ""
        for char in phrase:
            if random.random() < rate: # Kans op mutatie (bv 0.01 = 1%)
                mutated_phrase += random.choice(string.printable)
            else:
                mutated_phrase += char
        return mutated_phrase

    def select_best(self, population):
        sorted_population = sorted(population, key=self.calculate_fitness, reverse=True)
        return sorted_population[:len(population)//2]

    def genetic_algorithm(self):
        phrase_length = len(self.target_phrase)
        
        population = self.generate_population(self.population_size, phrase_length)

        for generation in range(self.num_generations):
            
            best_parents = self.select_best(population)
            best_phrase = best_parents[0]

            if generation % 100 == 0:
                print(f"Gen {generation}: {best_phrase} (Fitness: {self.calculate_fitness(best_phrase):.2f})")

            new_population = best_parents[:]

            while len(new_population) < self.population_size:
                # Kies twee willekeurige ouders uit de 'beste helft'
                parent1 = random.choice(best_parents)
                parent2 = random.choice(best_parents)
                
                # Crossover: Maak een kind
                child = self.crossover(parent1, parent2)
                
                # Mutatie: Misschien muteert het kind een beetje
                child = self.mutate(child, self.mutation_rate)
                
                # Voeg het kind toe aan de nieuwe generatie
                new_population.append(child)

            # Vervang de oude populatie door de nieuwe populatie
            population = new_population

        # Als de loop klaar is en de zin is nog niet perfect, geef dan de beste terug die we hebben
        return self.select_best(population)[0]


def main():
    target_phrase = "De basiswetten van de robotica werden ontwikkeld door Asimov"
    puzzle = WordPuzzle(target_phrase)
    best_phrase = puzzle.genetic_algorithm()
    print(f"Beste zin: {best_phrase}")


if __name__ == "__main__":
    main()