def les_avstand():
    fil = open("avstand.txt", "r")
    avstand = int(fil.read())
    fil.close()
    return avstand

def vurder_avstand(avstand):
    if avstand <= 10000:
        return "nerme"
    else:
        return "Langt unna"

avstand = (les_avstand())
print("Avstand: ", avstand)
print(vurder_avstand(avstand))
