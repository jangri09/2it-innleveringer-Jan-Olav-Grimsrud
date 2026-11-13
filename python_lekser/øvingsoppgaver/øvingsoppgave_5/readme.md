del 1:
oppgave 1.1

Fido sier voff
Ukjent lager en lyd

jeg tror programet skriver ut dette fordy listen dyrene starter på hund navnet Fido. siden for d in dyrene gjør d om til hund først skrives hund.lyd som printer self.navn, "sier voff" som blir Fido sier voff. neste blir d om til katt men siden kat ikke har en lyd funksjon kommer ingenting til å skje. eventuelt blir det en error. til slutt tar programet d til dyr("Ukjent") som skriver dyr.lyd() som da bruker funksjonen lyd og printer self.navn, "lager en lyd" som da blir "Ukjent lager en lyd"
hvis du skal lege til for eksemple lyd tar du bort pass og leger in en def med def lyd(self): print(slef.navn, "sier mow")

jeg testa koden og inså at jeg tok feil. katt kommer også til å si "lager en lyd" fordi den arver det fra dyr.

oppgave 1.2
det er fordi ikke super() er brukt for å få variablene fra kjoretoy til å fungere i Elbil classen.
class Kjoretoy:
def **init**(self, merke, aarsmodell):
self.merke = merke
self.aarsmodell = aarsmodell

    def info(self):
        print(self.merke, "fra", self.aarsmodell)

class Elbil(Kjoretoy):
def **init**(self, merke, aarsmodell, rekkevidde):
super().**init**(merke, aarsmodell)
self.rekkevidde = rekkevidde

bil = Elbil("Tesla", 2021, 450)
bil.info()

oppgave 1.3

1. hund brude arve fra dyr siden hund er et dyr.
2. hjul burde arve fra bil siden hjul er en del av bil.
3. elev brude arve fra person siden elev er en type person.
4. bok brude arve fra biblotek fro det er noe som er i biblotek.
5. lærer brude arve fra skole fordi lærer er en rolle på skole.
6. rektangel og kvadrat brude ikke arve noe fra hverandre men brude heller arve fra for eksemple noe som heter form eller firkant. fordi de er en form og firkant

del 2
