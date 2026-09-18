def Lese_drivstoff():
    fil = open("drivstoff.txt", "r")
    drivstoff = int(fil.read())
    fil.close()
    return drivstoff
drivstoff = (Lese_drivstoff())

print("drivstoff: ", drivstoff, "%")

def Vurdere_drivstoff(drivstoff):
    if drivstoff >= 50:
        return ("nok drivstoff")
    else:
        return "for lite drivstoff!!"

print(Vurdere_drivstoff(drivstoff))
