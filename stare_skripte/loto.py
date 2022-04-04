import random
from scipy.special import comb
import sys
import time

stevilke = [stev for stev in range(1,25)]
#stevilke = [3,4,5,7,10,11,13,15,16,17,19,20,22,23,27,29,30]
kombinacije = set()
stevilo = 75
if len(sys.argv) > 1:
    stevilo = int(sys.argv[1])

st = time.time()
while len(kombinacije) < stevilo:
    nova = set()
    while len(nova) < 7:
        nova.add(stevilke[random.randint(0,len(stevilke)-1)])

    sys.stdout.write("\rPoskušam: {}".format(str(nova)))
    sys.stdout.flush()

    ujemanje = False
    for kombinacija in kombinacije:
        if len(nova.intersection(kombinacija)) >3:
            ujemanje = True
            break
    
    if not ujemanje:
        kombinacije.add(tuple(nova))
        print("\n"+str(len(kombinacije))+ " " + str(kombinacije))


with open("kombinacije.txt", "w", encoding="utf-8") as f:
    for kombinacija in kombinacije:
        f.write(str(kombinacija) + "\n")
    print("\nZapisanih {} kombinacij v {:.2f} sekundah.".format(len(kombinacije),time.time()-st))