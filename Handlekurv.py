pris_baguette = 45
pris_energidrikk = 25
antall_baguette = 0
antall_energidrikk = 0

def handlekurv():
    print("Velkommen til handlekurven!")
    print("Vi har følgende varer tilgjengelig:")
    print(f"1. Energidrikk - {pris_energidrikk} kr")
    print(f"2. Baguette - {pris_baguette} kr")

def ønsker_du_flere_varer():
    while True:
        valg = input("Hva vil du kjøpe? (1 for energidrikk, 2 for baguette): ")
        if valg == "1":
            while True:
                try:
                    global antall_energidrikk
                    antall_energidrikk = int(input("Hvor mange energidrikker vil du kjøpe? "))
                    break
                except ValueError:
                    print("Vennligst skriv inn et gyldig tall for antall energidrikker.")
            break
        elif valg == "2":
            while True:
                try:
                    global antall_baguette
                    antall_baguette = int(input("Hvor mange baguetter vil du kjøpe? "))
                    break
                except ValueError:
                    print("Vennligst skriv inn et gyldig tall for antall baguetter.")
            break
        else:
            print("Ugyldig valg. Vennligst velg 1 eller 2.")

def vil_du_fortsatt_kjøpe():
    while True:
        svar = input("Vil du kjøpe flere varer? (ja/nei): ").strip().lower()
        if svar in ["ja", "nei"]:
            return svar == "ja"
        else:
            print("Vennligst svar med 'ja' eller 'nei'.")

handlekurv()
ønsker_du_flere_varer()
for varer in range(1, 3):
    if vil_du_fortsatt_kjøpe():
        ønsker_du_flere_varer()
    else:
        break

totalpris = (antall_energidrikk * pris_energidrikk) + (antall_baguette * pris_baguette)
totalpris_energidrikk = antall_energidrikk * pris_energidrikk
totalpris_baguette = antall_baguette * pris_baguette
print(f"Du har kjøpt {antall_energidrikk} energidrikker til en totalpris av {totalpris_energidrikk} kr.")
print(f"Du har kjøpt {antall_baguette} baguetter til en totalpris av {totalpris_baguette} kr.")  
print(f"Totalpris: {totalpris} kr")