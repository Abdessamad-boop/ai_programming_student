"""
Oefening 2: Sliding Puzzle (8-puzzle)
======================================
Implementeer de sliding puzzle en los hem op met BFS/DFS.
"""
import numpy as np
from collections import deque

class SlidingPuzzle:
    GRIDSIZE = 3
    EMPTY = 0

    GOAL = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    def __init__(self, game):
        self.Game = np.array(game)

    def possible_new_configurations(self):
        # TODO: geef alle nieuwe configuraties door het lege vakje te verschuiven
        configurations = []
        
        row, col = self.locate_empty()
        
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for d_row, d_col in moves:
            new_row = row + d_row
            new_col = col + d_col
            
            if 0 <= new_row < self.GRIDSIZE and 0 <= new_col < self.GRIDSIZE:
                
                new_puzzle = self.duplicate()
                
                getal = new_puzzle.Game[new_row][new_col] 
                
                new_puzzle.Game[row][col] = getal 
                new_puzzle.Game[new_row][new_col] = self.EMPTY 
                
                configurations.append(new_puzzle)
                
        return configurations

    def locate_empty(self):
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                if self.Game[row][col] == self.EMPTY:
                    return (row, col)
        raise Exception("Geen leeg vakje!")

    def manhattan_distance(self):
        totale_afstand = 0

        for rij_huidig in range(self.GRIDSIZE):
            for kol_huidig in range(self.GRIDSIZE):
                getal = self.Game[rij_huidig][kol_huidig]

                if getal != self.EMPTY:
                    
                    for rij_doel in range(self.GRIDSIZE):
                        for kol_doel in range(self.GRIDSIZE):
                            
                            if self.GOAL[rij_doel][kol_doel] == getal:
                                afstand = abs(rij_doel - rij_huidig) + abs(kol_doel - kol_huidig)
                                totale_afstand += afstand
                                
        return totale_afstand
                    

    def is_goal(self):
        return np.array_equal(self.Game, self.GOAL)

    def duplicate(self):
        return SlidingPuzzle([[self.Game[r][c] for c in range(self.GRIDSIZE)] for r in range(self.GRIDSIZE)])

    def log(self):
        print("---")
        for row in self.Game:
            print(", ".join(str(int(x)) for x in row))
        print("---")


def solve_puzzle(start_puzzle):
    # 1. Maak een wachtrij (queue). We slaan de puzzel op én het pad (de stappen) ernaartoe.
    queue = deque([(start_puzzle, [start_puzzle])])
    
    # 2. Hou bij welke borden we al bezocht hebben om oneindige loops te voorkomen.
    visited = set()
    
    # NumPy arrays (jouw bord) kunnen niet in een set. We zetten het om naar een vaste "tuple".
    start_state = tuple(tuple(row) for row in start_puzzle.Game)
    visited.add(start_state)

    # 3. Blijf zoeken zolang er puzzels in de wachtrij zitten
    while queue:
        # Haal de eerste puzzel en het bijbehorende pad uit de wachtrij
        current_puzzle, path = queue.popleft()

        # 4. Controleer of we gewonnen hebben
        if current_puzzle.is_goal():
            return path # Oplossing gevonden! We geven de lijst met stappen terug.

        # 5. Bekijk alle mogelijke volgende zetten
        for next_puzzle in current_puzzle.possible_new_configurations():
            
            # Zet het nieuwe bord weer om naar een tuple
            state = tuple(tuple(row) for row in next_puzzle.Game)
            
            # Als we dit bord nog niet eerder hebben gezien
            if state not in visited:
                visited.add(state) # Markeer als bezocht
                
                # Voeg de nieuwe puzzel toe aan de wachtrij, plus het nieuwe pad
                queue.append((next_puzzle, path + [next_puzzle]))
                
    return None 


if __name__ == "__main__":
    game = [
        [1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]
    ]
    puzzle = SlidingPuzzle(game)
    print("Startconfiguratie:")
    puzzle.log()

    oplossing = solve_puzzle(puzzle)
    
    print(f"Oplossing gevonden in {len(oplossing) - 1} stappen:")
    for stap in oplossing:
        stap.log()