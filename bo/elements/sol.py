class Sol :


    def attaque(self, typeDefense):
        switcher = {
            "acier": 2,
            "combat": 1,
            "dragon": 1,
            "eau": 1,
            "electrik": 2,
            "fee": 1,
            "feu": 2,
            "glace": 1,
            "insecte": 0.5,
            "normal": 1,
            "plante": 0.5,
            "poison": 2,
            "psy": 1,
            "roche": 2,
            "sol": 1,
            "spectre": 1,
            "tenebre": 1,
            "vol": 0,
        }
        return switcher.get(typeDefense)


    def defend (self, typeAttaque):
        switcher = {
            "acier": 1,
            "combat": 1,
            "dragon": 1,
            "eau": 2,
            "electrik": 0,
            "fee": 1,
            "feu": 1,
            "glace": 2,
            "insecte": 1,
            "normal": 1,
            "plante": 2,
            "poison": 0.5,
            "psy": 1,
            "roche": 0.5,
            "sol": 1,
            "spectre": 1,
            "tenebre": 1,
            "vol": 1,
        }
        return switcher.get(typeAttaque)