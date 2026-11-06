class Menneske:
    def __init__(self, navn, alder, yrke, hoyde):
        self.navn = navn
        self.alder = alder
        self.yrke = yrke
        self.hoyde = hoyde
    def presenter(self):
        print(f"Hei jeg heter {self.navn}")
    def bliEldre(self):
        print(f"Jeg var {self.alder} år gammel")
        self.alder += 1
        print(f"Jeg er {self.alder} år gammel")

    def jobb(self):
        print("Mennesket jobbet")

class Laerer(Menneske):
    def __init__(self, navn, alder, yrke, hoyde, elever):
        super().__init__(navn, alder, yrke, hoyde,)
        self.elever = elever
        
    def retteProve(self):
        print(f"{self.navn} rettet en prøve")

    def jobb(self):
        print("læreren jobber")

class Butikk(Menneske):
    def jobb(self):
        print("jobber i butikk")

class IKjeller(Menneske):
    def jobb(self):
        print("jobber i kjelleren")

jakob = Laerer("Jakob", 27, "lærer", 187, 6)
kari = Butikk("Kari", 14, "butikk", 134)
filip = IKjeller("Filip", 69, "I kjeller", 99)
maja = Menneske("Maja", 67, "Elev", 177)

print(jakob.alder)
print(kari.alder)
print(filip.alder)
print(maja.alder)

jakob.presenter()
jakob.bliEldre()
jakob.retteProve()
jakob.jobb()
kari.jobb()
filip.jobb()
maja.jobb()

arbeidere = [jakob, kari, filip, maja]

for arbeidere in arbeidere:
    arbeidere.jobb()

