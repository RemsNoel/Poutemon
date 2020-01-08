class Fee :


    def attaque(self, typeDefense):
        switcher = {
            "acier": 0.5,
            "combat": 2,
            "dragon": 2,
            "eau": 1,
            "electrik": 1,
            "fee": 1,
            "feu": 0.5,
            "glace": 1,
            "insecte": 1,
            "normal": 1,
            "plante": 1,
            "poison": 0.5,
            "psy": 1,
            "roche": 1,
            "sol": 1,
            "spectre": 1,
            "tenebre": 2,
            "vol": 1,
        }
        return switcher.get(typeDefense)


    def defend (self, typeAttaque):
        switcher = {
            "acier": 2,
            "combat": 0.5,
            "dragon": 0,
            "eau": 1,
            "electrik": 1,
            "fee": 1,
            "feu": 1,
            "glace": 1,
            "insecte": 0.5,
            "normal": 1,
            "plante": 1,
            "poison": 2,
            "psy": 1,
            "roche": 1,
            "sol": 1,
            "spectre": 1,
            "tenebre": 0.5,
            "vol": 1,
        }
        return switcher.get(typeAttaque)