while True:
    try:
        alder = int(input("Skriv inn alderen din: "))
        break
    except ValueError:
        print("Vennligst skriv inn et gyldig tall for alderen.")

if alder < 13:
    print("barn")
elif alder < 18:
    print("ungdom")
else:
    print("voksen")

