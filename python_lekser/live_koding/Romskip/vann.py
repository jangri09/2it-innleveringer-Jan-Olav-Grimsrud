def les_vann():
    fil = open("vann.txt", "r")
    litervann = int(fil.read())
    fil.close()
    return litervann

def vurder_vann(liter):
    if liter > 50:
        print("nok vann")
    else:
        print("lite vann")

Liter_vann = (les_vann())
print("liter vann: ", Liter_vann)
vurder_vann(Liter_vann)
