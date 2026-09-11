
with open("python_lekser\øve-oppgave-1\pris.txt", "r") as f:
    pris_energidrikk = int(f.readline())
    pris_baguette = int(f.readline())
    pris_poteter = int(f.readline())

def handlekurv():
    print("Velkommen til handlekurven!")
    print("Vi har følgende varer tilgjengelig:")
    print(f"1. Energidrikk - {pris_energidrikk} kr")
    print(f"2. Baguette - {pris_baguette} kr")
    print(f"3. Poteter - {pris_poteter} kr")

def ønsker_du_flere_varer():
    while True:
        valg = input("Hva vil du kjøpe? (1 for energidrikk, 2 for baguette, 3 for poteter): ")
        if valg == "1":
            while True:
                try:
                    global antall_energidrikk
                    antall_energidrikk =+ int(input("Hvor mange energidrikker vil du kjøpe? "))
                    break
                except ValueError:
                    print("Vennligst skriv inn et gyldig tall for antall energidrikker.")
            break
        elif valg == "2":
            while True:
                try:
                    global antall_baguette
                    antall_baguette =+ int(input("Hvor mange baguetter vil du kjøpe? "))
                    break
                except ValueError:
                    print("Vennligst skriv inn et gyldig tall for antall baguetter.")
            break
        elif valg == "3":
            while True:
                try:
                    global antall_poteter
                    antall_poteter =+ int(input("Hvor mange poteter vil du kjøpe? "))
                    break
                except ValueError:
                    print("Vennligst skriv inn et gyldig tall for antall poteter.")
            break
        else:
            print("Ugyldig valg. Vennligst velg 1, 2 eller 3.")

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

if 'antall_energidrikk' not in globals():
    antall_energidrikk = 0
if 'antall_baguette' not in globals():
    antall_baguette = 0
if 'antall_poteter' not in globals():
    antall_poteter = 0
totalpris = (antall_energidrikk * pris_energidrikk) + (antall_baguette * pris_baguette) + (antall_poteter * pris_poteter)
totalpris_energidrikk = antall_energidrikk * pris_energidrikk
totalpris_baguette = antall_baguette * pris_baguette
totalpris_poteter = antall_poteter * pris_poteter

if antall_energidrikk > 0:
    print(f"Du har kjøpt {antall_energidrikk} energidrikker til en totalpris av {totalpris_energidrikk} kr.")
if antall_baguette > 0:
    print(f"Du har kjøpt {antall_baguette} baguetter til en totalpris av {totalpris_baguette} kr.")
if antall_poteter > 0:
    print(f"Du har kjøpt {antall_poteter} poteter til en totalpris av {totalpris_poteter} kr.")
print(f"Totalpris: {totalpris} kr")

with open("python_lekser\øve-oppgave-1\handlekurv.txt", "w") as f:
    if antall_energidrikk > 0:
        f.write(f"Du har kjøpt {antall_energidrikk} energidrikker til en totalpris av {totalpris_energidrikk} kr.\n")
    if antall_baguette > 0:
        f.write(f"Du har kjøpt {antall_baguette} baguetter til en totalpris av {totalpris_baguette} kr.\n")
    if antall_poteter > 0:
        f.write(f"Du har kjøpt {antall_poteter} poteter til en totalpris av {totalpris_poteter} kr.\n")
    f.write(f"Totalpris: {totalpris} kr\n")