"""La o ferma avicola sunt x pasari. Jumatate din acestea sunt gaini. Numarul ratelor constituie
un sfert din numarul gainilor. Celelalte sunt gaste. Scrieti un program care citeste de la tastatura
numarul total de pasari si afiseaza numarul de gaini, rate si gaste.
Date de intrare: 4560 de pasari, Date de iesire: gaini-2280, rate-570, gaste-1710"""
p = int(input("Dati numarul total de pasari: "))
print("Din", '\33[93m',p, '\33[37m',"de  pasari",'\33[93m',p//2,'\33[37m', "sunt  gaini,", '\33[93m', (p//2)//4, '\33[37m', "sunt  rate, iar", '\33[93m', p-(p//2)-((p//2)//4), '\33[37m', "sunt  gaste.", end='')