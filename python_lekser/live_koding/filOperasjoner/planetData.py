
#fil = open("filOperasjoner/planeter.txt", "a")
#fil.write("mars" "\n")
#fil.close

#with open("filOperasjoner/planeter.txt", "r") as fil:
#   for linje in fil:
#        print(linje.strip())

planet = input("Skriv inn en planet: ")
antmaaner = input("Skriv inn antall måner: ")

with open("filOperasjoner/planeter.txt", "w") as fil:
    fil.write(planet + "\n")
    fil.write(antmaaner + "\n")

with open("filOperasjoner/planeter.txt", "r") as fil:
    print(fil.read())
print("planeten ble lagret")


