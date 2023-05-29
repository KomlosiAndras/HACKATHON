import sys
symbols = None
cards = []


if len(sys.argv) > 1:                                                                                                   #Ellenőrizzük hogy a felhasználó meg adott e paramétert
    symbols = int(sys.argv[1])                                                                                          #Paraméter kiolvasása
else:
    symbols = input("Helyes használat: dobble.py <n>! Nem adtál meg értéket, ezt itt pótold: ")                         #Ha a felhasználó nem adott meg paramétert akkor bekérünk egyett
    try:                                                                                                                #Ellenőrizzük hogy a paraméter szám
        symbols = int(symbols)
    
    except:
        print("Helytelen érték!")                                                                                       #Ha a megadott paraméter nem szám abba hagyjuk a program futását



for i in range(symbols):                                                                                                #Első n kártya generálása
    card = [1]
    for j in range(symbols-1):
        card.append((j+1)+(i*(symbols-1))+1)
    cards.append(card)                                                                                                  #A generált kártyákat hozzá adjuk a cards listához



for i in range(symbols-1):                                                                                              #Újjab n^2 kártyát generálunk
    for j in range(symbols-1):
        card = [i+2]
        
        for k in range(symbols-1):
            val = (symbols + (symbols-1)*k + (i*k+j)%(symbols-1)) + 1
            card.append(val)
        
        cards.append(card)                                                                                              #A generált kártyákat hozzá adjuk a cards listához


for card in cards:                                                                                                      
    text = ""
    for i in card:                                                                                                      #A kártyák tartalmát szöveges formába rendezzük
        text = f"{text}{i} "
    print(text.rstrip())                                                                                                #Kiírjuk az elkészült kártyákat



def checker(list):                                                                                                      #Ellenörző program, igény szerint ki/be kapcsolható
    correct = True
    for i, card in enumerate(list):                                                                                     
        for j, card2 in enumerate(list):
            if i != j:                                                                                                  #Ellenőrizzük az összes lehetséges kombinációt
                common = set(card) & set(card2)                                                                         #Ellenörizzük az azonos elemeket
                if len(common) > 1:
                    print(f"A(z) {card} kártyának és a(z) {card2} kártyának több közös eleme van: {common}.")           #Kiírjuk azokat az elemeket amelyek nem felelnek meg
                    correct = False
                if len(common) < 1:
                    print(f"A(z) {card} kártyának és a(z) {card2} kártyának nincs közös eleme.")
                    correct = False
    if correct == True:                                                                                                 
        print(f"A dobble pakli megfelelő, bármelyik 2 kártyának egy és csakis egy azonos eleme van!")                   #Ha minden elem megfelelt akkor kiírjuk hogy sikeres volt a generálás


check = False                                                                                                           #Ellenörző funkció ki és be kapcsolása (True/False)

if  check == True:  
    checker(cards)                                                                                                      #Ellenörző funkció meghívása