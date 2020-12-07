"""Doi gospodari au loturi de aceeasi arie. Un lot are forma patrata si este imprejmuit cu un gard de 48m
lungime. Alt lot are forma unui dreptunghi cu latimea de 9 m. Ce lungime are gardul care imprejmuieste 
acest lot?"""
#Prin lp si ld1 voi indica lungimea gardului si latimea dreptunghiului
lp = 48
ld1 = 9
#Apoi aflu lungimea lat. patratului(l), aria lui(a), lungimea dretunghiului(ld2) si lung. gardului(lg)
l = lp/4
a = l**2
ld2 = a/ld1
lg = 2*(ld1+ld2)
print("Lungimea gardului este de", int(lg), "de metri")