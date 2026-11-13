class Kjoretoy:
    def __init__(self, merke, aarsmodell):
        self.merke = merke
        self.aarsmodell = aarsmodell

    def info(self):
        print(self.merke, "fra", self.aarsmodell)

class Elbil(Kjoretoy):
    def __init__(self, merke, aarsmodell, rekkevidde):
        super().__init__(merke, aarsmodell)
        self.rekkevidde = rekkevidde

bil = Elbil("Tesla", 2021, 450)
bil.info()
