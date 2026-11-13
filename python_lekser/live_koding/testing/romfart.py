def beregn_avstand(fart, timer):
    if timer < 0:
        raise ValueError("Tid kan ikke være negativ")
    avstand = fart * timer
    return avstand

def beregn_drivstoff(avstand, timer):
    return avstand * timer

def velkommen(navn):
    return f"Velkommen om bord {navn}"