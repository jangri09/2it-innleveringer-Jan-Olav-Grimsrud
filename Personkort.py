navn = input("Skriv inn navnet ditt: ")
alder = int(input("Skriv inn alderen din: "))
høyde = float(input("Skriv inn høyden din i meter: "))
liker_python = input("Liker du Python? (ja/nei): ").strip().lower() == "ja"

print("Navn:", navn)
print("Alder:", alder)
print("Høyde:", høyde)
print("Liker Python:", liker_python)