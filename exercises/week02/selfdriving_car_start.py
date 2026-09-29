"""
Oefening 1: Self-Driving Car (Model-based Reflex Agent)
========================================================
Implementeer een agent die zijn voorligger volgt op 10m.
"""


class LidarSensorInput:
    def __init__(self, distance=0.0):
        self.DistanceTo = distance


class Brake:
    def __str__(self):
        return "BRAKE"


class Nothing:
    def __str__(self):
        return "NOTHING"


class SelfDrivingCar:
    def __init__(self):
        self.vorige_afstand = None

    def process(self, sensor_input):
        # TODO: bereken relatieve snelheid en tijd tot botsing
        #       rem als tijd < 5 seconden
        huidige_afstand = sensor_input.DistanceTo
        action = Nothing()

        if self.vorige_afstand is not None:
            snelheid = self.vorige_afstand - huidige_afstand
            if snelheid > 0:
                tijd = huidige_afstand / snelheid
                if tijd < 5:
                    action = Brake()

        self.vorige_afstand = huidige_afstand

        
       
        return action


if __name__ == "__main__":
    sensor = LidarSensorInput(10)
    agent = SelfDrivingCar()

    for afstand in [10, 15, 13, 10, 8, 6, 4, 3]:
        sensor.DistanceTo = afstand
        action = agent.process(sensor)
        print(f"Afstand: {afstand}m -> {action}")