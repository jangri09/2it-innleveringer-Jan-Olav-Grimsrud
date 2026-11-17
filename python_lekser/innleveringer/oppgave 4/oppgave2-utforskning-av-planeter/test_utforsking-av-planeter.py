import pytest
from utforsking_av_planeter import Romfartoy, Satelitt, Romstasjon, Rombil


def test_underklasse_arver_metoder():
    romfartoy = Romfartoy("Test Romfartøy", 1000, 100)
    satelitt = Satelitt("Test Satelitt", 2000, 200, "Jorden")
    romstasjon = Romstasjon("Test Romstasjon", 3000, 300, 5)
    rombil = Rombil("Test Rombil", 4000, 400, 2)

    assert romfartoy.presenter() is None
    assert satelitt.presenter() is None
    assert romstasjon.presenter() is None
    assert rombil.presenter() is None

def test_satelitt_skift_bane():
    satelitt = Satelitt("Test Satelitt", 2000, 200, "Jorden")
    satelitt.skift_bane("Mars")
    assert satelitt.bane == "Mars"

def test_romstasjon_mannskap():
    romstasjon = Romstasjon("Test Romstasjon", 3000, 300, 5)
    assert romstasjon.mannskap == 5

def test_rombil_passasjerer():
    rombil = Rombil("Test Rombil", 4000, 400, 2)
    assert rombil.passasjerer == 2
