
import random
import getpass

def rādīt_instrukciju():
    instrukcija = """
    --------------------------------------------
            Spēle: "Uzmini skaitli"
    --------------------------------------------
    Spēles noteikumi:
    1. Izvēlieties spēlētāju skaitu (1 vai 2). Ja izvēlēsieties 1, tad spēlēsiet pret datoru. 
    2. Ievadiet minēšanas diapazonu (piem. 1-100) un mēģinājumu skaitu (piem. 10).
    3. Ja spēlē divi spēlētāji, katrs izvēlas savu skaitli, kuru pretiniekam jāuzmin.
    4. Ja spēlē viens spēlētājs, dators izvēlēsies skaitli, kuru spēlētājam jāuzmin.
    5. Jūs minat skaitli, kamēr beidzas mēģinājumi vai kāds no spēlētājiem uzmin.
    6. Uzvarētājis ir tas kurš pirmais uzmin pretinieka skaitli ar vismazāko mēģinājumu skaitu.

    Veiksmi!
    """
    print(instrukcija)
    
def ievadi_skaitli_robeza(jautajums, min_diapazons, max_diapazons):
    while True:
        try:
            skaitlis = int(input(jautajums))
            if min_diapazons <= skaitlis <= max_diapazons:
                return skaitlis
            else:
                print(f"Lūdzu ievadi skaitli robežās no {min_diapazons} līdz {max_diapazons}.")
        except ValueError:
            print("Lūdzu ievadi derīgu skaitli.")

def ievadi_noslēpto_skaitli(jautajums, min_diapazons, max_diapazons):
    while True:
        try:
            skaitlis = int(getpass.getpass(jautajums))
            if min_diapazons <= skaitlis <= max_diapazons:
                return skaitlis
            else:
                print(f"Lūdzu ievadi skaitli robežās no {min_diapazons} līdz {max_diapazons}.")
        except ValueError:
            print("Lūdzu ievadi derīgu skaitli.")

def uzmini_skaitli():
    rādīt_instrukciju()
    # Izvēlas spēlētāju skaitu
    while True:
        try:
            spaletaju_skaits = int(input("Ievadi spēlētāju skaitu (1 vai 2): "))
            if spaletaju_skaits in [1, 2]:
                break
            else:
                print("Lūdzu ievadi 1 vai 2.")
        except ValueError:
            print("Lūdzu ievadi derīgu skaitli.")

    # Ievada minēšanas diapazonu
    min_diapazons = ievadi_skaitli_robeza("Ievadi minēšanas diapazona sākumu: ", -float('inf'), float('inf'))
    max_diapazons = ievadi_skaitli_robeza("Ievadi minēšanas diapazona beigas: ", min_diapazons, float('inf'))

    # Ievada mēģinājumu skaitu
    meginasanas_skaits = ievadi_skaitli_robeza("Ievadi mēģinājumu skaitu: ", 1, float('inf'))

    # Ievada spēlētāju vārdus
    speletaji = []
    for i in range(spaletaju_skaits):
        vards = input(f"Ievadi spēlētāja {i + 1} vārdu: ")
        speletaji.append(vards)

    # Izvēlas uzminamo skaitli
    if spaletaju_skaits == 1:
        uzminamais_skaitlis = random.randint(min_diapazons, max_diapazons)
        print(f"Uzmini skaitli no {min_diapazons} līdz {max_diapazons}. Tev ir {meginasanas_skaits} mēģinājumi.")

        for i in range(meginasanas_skaits):
            meginajums = ievadi_skaitli_robeza(f"{speletaji[0]}, ievadi savu minējumu: ", min_diapazons, max_diapazons)

            if meginajums < uzminamais_skaitlis:
                print("Pārāk mazs!")
            elif meginajums > uzminamais_skaitlis:
                print("Pārāk liels!")
            else:
                print(f"Apsveicu, {speletaji[0]}! Tu uzminēji skaitli {uzminamais_skaitlis}, {i + 1} mēģinājumos!")
                break
        else:
            print(f"Diemžēl, {speletaji[0]}, tu neuzminēji skaitli. Pareizais skaitlis bija {uzminamais_skaitlis}.")
    else:
        uzminamie_skaitli = []
        for speletajs in speletaji:
            skaitlis = ievadi_noslēpto_skaitli(f"{speletajs}, ievadi savu izvēlēto skaitli, ko pretinieks minēs ({min_diapazons}-{max_diapazons}): ", min_diapazons, max_diapazons)
            uzminamie_skaitli.append(skaitlis)

        uzmineti_skaitli = [False, False]
        uzminets_meginajumos = [0, 0]

        for i in range(meginasanas_skaits):
            for j, speletajs in enumerate(speletaji):
                if not uzmineti_skaitli[j]:
                    pretinieks = speletaji[1 - j]
                    meginajums = ievadi_skaitli_robeza(f"{speletajs}, mēģini uzminēt {pretinieks} izvēlēto skaitli: ", min_diapazons, max_diapazons)

                    if meginajums < uzminamie_skaitli[1 - j]:
                        print("Pārāk mazs!")
                    elif meginajums > uzminamie_skaitli[1 - j]:
                        print("Pārāk liels!")
                    else:
                        print(f"Apsveicu, {speletajs}! Tu uzminēji {pretinieks} izvēlēto skaitli {i + 1} mēģinājumos!")
                        uzmineti_skaitli[j] = True
                        uzminets_meginajumos[j] = i + 1

            if all(uzmineti_skaitli):
                break

        if uzmineti_skaitli[0] and uzmineti_skaitli[1]:
            if uzminets_meginajumos[0] == uzminets_meginajumos[1]:
                print("Neizšķirts! Abi spēlētāji uzminēja pareizo skaitli ar vienādu mēģinājumu skaitu.")
            else:
                uzvaretajs = speletaji[0] if uzminets_meginajumos[0] < uzminets_meginajumos[1] else speletaji[1]
                print(f"Apsveicu, {uzvaretajs}! Tu esi uzvarētājs.")
        elif uzmineti_skaitli[0]:
            print(f"Apsveicu, {speletaji[0]}! Tu esi uzvarētājs.")
        elif uzmineti_skaitli[1]:
            print(f"Apsveicu, {speletaji[1]}! Tu esi uzvarētājs.")
        else:
            print("Diemžēl neviens no spēlētājiem neuzminēja pareizo skaitli.")
            for i, speletajs in enumerate(speletaji):
                print(f"{speletaji[i]} izvēlētais skaitlis bija {uzminamie_skaitli[i]}.")

#print("Esi sveicināts spēlē "Uzmini skaitli!"!")
# Palaiž spēli
uzmini_skaitli()
