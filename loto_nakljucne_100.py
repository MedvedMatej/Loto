import itertools
import random
from scipy.special import comb
import time
import sys

st = time.time()

for j in range(100):
    stevilke = [stev for stev in range(1,40)]
    random.shuffle(stevilke)
    stevilke = stevilke[:31]
    vse_kombinacije = list(itertools.combinations(stevilke,7))
    random.shuffle(vse_kombinacije)
    izbrane = set()
    for e,kombinacija in enumerate(vse_kombinacije):
        ujemanje = False
        for i in izbrane:
            if len(set(kombinacija).intersection(i)) > 3:
                ujemanje = True

        if not ujemanje:
            izbrane.add((kombinacija))
            sys.stdout.write("\r Izbranih kombinacij: {}. Preveril {} od {} kombinacij.".format(len(izbrane),e, len(vse_kombinacije)))
            sys.stdout.flush()
            
    with open("./kombinacije/kombinacije1-random-{}.txt".format(j), "w", encoding="utf-8") as f:
        for kombinacija in izbrane:
            f.write(str(kombinacija) + "\n")
        print("\nZapisanih {} kombinacij v {:.2f} sekundah.\n Smo na iteraciji {}.\n".format(len(izbrane),time.time()-st,j))