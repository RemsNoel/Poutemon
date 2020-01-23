from bo.elements.acier import Acier
from bo.elements.combat import Combat
from bo.elements.dragon import Dragon
from bo.elements.eau import Eau
from bo.elements.electrik import Electrik
from bo.elements.fee import Fee
from bo.elements.feu import Feu
from bo.elements.glace import Glace
from bo.elements.insecte import Insect
from bo.elements.normal import Normal
from bo.elements.plante import Plante
from bo.elements.poison import Poison
from bo.elements.psy import Psy
from bo.elements.roche import Roche
from bo.elements.sol import Sol
from bo.elements.spectre import Spectre
from bo.elements.tenebres import Tenebre
from bo.elements.vol import Vol


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
