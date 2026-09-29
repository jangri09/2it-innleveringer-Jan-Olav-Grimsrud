planet0 = "venus"
planet1 = "merkur"
planet2 = "jorden"
planet3 = "mars"
planet4 = "jupiter"
planet5 = "saturn"
planet6 = "uranus"
planet7 = "neptun"

solsystem = [planet0, planet1, planet2, planet3, planet4, planet5, planet6, planet7]

print(solsystem)


nyPlanet = "pluto"
solsystem.append(nyPlanet)

print(solsystem)

solsystem.insert(1, "Aries")

print(solsystem)

solsystem.remove("pluto")

print(solsystem)

solsystem.pop(1)

print(solsystem)

for planet in solsystem:
    if planet == "venus":
        print(planet, "eksisterer")
    print(planet)

solsystem[2] = "Terra"

print(solsystem)

tall = (12, 45, 40)

for tallverdi in tall:
    print (tallverdi * 2)

for index, planet in enumerate(solsystem):
    print(index, planet)