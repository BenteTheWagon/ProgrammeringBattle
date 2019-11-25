def insertionSort(case):
    #jeg definerer insertionSort som en case
    for i in range(1, len(case)):
        #Den tager den 1 i (index) af længden af listen
        curNum = case[i]
        #Current nummer som algoritmen tager = i
        for j in range(i-1, -1, -1):
            if case[j] > curNum:
                #Hvis case [j] er større end curNum (current nummer) også i (index)
                case[j+1] = case[j]
                #skal der tilføjes +1 casen [j]

            else:
                j+=1
                break
            case[j]=curNum




#ellers
#skal casen [j] tilføjes 1 til current nummer


list1 = ['b','j','q','d','k','d','y','x','b','n','m','u','l','a','w','q','e','m']
list2 = ['9','5','0','5','1','3','4','2','9','3','6','9','l','7','9','2','6','1']
#Her laver jeg en liste til test af kode
insertionSort(list1)
insertionSort(list2)
#Her siger jeg at InseritonSort skal bruge (list1)
print (list1)
print (list2)
#Her printer den resultatet af den sorterede liste



def selectionSort(case):
    for i in range (0, len(case) - 1):
        minIndex = i
        for j in range (i+1, len(case)):
            if case[j] < case [minIndex]:
                minIndex = j

        if minIndex != i:
            case[i], case[minIndex] = case[minIndex], case [i]
