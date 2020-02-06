
class Zones():

    def __init__(self,actuel,avant,apres,evenement,typezone):
        self.actuel = actuel
        self.avant = avant
        self.apres = apres

        self.evenement = evenement
        self.typezone = typezone
      

    def get_actuel(self):
        return self.actuel

    def get_avant(self):
        return self.avant

    def get_apres(self):
        return self.apres

    def get_typezone(self):
        return self.typezone

              