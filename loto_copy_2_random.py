import itertools
import random
from scipy.special import comb
import time
import sys

stevilke = [stev for stev in range(1,40)]
random.shuffle(stevilke)
stevilke = stevilke[:32]

vse_kombinacije = set()

st = time.time()

vse_kombinacije = set(list(itertools.combinations(stevilke,7)))
""" vk = list(itertools.combinations(stevilke,7))
random.shuffle(vk) """

print(" Generacija kombinacij traja {} sekund".format(time.time()-st))
izbrane = set()
for e,kombinacija in enumerate(vse_kombinacije):
    ujemanje = False
    for i in izbrane:
        if len(set(kombinacija).intersection(i)) > 4:
            ujemanje = True

    if not ujemanje:
        izbrane.add((kombinacija))
        sys.stdout.write("\r Izbranih kombinacij: {}. Preveril {} od {} kombinacij.".format(len(izbrane),e, len(vse_kombinacije)))
        sys.stdout.flush()
        
with open("kombinacije1-random-ujemanje4.txt", "w", encoding="utf-8") as f:
    for kombinacija in izbrane:
        f.write(str(kombinacija) + "\n")
    print("\nZapisanih {} kombinacij v {:.2f} sekundah.".format(len(izbrane),time.time()-st))