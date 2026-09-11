poeng = int(input("Skriv inn poengene dine: "))

while True:
    try:
        poeng = int(input("Skriv inn poengene dine: "))
        break
    except ValueError:
        print("Vennligst skriv inn et gyldig tall for poengene.")

if poeng < 0 or poeng > 100:
    print("Vennligst skriv inn et gyldig tall for poengene (0-100).")
elif poeng >= 90:
        print("meget bra")
elif poeng >= 70:
        print("godt")
elif poeng >= 50:
        print("bestått")
else:
        print("ikke bestått")