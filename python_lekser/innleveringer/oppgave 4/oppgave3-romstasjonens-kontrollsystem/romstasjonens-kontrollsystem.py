class Romstasjonens_enheter:
    def __init__(self, navn, status):
        self.navn = navn
        self.status = status

    def presenter(self):
        print(f"Enheten {self.navn} har status: {self.status}.")

class Roboter(Romstasjonens_enheter):
    def __init__(self, navn, status, oppgave):
        super().__init__(navn, status)
        self.oppgave = oppgave
        
    def presenter(self):
        super().presenter()
        print(f"Roboten {self.navn} har oppgaven: {self.oppgave}.")

class Satellitter(Romstasjonens_enheter):
    def __init__(self, navn, status, type_sensor):
        super().__init__(navn, status)
        self.type_sensor = type_sensor

class Sensorer(Romstasjonens_enheter):
    def __init__(self, navn, status, sensor_type):
        super().__init__(navn, status)
        self.sensor_type = sensor_type