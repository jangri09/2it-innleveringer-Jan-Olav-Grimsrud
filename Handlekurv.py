pris_baguette = 45
pris_energidrikk = 25

print("Velkommen til handlekurven!")
print("Vi har følgende varer tilgjengelig:")
print(f"1. Energidrikk - {pris_energidrikk} kr")
print(f"2. Baguette - {pris_baguette} kr")

while True:
    try:
        antall_energidrikk = int(input("Hvor mange energidrikker vil du kjøpe? "))
        break
    except ValueError:
        print("Vennligst skriv inn et gyldig tall for antall energidrikker.")
while True:
    try:
        antall_baguette = int(input("Hvor mange baguetter vil du kjøpe? "))
        break
    except ValueError:
        print("Vennligst skriv inn et gyldig tall for antall baguetter.")

total_energidrikk = pris_energidrikk * antall_energidrikk
total_baguette = pris_baguette * antall_baguette
totalpris = total_energidrikk + total_baguette

print("totalpris energidrikk:", total_energidrikk)
print("totalpris baguette:", total_baguette)
print("Totalpris:", totalpris)