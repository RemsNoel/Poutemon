class Roche :
    name = "roche"

    def attaque(self, typeDefense):
        switcher = {
            "acier": 0.5,
            "combat": 0.5,
            "dragon": 1,
            "eau": 1,
            "electrik": 1,
            "fee":1,
            "feu": 2,
            "glace": 2,
            "insecte": 2,
            "normal": 1,
            "plante": 1,
            "poison": 1,
            "psy": 1,
            "roche": 1,
            "sol": 0.5,
            "spectre": 1,
            "tenebre": 1,
            "vol": 2,
        }
        return switcher.get(typeDefense)


    def defend (self, typeAttaque):
        switcher = {
            "acier": 2,
            "combat": 2,
            "dragon": 1,
            "eau": 2,
            "electrik": 1,
            "fee": 1,
            "feu": 0.5,
            "glace": 1,
            "insecte": 1,
            "normal": 0.5,
            "plante": 2,
            "poison": 0.5,
            "psy": 1,
            "roche": 1,
            "sol": 2,
            "spectre": 1,
            "tenebre": 1,
            "vol": 0.5,
        }
        return switcher.get(typeAttaque)