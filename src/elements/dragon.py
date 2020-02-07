class Dragon :
    name = "dragon"

    def attaque(self, typeDefense):
        switcher = {
            "acier": 0.5,
            "combat": 1,
            "dragon": 2,
            "eau": 1,
            "electrik": 1,
            "fee": 0,
            "feu": 1,
            "glace": 1,
            "insecte": 1,
            "normal": 1,
            "plante": 1,
            "poison": 1,
            "psy": 1,
            "roche": 1,
            "sol": 1,
            "spectre": 1,
            "tenebre": 1,
            "vol": 1,
        }
        return switcher.get(typeDefense)


    def defend (self, typeAttaque):
        switcher = {
            "acier": 1,
            "combat": 1,
            "dragon": 2,
            "eau": 0.5,
            "electrik": 0.5,
            "fee": 2,
            "feu": 0.5,
            "glace": 2,
            "insecte": 1,
            "normal": 1,
            "plante": 0.5,
            "poison": 1,
            "psy": 1,
            "roche": 1,
            "sol": 1,
            "spectre": 1,
            "tenebre": 1,
            "vol": 1,
        }
        return switcher.get(typeAttaque)