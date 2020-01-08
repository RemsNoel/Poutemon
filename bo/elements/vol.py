class Vol :


    def attaque(self, typeDefense):
        switcher = {
            "acier": 0.5,
            "combat": 2,
            "dragon": 1,
            "eau": 1,
            "electrik": 0.5,
            "fee": 1,
            "feu": 1,
            "glace": 1,
            "insecte": 2,
            "normal": 1,
            "plante": 2,
            "poison": 1,
            "psy": 1,
            "roche": 0.5,
            "sol": 1,
            "spectre": 1,
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
            "electrik": 2,
            "fee": 1,
            "feu": 1,
            "glace": 2,
            "insecte": 0.5,
            "normal": 1,
            "plante": 0.5,
            "poison": 1,
            "psy": 1,
            "roche":2,
            "sol": 0,
            "spectre": 1,
            "tenebre": 1,
            "vol": 1,
        }
        return switcher.get(typeAttaque)