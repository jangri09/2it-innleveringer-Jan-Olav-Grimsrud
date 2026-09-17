def vis_planet(planet, antall_maaner):
    print("-----------")
    print("Velkommen til en planet")
    print("planet: " + planet)
    print("antall måner: ", antall_maaner)
    print("-------------")

vis_planet("mars", 8)

def beregn_avstand(fart, timer):
    avstand =fart * timer
    return avstand

print(beregn_avstand(2187398, 100))

def vurder_tempratur(tempratur):
    if tempratur < -100:
        return "Ekstremt kaldt"
    elif tempratur < 0:
       return "Kaldt"
    elif tempratur < 30:
        return "varmt og godt"
    else:
       return "Veldig varmt"

print(vurder_tempratur(24))
