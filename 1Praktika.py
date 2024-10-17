from collections import Counter
f = ['E', 'A', 'O', 'L', 'S', 'N', 'D', 'R', 'U', 'I', 'T', 'C', 'P', 'M', 'Y', 'Q', 'B', 'H', 'G', 'F', 'V', 'J', 'Ñ', 'Z', 'X', 'K', 'W']

def textuaren_letrak_zenbatu(textua):
    t = textua.upper()
    hizkiak = [char for char in t if char.isalpha()]
    frekuentziak = Counter(hizkiak)
    hizkiOrdenatuak = frekuentziak.most_common()
    zerrenda = [hizkia for hizkia, count in hizkiOrdenatuak]
    return zerrenda

def hizkiak_ordezkatu(textua):
    hizkiak_ord = textuaren_letrak_zenbatu(textua)
    textu_berria = []
    
    for char in textua.upper():
        if char in hizkiak_ord:
            index = hizkiak_ord.index(char)
            if index < len(f):
                textu_berria.append(f[index])
            else:
                textu_berria.append(char)
        else:
            textu_berria.append(char)

    return "".join(textu_berria)

def hiztegia_sortu(textu_berria):
    hiztegia = {hizkia: hizkia for hizkia in textu_berria}
    return hiztegia

def textua_deszifratu(textua, hiztegia):
    textu_berria = []
    for char in textua.upper():
        if char in hiztegia:
            textu_berria.append(hiztegia[char])
        else:
            textu_berria.append(char)
    
    return "".join(textu_berria)

def hizkiak_aldatu(textua, hiztegia):
    while True:
        erantzuna = input("Textua aldatu nahi duzu? (bai/ez)")
        if erantzuna == "bai":
            zaharra = input("Sartu aldatu nahi duzun hizkia: ").upper()
            berria = input("Sartu hizki berria: ").upper()
            if len(zaharra) == 1 and len(berria) == 1 and zaharra.isalpha() and berria.isalpha():
                if zaharra in hiztegia.values() or berria in hiztegia.values():
                    for key, value in hiztegia.items():
                        if value == zaharra:
                            hiztegia[key] = berria
                        elif value == berria:
                            hiztegia[key] = zaharra
                else:
                    hiztegia[zaharra] = berria

                textu_berria = textua_deszifratu(textua, hiztegia)
                print(textu_berria)
            
            else:
                print("Hizkiak soilik sartu ditzakezu.")

        elif erantzuna == "ez":
            print("Ez dira aldaketa gehiago egingo.")
            break

        else:
            print("Erantzun baliogabea. Jarri bai edo ez mesedez.")

def main():
    textua = input("Sartu textu bat: ")
    t = hizkiak_ordezkatu(textua)
    print(t)
    h = hiztegia_sortu(t)
    hizkiak_aldatu(t, h)

main()
