def satelittmeldinger(navn, planet):
    print("Dette er satelitt ", navn)
    print("Jeg er på planeten ", planet)

def signaltid_satelitt(km):
    tid = km / 300000
    return tid

def vurder_signaltid_satelitt(tid):
    if tid <= 1:
        return "Direkte kommunikasjon"
    elif tid <= 10:
        return "Forsinket kommunikasjon"
    else:
        return "Stor forsinkelse"
def meteorvarsel(dimeter, km_fra_jorden):
    if dimeter >= 10000:
        return "Høy risiko"
    elif km_fra_jorden <= 5000:
        return "Høy risiko"
    elif dimeter >= 50000:
        return "Middels risiko"
    elif km_fra_jorden <= 10000:
        return "Middels risiko"
    else:
        return "lav risiko"
satelittmeldinger("satelitt-potet", "mars")
satelittmeldinger("satelitt-Jan21", "Jorda")
satelittmeldinger("satelitt-kåre2", "Månen")

signaltid = signaltid_satelitt(10000000)
print("sekunder: ", signaltid)
signaltid = signaltid_satelitt(239098)
print("sekunder: ", signaltid)

print(vurder_signaltid_satelitt(signaltid))

print(meteorvarsel(5000, 4000))
print(meteorvarsel(1000, 10000))
print(meteorvarsel(2272, 112313))
