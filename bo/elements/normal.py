class Normal :


    def attaque(self, typeDefense):
        switcher = {
            "acier": 0.5,
            "combat": 1,
            "dragon": 1,
            "eau": 1,
            "electrik": 1,
            "fee": 1,
            "feu": 1,
            "glace": 1,
            "insecte": 1,
            "normal": 1,
            "plante": 1,
            "poison": 1,
            "psy": 1,
            "roche": 0.5,
            "sol": 1,
            "spectre": 0,
            "tenebre": 1,
            "vol": 1,
        }
        return switcher.get(typeDefense)


    def defend (self, typeAttaque):
        switcher = {
            "acier": 1,
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
            "poison": 1,
            "psy": 1,
            "roche": 1,
            "sol": 1,
            "spectre": 0,
            "tenebre": 1,
            "vol": 1,
        }
        return switcher.get(typeAttaque)