knowledgeBase = {
    'owner':"ABC",
    "location":"ccc",
    "time":"24*7"
}

menu = [
    ['Vada Pav',15],
    ['Maggi',30],
    ['Cold Coffie',25]
]

orders = []
total = 0

def displayMenu():
    for i in menu:
        print(i[0],"  |  ",i[1])

def takeOrder():
    displayMenu()
    ord = int(input("PLS GIVE YOUR ORDER = "))
    qty = int(input("PLS ENTER QUANTITY  = "))
    if ord<=3 and ord>0:
        print("YOUR ORDER --> ",menu[ord-1][0], qty)
        orders.append([menu[ord-1][0],menu[ord-1][1],qty,menu[ord-1][1]*qty])
    else:
        print("WRONG INPUT")

def genrateBill():
    if len(orders):
        for i in orders:
            print(i[0],"  |  ",i[1], "  |  ",i[2],"  |  ",i[3])
    else:
        print("\n\nYou hav not given any order")

print("\n\n\n ===== Hotel Anapurna =====\n")
while(True):
    ch = int(input("\n1.Take Order\n2. Genrate Bill\n3.Know More\n4. Exit\n-->"))  
    if ch==1:
        takeOrder()
        flag = input("\n\nDO YOU WANT TO GIVE MORE ORDER")
        while(flag=="y" or flag=="Y"):
            takeOrder()
            flag = input("DO YOU WANT TO GIVE MORE ORDER")
    if ch== 2:
        genrateBill()
    if ch==3:
        while True:
            query = input("\nWHAT DO YOU WANTV TO KNOW? = ")
            if query=="quit":
                break
            query = query.lower()
            matchedKey = [i for i in query.split() if i in list(knowledgeBase.keys())]
            for i in matchedKey:
                if i=="time":
                    print(f"We are open at {knowledgeBase[i]}")
                elif i=="location":
                    print(f"We are at {knowledgeBase[i]}")
                elif i=="owner":
                    print(f"Our owner is {knowledgeBase[i]}")
            if len(matchedKey)==0:
                    print("Don't have knowledge")
    if ch==4:
        break
