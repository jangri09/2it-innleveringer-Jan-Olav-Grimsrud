def les_oksygen():
    fil = open("oksygen.txt", "r")
    oksygennivaaet = int(fil.read())
    fil.close()
    return oksygennivaaet

def vurder_oksygen(prosent):
    if prosent >= 50:
        return("oksygennivaa ok")
    else:
        return("lavt oksygennivaa")
oksygenprosent = les_oksygen()
print("oksygen: ", oksygenprosent, "%")

print(vurder_oksygen(oksygenprosent))
