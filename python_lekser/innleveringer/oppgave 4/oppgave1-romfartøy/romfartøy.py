class Romfartøy:
    def __init__(self, navn, hastighet, drivstoff):
        self.navn = navn
        self.hastighet = hastighet
        self.drivstoff = drivstoff
    def presenter(self):
        print(f"Romfartøyet {self.navn} har en hastighet på {self.hastighet} km/t og bruker {self.drivstoff} som drivstoff.")
    def oek_hastighet(self):
        self.hastighet += 10
        if self.drivstoff >= 5:
            self.drivstoff -= 5
        else:
            print(f"Ikke nok drivstoff til å øke hastigheten for {self.navn}.")
        print(f"Hastigheten til {self.navn} er nå {self.hastighet} km/t.")
