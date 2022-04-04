from collections import defaultdict
tip = ["7  ", "6+1", "6  ", "5+1", "5  ", "4+1", "4  ", "3+1"]
with open("./vrednosti_zadetkov.txt", "r", encoding="utf-8") as f:
    zadetki = f.read().splitlines()

    avg = defaultdict(float)
    for i, zadetek in enumerate(zadetki):
        avg[i%8] += float(zadetek.strip().split(" ")[-2].replace(".", "").replace(",","."))*8/len(zadetki)

    with open("./povprecni_zadetki.txt", "w", encoding="utf-8") as fw:
        for k,v in avg.items():
            fw.write("{} : {:.2f}\n".format(tip[k],v))

