
class ojeda_Persona:
    def __init__(self,ojeda_nombre,ojeda_distancia_recorrida):
        self.ojeda_nombre = ojeda_nombre
        self.ojeda_distancia_recorrida = ojeda_distancia_recorrida

    def ojeda_caminar(self, ojeda_km):
        self.ojeda_caminar = 2 


class ojeda_Atleta:
    def __init__(self, ojeda_nombre, ojeda_calorias_consumidas, ojeda_distancia_recorrida):
        self.calorias_consumidas = ojeda_calorias_consumidas
        super().__init__(self, ojeda_nombre, ojeda_distancia_recorrida)
    def ojeda_entrenar(self, ojeda_entrenar, ojeda_km):
        self.calorias_consumidas = ojeda_km/500
        self.ojeda_distancia_recorrida = 10 
    def ojeda_competencia(self, ojeda_competencia, ojeda_km):
        self.calorias_consumidas = 750
        self.ojeda

per1= ojeda_Atleta

print("per1:  )
