# er zijn verschillende manieren om variabelen in je string te plaatsen en deze te printen
# naam = "Teun van der Ploeg"
# print("Mijn naam is " + naam)
# print(f"Mijn naam is {naam}")
# print("Mijn naam is".format(naam))

bvn = input("Bijvoeglijk naamwoord: ")
persoon = input("Een persoon: ")
programeer_taal = input("Saaie programeer taal: ")
madlib = f"Python is een {bvn} taal om te leren. Want iedereen kan het leren zelfs {persoon}. En het is een stuk leuker dan {programeer_taal}."
print(madlib)
