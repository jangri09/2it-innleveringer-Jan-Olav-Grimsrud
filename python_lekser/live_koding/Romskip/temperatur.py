def les_temperatur():
    fil = open("temperatur.txt", "r")
    temperatur = int(fil.read())
    fil.close()
    return temperatur

def vurder_temperatur(temperatur):
    if temperatur > 0:
        return("over frysepunktet")
    else:
        return("under frysepunktet")
temperatur = les_temperatur()
print("temeperatur: ", temperatur)

print(vurder_temperatur(temperatur))

