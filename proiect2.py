fin = open("intrare.txt", 'r')
lista = [int(element) for element in fin.readline().split()]
numar_noduri = lista[0]
numar_muchii = lista[1]
contor = 1
muchii = []
stare_initiala = 0
stare_finala = 0
for linie in fin.readlines():   #am citit datele din fisier
    if contor <= numar_muchii:
        linie = linie.split()
        nod_initial = int(linie[0])
        nod_final = int(linie[1])
        litera = linie[2]
        muchii.append([nod_initial, nod_final, litera])
    elif contor == numar_muchii + 1:
        linie = linie.split()
        stare_initiala = int(linie[0])
    elif contor == numar_muchii + 2:
        linie = linie.split()
        stare_finala = int(linie[0])
    contor += 1
i = 0
indici_folositi = []  
while i < len(muchii) - 1:  #parcurg lista de muchii
    j = i + 1
    nod_stanga_1 = muchii[i][0]
    nod_dreapta_1 = muchii[i][1]
    lit1 = muchii[i][2]
    while j < len(muchii):  #voi verifica daca exista litere care au aceleasi muchii => reuniune
        nod_stanga_2 = muchii[j][0]
        nod_dreapta_2 = muchii[j][1]
        lit2 = muchii[j][2]
        if nod_stanga_1 == nod_stanga_2 and nod_dreapta_1 == nod_dreapta_2:
            print('(' + lit1 + '+', end = "")
            print( lit2 + ')' , end = "")
            indici_folositi.append(i)
            indici_folositi.append(j)   #voi pune i si j intr-o lista ca sa stiu sa sar peste ei mai tarziu, altfel mi se vor repeta literele
        j += 1
    if nod_stanga_1 == nod_dreapta_1 and i not in indici_folositi:  #Kleene
        print(lit1 + '*', end="") 
    else:   #concatenarea
        k = i + 1
        while k < len(muchii):
            nod_stanga_2 = muchii[k][0]
            nod_dreapta_2 = muchii[k][1]
            lit2 = muchii[k][2]
            if nod_dreapta_1 == nod_stanga_2 and i not in indici_folositi:
                print(lit1, end = "")
                break
            k+=1
    i += 1
if muchii[i][1] == stare_finala and muchii[i][0] == muchii[i][1]:
    print(muchii[i][2] + '*')
elif muchii[i][1] == stare_finala :
    print(muchii[i][2])