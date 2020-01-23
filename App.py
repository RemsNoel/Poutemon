from bo.elements.acier import Acier
from bo.elements.roche import Roche
from bo.fight import Fight

acier = Acier()
roche = Roche()
fight = Fight()
num = fight.defend(acier, roche, 20)
print(num)
num = fight.attaque(acier, roche, 20)
print(num)