class Poison :


    def attaque(self, typeDefense):
        switcher = {
            "acier": 0,
            "combat": 1,
            "dragon": 1,
            "eau": 1,
            "electrik": 1,
            "fee": 2,
            "feu": 1,
            "glace": 1,
            "insecte": 1,
            "normal": 1,
            "plante": 2,
            "poison": 0.5,
            "psy": 1,
            "roche": 0.5,
            "sol": 0.5,
            "spectre": 0.5,
            "tenebre": 1,
            "vol": 1,
        }
        return switcher.get(typeDefense)


    def defend (self, typeAttaque):
        switcher = {
            "acier": 1,
            "combat": 0.5,
            "dragon": 1,
            "eau": 1,
            "electrik": 1,
            "fee": 0.5,
            "feu": 1,
            "glace": 1,
            "insecte": 0.5,
            "normal": 1,
            "plante": 0.5,
            "poison": 0.5,
            "psy": 2,
            "roche": 1,
            "sol": 2,
            "spectre": 1,
            "tenebre": 1,
            "vol": 1,
        }
        return switcher.get(typeAttaque)