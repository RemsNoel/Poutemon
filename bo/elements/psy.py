class Psy :


    def attaque(self, typeDefense):
        switcher = {
            "acier": 0.5,
            "combat": 2,
            "dragon": 1,
            "eau": 1,
            "electrik": 1,
            "fee": 1,
            "feu": 1,
            "glace": 1,
            "insecte": 1,
            "normal": 1,
            "plante": 1,
            "poison": 2,
            "psy": 0.5,
            "roche": 1,
            "sol": 1,
            "spectre": 1,
            "tenebre": 0,
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
            "fee": 1,
            "feu": 1,
            "glace": 1,
            "insecte": 2,
            "normal": 1,
            "plante": 1,
            "poison": 1,
            "psy": 0.5,
            "roche": 1,
            "sol": 1,
            "spectre": 2,
            "tenebre": 2,
            "vol": 1,
        }
        return switcher.get(typeAttaque)