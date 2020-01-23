from bo.fight import Fight

acier = "acier"
roche = "roche"
fight = Fight()
num = fight.defend(acier, roche, 20)
print(num)
num = fight.attaque(acier, roche, 20)
print(num)