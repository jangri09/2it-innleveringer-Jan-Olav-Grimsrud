while True:
    try:
        poeng = int(input("Skriv inn poengene dine: "))
        if 0 <= poeng <= 100:
            break
        print("Vennligst skriv inn et tall mellom 0 og 100.")
    except ValueError:
        print("Vennligst skriv inn et gyldig tall for poengene.")

if poeng >= 90:
    print("meget bra")
elif poeng >= 70:
    print("godt")
elif poeng >= 50:
    print("bestått")
else:
    print("ikke bestått")