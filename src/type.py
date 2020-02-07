from elements.acier import Acier
from elements.combat import Combat
from elements.dragon import Dragon
from elements.eau import Eau
from elements.electrik import Electrik
from elements.fee import Fee
from elements.feu import Feu
from elements.glace import Glace
from elements.insecte import Insect
from elements.normal import Normal
from elements.plante import Plante
from elements.poison import Poison
from elements.psy import Psy
from elements.roche import Roche
from elements.sol import Sol
from elements.spectre import Spectre
from elements.tenebres import Tenebre
from elements.vol import Vol
import pygame
import sys

class Type:

    def determiner(self, type):
        switcher = {
            "acier": Acier(),
            "combat": Combat(),
            "dragon": Dragon(),
            "eau": Eau(),
            "electrik": Electrik(),
            "fee": Fee(),
            "feu": Feu(),
            "glace": Glace(),
            "insecte": Insect(),
            "normal": Normal(),
            "plante": Plante(),
            "poison": Poison(),
            "psy": Psy(),
            "roche": Roche(),
            "sol": Sol(),
            "spectre": Spectre(),
            "tenebre": Tenebre(),
            "vol": Vol(),
        }
        return switcher.get(type)
