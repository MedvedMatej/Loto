import random
from scipy.special import comb
import time
import sys

stevilke = [stev for stev in range(1,32)]
#stevilke = [3,4,5,7,10,11,13,15,16,17,19,20,22,23,27,29,30]
vse_kombinacije = set()

st = time.time()
while len(vse_kombinacije) < comb(len(stevilke),7):
    nova = set()
    while len(nova) < 7:
        nova.add(stevilke[random.randint(0,len(stevilke)-1)])

    dolzina = len(vse_kombinacije)
    vse_kombinacije.add(tuple(nova))
    if dolzina != len(vse_kombinacije):
        sys.stdout.write("\rŠtevilo kombinacij: " + str(len(vse_kombinacije)) + " od " + str(comb(len(stevilke),7)))
        sys.stdout.flush()
    
print(" Generacija kombinacij traja {} sekund".format(time.time()-st))
izbrane = set()
for kombinacija in vse_kombinacije:
    ujemanje = False
    for i in izbrane:
        if len(set(kombinacija).intersection(i)) > 4:
            ujemanje = True

    if not ujemanje:
        izbrane.add((kombinacija))
        sys.stdout.write("\r Izbranih kombinacij: {}".format(len(izbrane)))
        sys.stdout.flush()
        
with open("kombinacije1-ujemanje4.txt", "w", encoding="utf-8") as f:
    for kombinacija in izbrane:
        f.write(str(kombinacija) + "\n")
    print("\nZapisanih {} kombinacij v {:.2f} sekundah.".format(len(izbrane),time.time()-st))