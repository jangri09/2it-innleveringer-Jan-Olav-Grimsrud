navn = input("Skriv inn navnet ditt: ")
while True:
    try:
        alder = int(input("Skriv inn alderen din: "))
        break
    except ValueError:
        print("Vennligst skriv inn et gyldig tall for alderen.")
while True:
    try:
        høyde = float(input("Skriv inn høyden din i meter: "))
        break
    except ValueError:
        print("Vennligst skriv inn et gyldig tall for høyden.")
while True:
    liker_python = input("Liker du Python? (ja/nei): ").strip().lower()
    if liker_python in ["ja", "nei"]:
        break
    else:
        print("Vennligst svar med 'ja' eller 'nei'.")

print("Navn:", navn)
print("Alder:", alder)
print("Høyde:", høyde)
print("Liker Python:", liker_python)