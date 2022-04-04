with open("zgo-cela.txt", "r", encoding="utf-8") as f:
    zapisi = f.read().splitlines()

zapisi = [zapis for zapis in zapisi if len(zapis) >0 and len(zapis)<3]
with open("zgo-cela-parsed.txt", "w", encoding="utf-8") as f:
    for i, zapis in enumerate(zapisi):
        if(i%8 == 0):
            f.write("\n")
        f.write(zapis + " ")
