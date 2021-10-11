def cislo():
    while True:
        cislo = input("Zadaj počet priečinkov:")
        try:
            return int(cislo)
        except ValueError:
            print("Nebolo zadané správne číslo(1 a viac) ")


cislo = cislo()
inp = []
pocet = 0

with open("basnicka.txt", encoding="utf-8") as f:
    for slovo in f:
        inp += slovo.split()
    for i in range(cislo):
        pocet += 1
        if pocet == len(inp):
            pocet -= len(inp)
        with open(f"""slovo{pocet}.txt""", mode="w", encoding="utf-8") as f:
            print(inp[pocet - 1], file=f)