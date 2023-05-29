import random                                                                       
snake = [{'X': random.randint(1,58), 'Y': random.randint(1,28)}]                    #Random generálunk a kígyónak egy kezdőpontot
cherry = {}                                                                         
play = True                                                                         #Engedélyezzük a játékmenetet

def cherryGen():                                                                    #Létrehozzuk azt a függvényt amivel elhelyezünk egy cseresznyét egy random pozícióban
    global snake, cherry                                                            
    x = random.randint(1,58)                                                                                                                
    y = random.randint(1,28)                                                        
    pos = False
    for i in snake:                                                                 #Ellenőrizzük hogy a cseresznye nem a kígyóba generálódott
        if i['X'] == x and i['Y'] == y:
            pos = True
    if pos == True:                                                                 #Ha a cseresznye a kígyóba generálódott akkor újraindítjuk a függvényt
        cherryGen
    else:                                                                           #Ha a cseresznye megfelelő helyre generálódott akkor megadjuk az új pozícióját
        cherry['X'] = x
        cherry['Y'] = y


def map():                                                                          #Létrehozzuk azt a függvényt amely létrehozza a játék pályát illetve elhelyezi azon a kígyót és a cseresznyét
    global snake
    global cherry
    for i in range(30):
        line = ""                                                                   #Elkészítjük az új üres sort
        if i == 0 or i == 29:                                                       #Ellenőrizzük hogy a sor az első vagy az utolsó sor e, ezekben az esetekben feltöltjük a sort * karakterekkel  
            for j in range(60):                                         
                pos = False
                for k in snake:                                                     #Ellenőrizzük hogyha a kígyó neki ment a falnak, amenyiben igen, akkor az adott ponton kicseréljük a falat jelző * -ot @ -ra, a kígyó falnak ütközésének jobb láthatósága érdekében
                    if k['X'] == j and k['Y'] == i:
                        line = f"{line}@"
                        pos = True
                if pos == False: 
                    line = f"{line}*"                                               #Feltöltjük a sort * karakterekkel

        else:                                                                       #Amenyiben a sor nem az első vagy az utolsó akkor feltöltjük a sort a megfelelő karakterekkel
            for j in range(60):
                pos = False
                for k in snake:                                                     
                    if k['X'] == j and k['Y'] == i:                                 #Ellenőrizzük hogy a sorban hova kell elhelyezni a kígyót szimbolizáló @ -ot
                        pos = True
                if pos == True:
                    line = f"{line}@"                                               
                elif i == cherry['Y'] and j == cherry['X']:                         #Ellenőrizzük hogy a sorban hova kell elhelyezni a cseresznyét szimbolizáló O -ot
                    line = f"{line}O"                                              
                elif j == 0 or j == 59:                                             #A sor első és utolsó karaktere *, ezzel jelezve a pálya széleit
                    line = f"{line}*"
                else:
                    line = f"{line} "                                               #A sorban a maradék helyet kitöltjük space -ekkel
        
        print(line)
def move():                                                                         #Létrehozzuk azt a függvényt amely kezeli a kígyó helyzetét, növeli a kígyó hosszát amennyiben az megeszik egy cseresznyét, illetve véget vet a játéknak ha a kígyó neki megy a falnak vagy önmagának, vagy ha a játékos megunja a játékot
    global snake, cherry, play  
    direction = input("Hova?\n")                                                    #Bekérjük a felhasználótól az új utasítás a program számára
    match direction:                                                                #Megnézzük melyik parancsot használta a játékos
        case 'fel':                                                                 #Kígyó mozgatása felfelé
            way = {'X': snake[0]['X'], 'Y': snake[0]['Y'] - 1}
        case 'le':                                                                  #Kígyó mozgatása lefelé
            way = {'X': snake[0]['X'], 'Y': snake[0]['Y'] + 1}
        case 'jobbra':                                                              #Kígyó mozgatása jobbra
            way = {'X': snake[0]['X'] + 1, 'Y': snake[0]['Y']}
        case 'balra':                                                               #Kígyó mozgatása balra
            way = {'X': snake[0]['X'] - 1, 'Y': snake[0]['Y']}
        case 'meguntam':                                                            #Játékmenet befejezése ha a játékos megunta azt
            way = {'X': snake[0]['X'], 'Y': snake[0]['Y']}
            play = False                                                            
    if way['X'] >= 59 or way['X'] <= 0 or way['Y'] >= 29 or way['Y'] <= 0:          #Ellenőrizzük hogy a kígyó falnak ütközött
        play = False                                    
        snake.pop()                         

    elif way in snake:                                                              #Ellenőrizzük hogy a kígyó önmagának ütközött
        play = False

    else:                                                                           #Ellenőrizzük hogy a kígyó megevett e egy cseresznyét, és növeljük a méretét
        if way['X'] == cherry['X'] and way['Y'] == cherry['Y'] and play == True:
            cherryGen()
        else:
            if play == True:
                snake.pop()
    snake.insert(0, way)                                                            #kígyó mozgatása a megadott
        

cherryGen()                                                                         #meghívjuk a CherryGen és map fügvényeket a játék elején
map()

while play == True:                                                                 #Elindul a játék a move és map függvények sorozatával
        move()
        map()
print("Most ennyi volt, szép napot!")                                               #Kilépés előtt elköszönünk