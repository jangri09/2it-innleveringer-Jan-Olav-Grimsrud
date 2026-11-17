import pytest
from romstasjonens_kontrollsystem import Romstasjonens_enheter, Roboter, Satellitter, Sensorer

def test_enheter_utfor_oppdrag():
    wall_E = Roboter("Wall-E", "aktiv", "rydde opp i romstasjonen")
    hubble = Satellitter("Hubble", "aktiv", "optisk teleskop")
    advanced_sensor = Sensorer("Advanced Sensor", "aktiv", "temperaturmåling")

    assert wall_E.utfor_oppgave() is None
    assert hubble.utfor_oppgave() is None
    assert advanced_sensor.utfor_oppgave() is None

def test_utfor_oppgave_metode_arv():
    wall_E = Roboter("Wall-E", "aktiv", "rydde opp i romstasjonen")
    hubble = Satellitter("Hubble", "aktiv", "optisk teleskop")
    advanced_sensor = Sensorer("Advanced Sensor", "aktiv", "temperaturmåling")

    assert isinstance(wall_E, Romstasjonens_enheter)
    assert isinstance(hubble, Romstasjonens_enheter)
    assert isinstance(advanced_sensor, Romstasjonens_enheter)