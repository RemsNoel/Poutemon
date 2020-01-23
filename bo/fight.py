from bo.type import Type


class Fight():

    # methode qui permet d'appeler la methode d'attaque de la classe correspondante en fonction du type en entrée
    def attaque(self, typeattaque, typedefense, basededegat):
        type = Type()
        att = type.determiner(typeattaque)
        deff = type.determiner(typedefense)
        degat = basededegat * att.attaque(deff.name)
        return degat

    # methode qui permet d'appeler la methode defend de la classe correspondante en fonction du type en entrée
    def defend(self, typedefense, typeattaque, basededegat):
        type = Type()
        deff = type.determiner(typedefense)
        att = type.determiner(typeattaque)
        degat = basededegat * deff.defend(att.name)
        return degat
