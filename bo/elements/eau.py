class Eau :
    name = "eau"

    def attaque(self, typeDefense):
        switcher = {
            "acier": 1,
            "combat": 1,
            "dragon": 0.5,
            "eau": 0.5,
            "electrik": 1,
            "fee": 1,
            "feu": 2,
            "glace": 1,
            "insecte": 1,
            "normal": 1,
            "plante": 0.5,
            "poison": 1,
            "psy": 1,
            "roche": 2,
            "sol": 2,
            "spectre": 1,
            "tenebre": 1,
            "vol": 1,
        }
        return switcher.get(typeDefense)


    def defend (self, typeAttaque):
        switcher = {
            "acier": 0.5,
            "combat": 1,
            "dragon": 1,
            "eau": 0.5,
            "electrik": 2,
            "fee": 1,
            "feu": 0.5,
            "glace": 0.5,
            "insecte": 1,
            "normal": 1,
            "plante": 2,
            "poison": 1,
            "psy": 1,
            "roche": 1,
            "sol": 1,
            "spectre": 1,
            "tenebre": 1,
            "vol": 1,
        }
        return switcher.get(typeAttaque)