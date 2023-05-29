from tkinter import *
import random
pizzak = []
rendelés = {'size': "", 'pizza': "", 'feltet': [], 'udito': None}
size = ["24","32","45","kicsi","közepes","nagy"]

with open("pizza.csv", "r", encoding="UTF-8") as file:
    sorok = file.readlines()
    for sor in sorok:
        cv = {}
        sor = sor.split(";")
        cv["nev"] = sor[0]
        sor.pop(0)
        for n,i in enumerate(sor):
            cv[str(n)] = i.rstrip()
        pizzak.append(cv)

with open("feltetek.csv", "r", encoding="UTF-8") as file:
    sor = file.readline()
    feltetek = sor.split(";")

with open("uditok.csv", "r", encoding="UTF-8") as file:
    sor = file.readline()
    uditok = sor.split(";")





def similarity(text,list):
    szavak = text.split()
    words = []
    for i in szavak:
        for j in list:
            common = set(i) & set(j)
            sim = len(common) / max(len(i), len(j)) * 100
            if sim >= 65:
                words.append(j)
    return words
    
    
def search(text):
    global rendelés, size, feltetek
    text = text.lower()

    for i in size:
        if i in text:
            match i:
                case "24" | "kicsi":
                    rendelés["size"] = "kicsi"
                case "32" | "közepes":
                    rendelés["size"] = "közepes"
                case "45" | "nagy":
                    rendelés["size"] = "nagy"
    

    rendelés['feltet'] = similarity(text, feltetek)
    rendelés['udito'] = similarity(text, uditok)



ans = random.choice(["Üdvözöljük a pizzériánkban! Miben segíthetek Önnek ma?", "Szívesen látjuk a pizzériánkban! Milyen ízletes pizzát szeretne rendelni?", "Jó napot! Nagyszerű, hogy benézett hozzánk! Mit választana a mennyei pizzáink közül?", "Üdvözöljük! Reméljük, jóllakottan távozik majd tőlünk. Mivel lephetjük meg?", "Jó reggelt! A nap bármely szakában örömmel látjuk vendégül. Hogyan segíthetünk ma a pizza kiválasztásában?"])
chat = True
while chat == True:
    bemenet = input(f"{ans}\n")
    search(bemenet)
    if rendelés['size'] == "":
        ans = random.choice(["Milyen méretű pizzát szeretne rendelni: kicsi, közepes vagy nagy?","A pizzája milyen méretű legyen: kicsi, normál vagy nagy?","Kérem, mondja meg, hogy mekkora pizzát szeretne rendelni: 24cm, 32cm, 45cm"])

    elif len(rendelés['udito']) == 0:
        ans = random.choice(["Milyen üdítőt szeretne rendelni a pizzája mellé? Van valamilyen kedvenc itala?", "Az étel mellé milyen folyadékot szeretne rendelni: klasszikus kólát, sprite-ot, vizet, vagy netán fantát?"])

    elif len(rendelés['feltet']) == 0:
        ans = random.choice(["Milyen feltéteket szeretne a pizzájára? Van valamilyen kedvenc feltéte vagy speciális ízlési igénye?","Milyen feltéteket szeretne a pizzára?","Kérem, mondja meg, milyen típusú feltétekkel szeretné ellátni a pizzáját: húsok, zöldségek, sajtok vagy egyéb extra összetevők?"])

    else: chat = False

text = ""
text2 = ""
for i in rendelés["feltet"]:
    text = f"{i} "
for i in rendelés["udito"]:
    text2 = f"{i} "

final = f"Ön egy {rendelés['size']} méretű pizzát rendelt, {text}feltétekkel, és {rendelés['udito']}üditővel!"
print(final)
