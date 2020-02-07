class Combat :
    name = "combat"

    def attaque(self, typeDefense):
        switcher = {
            "acier": 2,
            "combat": 1,
            "dragon": 1,
            "eau": 1,
            "electrik": 1,
            "fee": 0.5,
            "feu": 1,
            "glace": 2,
            "insecte": 0.5,
            "normal": 2,
            "plante": 1,
            "poison": 0.5,
            "psy": 0.5,
            "roche": 2,
            "sol": 1,
            "spectre": 0,
            "tenebre": 2,
            "vol": 0.5,
        }
        return switcher.get(typeDefense)


    def defend (self, typeAttaque):
        switcher = {
            "acier": 1,
            "combat": 1,
            "dragon": 1,
            "eau": 1,
            "electrik": 1,
            "fee": 2,
            "feu": 1,
            "glace": 1,
            "insecte": 0.5,
            "normal": 1,
            "plante": 1,
            "poison": 1,
            "psy": 2,
            "roche": 0.5,
            "sol": 1,
            "spectre": 1,
            "tenebre": 0.5,
            "vol": 2,
        }
        return switcher.get(typeAttaque)