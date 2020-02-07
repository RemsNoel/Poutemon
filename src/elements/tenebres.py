class Tenebre :
    name = "tenebre"

    def attaque(self, typeDefense):
        switcher = {
            "acier": 1,
            "combat": 0.5,
            "dragon": 1,
            "eau": 1,
            "electrik": 1,
            "fee": 0.5,
            "feu": 1,
            "glace": 1,
            "insecte": 1,
            "normal": 1,
            "plante": 1,
            "poison": 1,
            "psy": 2,
            "roche": 1,
            "sol": 1,
            "spectre": 2,
            "tenebre": 0.5,
            "vol": 1,
        }
        return switcher.get(typeDefense)


    def defend (self, typeAttaque):
        switcher = {
            "acier": 0,
            "combat": 2,
            "dragon": 1,
            "eau": 1,
            "electrik": 1,
            "fee": 2,
            "feu": 1,
            "glace": 1,
            "insecte": 2,
            "normal": 1,
            "plante": 1,
            "poison": 1,
            "psy": 0,
            "roche": 1,
            "sol": 1,
            "spectre": 0.5,
            "tenebre": 0.5,
            "vol": 1,
        }
        return switcher.get(typeAttaque)