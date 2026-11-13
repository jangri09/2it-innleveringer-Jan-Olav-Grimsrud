class Menneske:
    def __init__(self, navn, alder, yrke, hoyde):
        self.navn = navn
        self.alder = alder
        self.yrke = yrke
        self.hoyde = hoyde
    def presenter(self):
        print(f"Hei jeg heter {self.navn}")

class Laerer(Menneske):
    def __init__(self, navn, alder, yrke, hoyde, elever):
        super().__init__(navn, alder, yrke, hoyde)
        self.elever = elever
    def presenter(self):
        super().presenter()
        print(f"Jeg underviser {', '.join(self.elever)}")

jakob = Laerer("Jakob", 27, "lærer", 187, ["Kari", "Filip", "Maja"])
kari = Menneske("Kari", 14, "butikk", 134)
filip = Menneske("Filip", 69, "I kjeller", 99)
maja = Menneske("Maja", 67, "Elev", 177)

jakob.presenter()


