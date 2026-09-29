planeter0 = ["venus", "merkur", "jorden", "mars", "jupiter"]

print(planeter0)

print(planeter0[0])

print(planeter0[4])

planeter0.append("neptun")

print(planeter0)

print(len(planeter0))



planeter1 = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter"]

print(planeter1)

planeter1.remove("Venus")

print(planeter1)


fjernetplanet = planeter1.pop(2)

print("planeten som ble fjernet var: ", fjernetplanet)

print(planeter1)

ekspedisjon = []

i = 0
while i < 3:
    ekspedisjon.append(input("hvilke planeter hvil du besøke? "))
    i+=1

for index, planeter in enumerate(ekspedisjon):
    print(index, planeter)

indre_planeter = ("Merkur", "Venus", "Jorden", "Mars")

print(indre_planeter)
print(indre_planeter[1])

for planeter in indre_planeter:
    print(planeter)

indre_planeter[3] = "Jupiter"
print(indre_planeter)
#det fungerer ikke å endre til jupiter fordi det er en Tuple som ikke lar deg endre verdiene