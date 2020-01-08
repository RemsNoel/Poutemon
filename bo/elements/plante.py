class Plante :


    def attaque(self, typeDefense):
        switcher = {
            "acier": 0.5,
            "combat": 1,
            "dragon": 1,
            "eau": 0.5,
            "electrik": 0.5,
            "fee": 2,
            "feu": 0.5,
            "glace": 2,
            "insecte": 1,
            "normal": 1,
            "plante": 1,
            "poison": 1,
            "psy": 1,
            "roche": 2,
            "sol": 1,
            "spectre": 1,
            "tenebre": 1,
            "vol": 1,
        }
        return switcher.get(typeDefense)


    def defend (self, typeAttaque):
        switcher = {
            "acier": 0.5,
            "combat": 2,
            "dragon": 0.5,
            "eau": 1,
            "electrik": 1,
            "fee": 0.5,
            "feu": 2,
            "glace": 0.5,
            "insecte": 0.5,
            "normal": 0.5,
            "plante": 0.5,
            "poison": 0,
            "psy": 0.5,
            "roche": 0.5,
            "sol": 2,
            "spectre": 1,
            "tenebre": 1,
            "vol": 0.5,
        }
        return switcher.get(typeAttaque)