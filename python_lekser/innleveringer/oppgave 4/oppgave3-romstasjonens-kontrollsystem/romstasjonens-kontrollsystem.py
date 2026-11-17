class Romstasjonens_enheter:
    def __init__(self, navn, status):
        self.navn = navn
        self.status = status

    def presenter(self):
        print(f"Enheten {self.navn} har status: {self.status}.")

    def utfor_oppgave(self):
        print(f"{self.navn} utførte oppgaven sin.")

class Roboter(Romstasjonens_enheter):
    def __init__(self, navn, status, oppgave):
        super().__init__(navn, status)
        self.oppgave = oppgave

    def presenter(self):
        super().presenter()
        print(f"Roboten {self.navn} har oppgaven: {self.oppgave}.")

    def utfor_oppgave(self):
        print(f"Roboten {self.navn} utførte oppgaven: {self.oppgave}.")

class Satellitter(Romstasjonens_enheter):
    def __init__(self, navn, status, type_sensor):
        super().__init__(navn, status)
        self.type_sensor = type_sensor

    def utfor_oppgave(self):
        print(f"Satellitten {self.navn} utførte oppgaven med sensoren: {self.type_sensor}.")

class Sensorer(Romstasjonens_enheter):
    def __init__(self, navn, status, sensor_type):
        super().__init__(navn, status)
        self.sensor_type = sensor_type

    def utfor_oppgave(self):
        print(f"Sensoren {self.navn} utførte oppgaven med sensor type: {self.sensor_type}.")

tore = Roboter("Tore", "aktiv", "reparasjon")
