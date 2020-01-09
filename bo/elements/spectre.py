class Spectre :


    def attaque(self, typeDefense):
        switcher = {
            "acier": 1,
            "combat": 1,
            "dragon": 1,
            "eau": 1,
            "electrik": 1,
            "fee": 1,
            "feu": 1,
            "glace": 1,
            "insecte": 1,
            "normal": 0,
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
            "acier": 1,
            "combat": 0,
            "dragon": 1,
            "eau": 1,
            "electrik": 1,
            "fee": 1,
            "feu": 1,
            "glace": 1,
            "insecte": 0.5,
            "normal": 0,
            "plante": 1,
            "poison": 0.5,
            "psy": 1,
            "roche": 1,
            "sol": 1,
            "spectre": 2,
            "tenebre": 2,
            "vol": 1,
        }
        return switcher.get(typeAttaque)