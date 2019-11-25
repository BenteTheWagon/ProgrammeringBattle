def insertionSort(case):
    #jeg  starter med at definerer funktionen insertionSort
    for i in range(1, len(case)):
        #Den tager den 1 i (index) af længden af listen/casen
        #Det betyder at den kører igennem hvert eneste index i listen/casen fra det første index til det sidste i listen
        curNum = case[i]
        #Current nummer som algoritmen tager = i
        #Så det første nummer den tager fat i bliver index/case [i]
        for j in range(i-1, -1, -1):
            if case[j] > curNum:
                #Hvis case [j] er større end curNum (current nummer) også i (index)
                case[j+1] = case[j]
                #skal der tilføjes +1 casen [j]/den rykker 1 til højre/længere hen i listen

            else:
                #Ellers
                j+=1
                #skal casen [j] tilføjes 1 til current nummer
                break
            case[j]=curNum
                # Hvis ikke nummeret er større, så skal koden tilføje et til det nuværende nummer vi arbejder med
                # så listen bevæger sig længere og længere imod slutningen, og herefter slutte så koden lopper.



def selectionSort(case):
    #Jeg definerer selectionSort som en case/index
    for i in range (0, len(case) - 1):
        #Den tager den 1 i (index) af længden af listen/casen og tager 1 fra da python tæller fra 0,1,2,3,4,5,6,7,8,9,10 og ikke 1,2,3,4,5,6,7,8,9,10. Så vi får slættet 0 tallet.
        minIndex = i
        # [minIndex] bliver defineret som det første index i listen
        for j in range (i+1, len(case)):
            if case[j] < case [minIndex]:
                #Hvis case [J] altså det andet index er mindre end det første index [minIndex]
                minIndex = j
                #Skal [J] overtage i [minIndex] plads i listen

        if minIndex != i:
            case[i], case[minIndex] = case[minIndex], case [i]
            #Hvis [minIndex] ikke = i så skal [minIndex] bytte plads med [i]



#Følgende er en test for at se om vores algoritmerne kan sortere både tekst og tal rigtigt.
#Fjern indent på testPrint() for test
def testPrint():
    list1 = ['b','j','q','d','k','d','y','x','b','n','m','u','l','a','w','q','e','m']
    list2 = [9,5,0,5,1,3,4,2,9,3,6,9,1,7,9,6,6,1]
    #Her laver jeg 2 lister, en med bogstaver og 1 med tal
    insertionSort(list1)
    print ("Insertion sort, Liste 1:")
    print (list1)
    insertionSort(list2)
    print ("Insertion sort, Liste 2:")
    print (list2)
    selectionSort(list1)
    print ("Selection sort, Liste 1:")
    print (list1)
    selectionSort(list2)
    print ("Insertion sort, Liste 2:")
    print (list2)
testPrint()
#Her printer jeg alle svarende ud fra henholdvis hver liste til hver sorterings algoritme
