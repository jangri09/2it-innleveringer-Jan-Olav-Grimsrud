try:
    with open("filOperasjoner/galakse.txt", "r") as fil:
        print(fil.read)
except FileNotFoundError:
    print("filen ekssieterer ikke")

while True:
    try:
        planetNummer = int(input("Velg planetNR: "))
    except ValueError:
        print("skriv et tall!!")
    else:
        print(planetNummer)
        break
    