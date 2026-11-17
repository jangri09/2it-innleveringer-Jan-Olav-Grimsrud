import pytest
from romfartoy import Romfartoy

@pytest.mark.parametrize("navn, hastighet, drivstoff", [
    ("Test Romfartøy 1", 1000, 10),
    ("Test Romfartøy 2", 2000, 20),
    ("Test Romfartøy 3", 3000, 30),
])
def test_romfartoy_initialisering(navn, hastighet, drivstoff):
    romfartoy = Romfartoy(navn, hastighet, drivstoff)
    assert romfartoy.navn == navn
    assert romfartoy.hastighet == hastighet
    assert romfartoy.drivstoff == drivstoff


@pytest.mark.parametrize("navn, hastighet, drivstoff, drivstoff_forventet, hastighet_forventet", [
    ("Test Romfartøy 1", 1000, 8, 0, 1010),
    ("Test Romfartøy 2", 2000, 20, 12, 2010),
    ("Test Romfartøy 3", 1500, 2, 2, 1500),  # Ikke nok drivstoff til å øke hastigheten
])
def test_romfartoy_oker_hastighet(navn, hastighet, drivstoff, drivstoff_forventet, hastighet_forventet):
    romfartoy = Romfartoy(navn, hastighet, drivstoff)
    romfartoy.oek_hastighet()
    assert romfartoy.hastighet == hastighet_forventet
    assert romfartoy.drivstoff == drivstoff_forventet

