class Electrik :


    def attaque(self, typeDefense):
        switcher = {
            "acier": 1,
            "combat": 1,
            "dragon": 0.5,
            "eau": 2,
            "electrik": 0.5,
            "fee": 1,
            "feu": 1,
            "glace": 1,
            "insecte": 1,
            "normal": 1,
            "plante": 0.5,
            "poison": 1,
            "psy": 1,
            "roche": 1,
            "sol": 0,
            "spectre": 1,
            "tenebre": 1,
            "vol": 2,
        }
        return switcher.get(typeDefense)


    def defend (self, typeAttaque):
        switcher = {
            "acier": 0.5,
            "combat": 1,
            "dragon": 1,
            "eau": 1,
            "electrik": 0.5,
            "fee": 1,
            "feu": 1,
            "glace": 1,
            "insecte":1,
            "normal": 1,
            "plante": 1,
            "poison": 1,
            "psy": 1,
            "roche": 1,
            "sol": 2,
            "spectre": 1,
            "tenebre": 1,
            "vol": 0.5,
        }
        return switcher.get(typeAttaque)