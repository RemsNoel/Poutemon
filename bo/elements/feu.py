class Feu :


    def attaque(self, typeDefense):
        switcher = {
            "acier": 2,
            "combat": 1,
            "dragon": 0.5,
            "eau": 0.5,
            "electrik": 1,
            "fee": 1,
            "feu": 0.5,
            "glace": 2,
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
            "acier": 0.5,
            "combat": 1,
            "dragon": 1,
            "eau": 2,
            "electrik": 1,
            "fee": 0.5,
            "feu": 0.5,
            "glace": 0.5,
            "insecte": 0.5,
            "normal": 1,
            "plante": 0.5,
            "poison": 1,
            "psy": 1,
            "roche": 2,
            "sol": 1,
            "spectre": 1,
            "tenebre": 1,
            "vol": 1,
        }
        return switcher.get(typeAttaque)