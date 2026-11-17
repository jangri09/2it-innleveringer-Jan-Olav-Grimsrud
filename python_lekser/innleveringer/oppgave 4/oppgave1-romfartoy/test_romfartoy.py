import pytest
from romfartoy import Romfartoy

def test_romfartoy_oker_hastighet():
    romfartoy = Romfartoy("Test Romfartøy", 1000, 10)
    romfartoy.oek_hastighet()
    assert romfartoy.hastighet == 1010
    assert romfartoy.drivstoff == 2

def test_romfartoy_ikke_nok_drivstoff():
    romfartoy = Romfartoy("Test Romfartøy", 1000, 5)
    romfartoy.oek_hastighet()
    assert romfartoy.hastighet == 1000
    assert romfartoy.drivstoff == 5
