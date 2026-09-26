"""
Oefening 2: Floor Cleaning Agent (Model-based Reflex Agent)
=============================================================
Implementeer een model-based reflex agent voor een robotstofzuiger.
Volg het stappenplan in opgave_week1.md.
"""


class FloorCleaningAgent:
    """
    Een model-based reflex agent die een kamer proper maakt.

    De kamer is een grid van `rows` × `cols` tegels.
    De robot start in de linkerbovenhoek (rij 0, kolom 0).
    """

    def __init__(self, rows=5, cols=10):
        """
        Initialiseer de robot met een lege kamer van `rows` × `cols`.

        Tip: gebruik een 2D-lijst om de status van elke tegel bij te houden.
        """
        self.rows = rows
        self.cols = cols

        # TODO: interne state initialiseren
        # - huidige positie (rij, kolom)
        # - grid met proper/vuil status per tegel (bv. True = proper, False = vuil)

        self.row = 0  # startrij (bovenaan)
        self.col = 0  # startkolom (links)

        # Voorbeeld: grid aanmaken (alle tegels beginnen vuil)
        self.grid = [[False for _ in range(cols)] for _ in range(rows)]

    # ---------- Basisbewegingen ----------

    def move_up(self):
        """Verplaats de robot één tegel omhoog (rij -1)."""
        if self.row > 0:
            self.row -= 1
            print(f"Verplaats naar ({self.row}, {self.col})")
        else:
            print("Kan niet omhoog: rand bereikt")

    def move_down(self):
        """Verplaats de robot één tegel omlaag (rij -1)."""
        if self.row < 4:
            self.row += 1
            print(f"Verplaats naar ({self.row}, {self.col})")
        else:
            print("Kan niet omlaag: rand bereikt")

    def move_left(self):
        """Verplaatst de robot één tegel naar links (kolom - 1)."""
        if self.col > 0:
            self.col -= 1
        else:
            print("kan niet naar links: rand bereikt")

    def move_right(self):
        """Verplaatst de robot één tegel naar rechts (kolom + 1)."""
        if self.col < self.cols - 1:
            self.col += 1
        else:
            print("kan niet naar rechts: rand bereikt")

    # ---------- Stofzuigen ----------

    def clean_tile(self):
        """Stofzuig de huidige tegel (maak hem proper)."""
        self.grid[self.row][self.col] = True
        print(f"Tegel ({self.row}, {self.col}) is nu proper!")
        

    # ---------- Strategie ----------

    def clean_room(self):
        # Loop door alle kolommen van links naar rechts
        for kol in range(self.cols):
            
            # Controleer of we in een 'even' of 'oneven' kolom zitten
            if kol % 2 == 0:
                # Even kolom (0, 2, 4...): Beweeg helemaal naar beneden
                for i in range(self.rows - 1):
                    self.clean_tile()
                    self.move_down()
            else:
                # Oneven kolom (1, 3, 5...): Beweeg helemaal naar boven
                for i in range(self.rows - 1):
                    self.clean_tile()
                    self.move_up()
            
            # Maak de allerlaatste tegel in de huidige kolom schoon
            self.clean_tile()
            
            # Schuif één stapje op naar rechts voor de volgende kolom (behalve als we al bij de laatste zijn)
            if kol < self.cols - 1:
                self.move_right()

    # ---------- Helper om naar een specifieke tegel te gaan ----------

    def move_to(self, target_row, target_col):
        """
        Verplaats de robot van huidige positie naar (target_row, target_col).
        Gebruik de basisbewegingen move_up/down/left/right.
        """
        while self.col != target_col:
            if self.col > target_col:
                self.move_left()

            else:
                 self.move_right()

        while self.row != target_row:
            if self.row > target_row:
                self.move_up()

            else:
                 self.move_down()     

    

    # ---------- Weergave ----------

    def print_status(self):
        """Toon de huidige status van de kamer."""
        print("\nKamer status (V = vuil, P = proper, R = robot):")
        for r in range(self.rows):
            rij_str = ""
            for c in range(self.cols):
                if r == self.row and c == self.col:
                    rij_str += " R "
                else:
                    # TODO: toon 'V' of 'P' op basis van interne grid
                    rij_str += " ? "
            print(rij_str)
        print()


if __name__ == "__main__":
    # Test je agent
    robot = FloorCleaningAgent()

    print("Beginstatus:")
    robot.print_status()

    # TODO: roep clean_room() aan
    robot.clean_room()

    print("Eindstatus:")
    robot.print_status()

#x