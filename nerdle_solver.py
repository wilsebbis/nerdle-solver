from itertools import permutations
from collections import OrderedDict

#use (9*8-7=65)
#then use (0+12/3=4)

# a bit slow
# i also made it so that it only uses a max of 2 of the same number or operator
# because cartesian product was even slower
# so if there are three of the same number in one nerdle
# then you're out of luck

G = ["NA","NA","NA","NA","NA","NA","NA","NA"]
unknown = 8
R = [[],[],[],[],[],[],[],[]]
H = []
B = []
used_words = []

for p in range(6):
    U = []
    list_of_lists = []
    letters = input("Input equation as string: ")
    colors = input("Input colors as string Red Black Green (eg. RRBGB): ")
    if(colors == "GGGGGGGG"):
        print("Congrats!")
        exit()
    used_words.append(letters)
    def Convert(string):
        list1=[]
        list1[:0]=string
        return list1
    letterlist = Convert(letters)
    colorlist = Convert(colors)
    for i in range(len(letterlist)):
        if(letterlist[i] == "="):
            letterlist[i] = "=="
    for i in range(len(letterlist)):
        if(colorlist[i] == "G"):
            if G[i] != letterlist[i]:
                G[i] = letterlist[i]
                unknown -= 1
        if(colorlist[i] == "R"):
            R[i].append(letterlist[i])
            H.append(letterlist[i])
        if(colorlist[i] == "B"):
            if(letterlist[i] not in H):
                B.append(letterlist[i])
        
    equation_list1 = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/","=="]
    equation_list2 = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/"]
    equation_list = equation_list1 + equation_list2

    for i in range(len(equation_list)):
        if equation_list[i] not in B:
            U.append(equation_list[i])

    def read(list):
        return eval(''.join(list))

    def newthing(list):
        new_list = G.copy()
        k = 0
        for i in range(len(new_list)):
            if(new_list[i] == "NA"):
                new_list[i] = list[k]
                k += 1
        if (new_list[0].isdigit() and new_list[7].isdigit()):
            flag2 = 0
            for t in range(len(new_list) - 1):
                if(new_list[t].isdigit()==False and new_list[t+1].isdigit()==False):
                    flag2 = 1
                if(new_list[t] == "/" and new_list[t+1] == "0"):
                    flag2 = 1
                if(new_list[t] == "0" and new_list[t+1].isdigit()):
                    flag2 = 1
            if flag2 == 0:
                result = read(new_list)
                if result == True and new_list[0] not in R[0] and new_list[1] not in R[1] and new_list[2] not in R[2] and new_list[3] not in R[3] and new_list[4] not in R[4] and new_list[5] not in R[5] and new_list[6] not in R[6] and new_list[7] not in R[7]:
                    flag = 0
                    for j in range(len(H)):
                        if H[j] not in new_list:
                            flag = 1
                    if flag == 0:
                        list_of_lists.append(''.join(new_list))

    combos = permutations(U, unknown)
    hello = list(combos)
    print(hello)
    for i in range(len(hello)):
        newthing(list(hello[i]))

    semi_final_list = list(OrderedDict.fromkeys(list_of_lists))
    final_list = []
    for i in range(len(semi_final_list)):
        if(semi_final_list[i] not in used_words):
            final_list.append(semi_final_list[i])
    print(final_list)