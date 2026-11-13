class Romfartoy:
    def __init__(self, navn, hastighet, drivstoff):
        self.navn = navn
        self.hastighet = hastighet
        self.drivstoff = drivstoff
    def presenter(self):
        print(f"Romfartøyet {self.navn} har en hastighet på {self.hastighet} km/t og bruker {self.drivstoff} som drivstoff.")
    def oek_hastighet(self):
        if self.drivstoff >= 8:
            self.drivstoff -= 8
            self.hastighet += 10
            print(f"Hastigheten til {self.navn} er nå {self.hastighet} km/t.")
        else:
            print(f"Ikke nok drivstoff til å øke hastigheten for {self.navn}.")
            print(f"Hastigheten til {self.navn} er fortsatt {self.hastighet} km/t.")

the_odyssey = Romfartoy("The Odyssey", 10000, 2)
filip_nyhamn = Romfartoy("Filip Nyhamn", 20000, 50)
rakett = Romfartoy("Rakett", 1000, 50)


filip_nyhamn.presenter()

the_odyssey.oek_hastighet()
rakett.oek_hastighet()
