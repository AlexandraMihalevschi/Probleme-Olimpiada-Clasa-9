"""Sa se scrie un program care citeste un numar de ani si calculeaza numarul de luni, zile si ore corespunzatoare.
Se considera ca un an are 365 zile"""
n = int(input("Dati numarul de ani: "))
print(f"In {n} ani sunt", n*12, "luni,", n*365, "zile si", n*365*24, "ore")