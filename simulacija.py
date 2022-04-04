with open("kombinacije1-ujemanje2.txt", "r", encoding="utf-8") as f:
    kombinacije = f.read().splitlines()
    kombinacije = [{int(st.strip()) for st in kombinacija[1:-1].split(",")} for kombinacija in kombinacije]

with open("povprecni_zadetki.txt", "r", encoding="utf-8") as f:
    avg_zadetki = f.read().splitlines()
    avg_zadetki = { (7-i/2):float(avg.split(":")[1].strip()) for i,avg in enumerate(avg_zadetki)}

with open("zgodovina.txt", "r", encoding="utf-8") as f:
    izzrebane = f.read().splitlines()
    izzrebane = [({int(st) for st in izzrebana.split(" ")[:-1]},int(izzrebana.split(" ")[-1])) for izzrebana in izzrebane]

denar = 0;
for izzrebana,dodatna in izzrebane[:]:
    denar-= 0.6*len(kombinacije)
    for kombinacija in kombinacije:
        di = izzrebana.union(set([dodatna]))
        ujemanje = (len(izzrebana.intersection(kombinacija)) + len(di.intersection(kombinacija)))/2
        if ujemanje > 3:
            print(sorted(izzrebana),dodatna, sorted(kombinacija), ujemanje)
            denar += avg_zadetki[ujemanje]
print(len(kombinacije))
print(denar)