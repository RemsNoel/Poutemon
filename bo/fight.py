class Fight():

    # methode qui permet d'appeler la methode d'attaque de la classe correspondante en fonction du type en entrée
    def attaque(self, typeattaque, typedefense, basededegat):
        degat = basededegat * typeattaque.attaque(typedefense.name)
        return degat

    # methode qui permet d'appeler la methode defend de la classe correspondante en fonction du type en entrée
    def defend(self, typedefense, typeattaque, basededegat):
        degat = basededegat * typedefense.defend(typeattaque.name)
        return degat
