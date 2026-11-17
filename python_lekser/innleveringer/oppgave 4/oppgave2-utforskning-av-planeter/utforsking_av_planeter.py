class Romfartoy:

    def __init__(self, navn, hastighet, drivstoff):
        self.navn = navn
        self.hastighet = hastighet
        self.drivstoff = drivstoff
    def presenter(self):
        print(f"Romfartøyet {self.navn} har en hastighet på {self.hastighet} km/t og bruker {self.drivstoff}L som drivstoff.")
    def oek_hastighet(self):
        if self.drivstoff >= 80:
            self.drivstoff -= 80
            self.hastighet += 10
            print(f"Hastigheten til {self.navn} er nå {self.hastighet} km/t.")
        else:
            print(f"Ikke nok drivstoff til å øke hastigheten for {self.navn}.")
            print(f"Hastigheten til {self.navn} er fortsatt {self.hastighet} km/t.")

class Satelitt(Romfartoy):
    def __init__(self, navn, hastighet, drivstoff, bane):
        super().__init__(navn, hastighet, drivstoff)
        self.bane = bane
    def presenter(self):
        super().presenter()
        print(f"{self.navn} går i bane rundt {self.bane}.")
    def skift_bane(self, ny_bane):
        self.bane = ny_bane
        print(f"{self.navn} har nå skiftet bane til {self.bane}.")

class Romstasjon(Romfartoy):
    def __init__(self, navn, hastighet, drivstoff, mannskap):
        super().__init__(navn, hastighet, drivstoff)
        self.mannskap = mannskap
    def presenter(self):
        super().presenter()
        print(f"{self.navn} har et mannskap på {self.mannskap} personer.")

class Rombil(Romfartoy):
    def __init__(self, navn, hastighet, drivstoff, passasjerer):
        super().__init__(navn, hastighet, drivstoff)
        self.passasjerer = passasjerer
    def presenter(self):
        super().presenter()
        print(f"{self.navn} har plass til {self.passasjerer} passasjerer.")

forrest = Romstasjon("Forrest", 5000, 400, 10)
mars_rover = Rombil("Mars Rover", 100, 100, 2)
kommunikasjons_satelitt = Satelitt("Kommunikasjons-satellitt", 20000, 20, "Jorden")
kommunikasjons_satelitt.presenter()
forrest.presenter()
mars_rover.presenter()
kommunikasjons_satelitt.skift_bane("Mars")
