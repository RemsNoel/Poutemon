class Insect :


    def attaque(self, typeDefense):
        switcher = {
            "acier": 0.5,
            "combat": 0.5,
            "dragon": 1,
            "eau": 1,
            "electrik": 1,
            "fee": 0.5,
            "feu": 0.5,
            "glace": 1,
            "insecte": 1,
            "normal": 1,
            "plante": 2,
            "poison": 0.5,
            "psy": 2,
            "roche": 1,
            "sol": 1,
            "spectre": 0.5,
            "tenebre": 2,
            "vol": 0.5,
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
            "feu": 2,
            "glace": 1,
            "insecte": 1,
            "normal": 1,
            "plante": 0.5,
            "poison": 1,
            "psy": 1,
            "roche": 2,
            "sol": 0.5,
            "spectre": 1,
            "tenebre": 1,
            "vol": 2,
        }
        return switcher.get(typeAttaque)