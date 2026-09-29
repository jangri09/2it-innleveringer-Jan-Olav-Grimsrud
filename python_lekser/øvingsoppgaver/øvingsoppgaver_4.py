import random

planerter = ["merkur", "venus", "jorda", "mars", "jupiter", "saturn", "uranus", "neptun" ]

print("Dagens romreise går til: ", random.choice(planerter))
print("Antall astronauter: ", random.randint(1,10))

planet = input("Navn på planet: ")
antmaaner = int(input("Antall måner: "))



