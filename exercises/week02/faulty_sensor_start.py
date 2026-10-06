"""
Oefening 2: Foute sensor — Boeing 737 MAX (Model-based Reflex Agent)
=====================================================================
Een vliegtuig heeft twee hoogtemeters (redundantie). Eén sensor kan
stukgaan en onzin meten (denk aan de AoA-sensor van de Boeing 737 MAX).

De agent moet:
1. Beide sensoren lezen (sensors).
2. Beoordelen of ze het met elkaar eens zijn (plausibiliteitscheck).
3. Bij discrepantie vertrouwen op de sensor die consistent is met de
   vorige waarde (sensor model + interne state).
4. Als de betrouwbare hoogtemeter daalt: een correctie aanvragen
   (actuator).
"""
from typing import Optional


class Reading:
    """Eén meetslag van beide hoogtemeters."""

    def __init__(self, sensor_a, sensor_b):
        self.sensor_a = sensor_a
        self.sensor_b = sensor_b


class Correct:
    def __str__(self):
        return "CORRECTIE AANVRAGEN"


class Nothing:
    def __str__(self):
        return "NOTHING"


class FaultTolerantAgent:
    """Model-based reflex agent met redundante sensoren.

    Interne state:
    - vorige hoogte (voor de trend)
    - welke sensor verdacht is (None, 'a' of 'b')
    """

    TOLERANCE = 50.0  # meter; meer verschil = minstens één sensor is fout
    DESCENT_LIMIT = -10.0  # meter per meetslag; meer dalen = correctie

    def __init__(self):
        self.vorige_hoogte = None
        self.verdachte_sensor = None

    def read_all(self, p: Reading) -> tuple[float, float]:
        """Sensors: geef beide metingen terug."""
        return p.sensor_a, p.sensor_b
        

    def reliable_value(self, a: float, b: float, previous: Optional[float]) -> float:
        """Sensor model: bepaal de meest betrouwbare hoogtemeting.

        Regels:
        - Verschil <= TOLERANCE -> gemiddelde is betrouwbaar.
        - Anders: kies de sensor die het dichtst bij de vorige waarde
          ligt (interne state!).
        - Is er geen vorige waarde (eerste meetslag)? -> kies
          bij voorkeur sensor a.
        """
        if self.verdachte_sensor ==  "a":
            return b
        if self.verdachte_sensor ==  "b":
            return a

        verschil = abs(a-b)
        if verschil <= self.TOLERANCE:
            return (a+b)/2
        else:
            if self.vorige_hoogte != None: #kan ook previous schrijven
                afstand_A = abs(self.vorige_hoogte-a)
                afstand_B = abs(self.vorige_hoogte-b)
                if afstand_A > afstand_B:
                    self.verdachte_sensor = "a"
                    return b

                else:
                    self.verdachte_sensor = "b"
                    return a
            else:
                self.verdachte_sensor="a"
                return a



    def process(self, p: Reading):
        # TODO: kies de betrouwbare meting, bepaal de trend (delta t.o.v.
        #       de vorige waarde) en vraag correctie aan als de daling
        #       sneller is dan DESCENT_LIMIT. Vergeet de interne state
        #       niet bij te werken.

        betrouwbare_hoogte = self.reliable_value(p.sensor_a, p.sensor_b, self.vorige_hoogte)

        if self.vorige_hoogte != None:
            daling = betrouwbare_hoogte - self.vorige_hoogte
            if daling > self.DESCENT_LIMIT:
                self.vorige_hoogte = betrouwbare_hoogte
                return Nothing()
            else:
                self.vorige_hoogte = betrouwbare_hoogte
                return Correct()
        
        self.vorige_hoogte = betrouwbare_hoogte
        return Nothing()

        


if __name__ == "__main__":
    # Vluchtprofiel: klim, cruise, daal. Sensor A valt uit bij stap 4.
    vlucht = [
        Reading(1000, 1000),   # beide ok
        Reading(1020, 1025),   # beide ok, stijgende trend
        Reading(1050, 1048),   # beide ok
        Reading(1055, 600),    # sensor B stuk (of is het A?)
        Reading(1040, 100),    # sensor B blijft onzin
        Reading(1020, 50),     # daling wordt nu zichtbaar via A
        Reading(1000, 30),     # dalende trend -> correctie nodig
    ]

    agent = FaultTolerantAgent()
    for i, p in enumerate(vlucht, start=1):
        actie = agent.process(p)
        print(f"Stap {i}: a={p.sensor_a:6.0f} b={p.sensor_b:6.0f} -> {actie}")

    # Verwacht: vanaf stap 4 vertrouwt de agent sensor A, en vanaf
    # stap 6-7 vraagt hij een correctie aan.
