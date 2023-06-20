from time import *
from tabulate import tabulate


stock=[[50, "LAYS Blue"], [50, "LAYS Green"], [50, "LAYS Yellow"], [50, "LAYS Red"], [0, "Dairymilk XL"],
       [20, "Dairymilk L"], [20, "Dairymilk M"], [20, "Dairymilk S"],[30, "Iced Tea XL"], 
       [30, "Iced Tea L"], [30, "Iced Tea M"], [30, "Iced Tea S"], [15, "Bourbon "], 
       [15, "Crack Jack "], [15, "Hide & Seek "], [15, "Jim Jam "] ]

itemcode = [[1, "LAYS Blue", 30], [2, "LAYS Green", 30], [3, "LAYS Yellow", 30], [4, "LAYS Red", 30],[5,"Dairymilk XL", 150],[6, "Dairymilk L", 100], [7, "Dairymilk M", 80], [8, "Dairymilk S", 30], 
[9, "Iced Tea XL", 100], [10, "Iced Tea L", 80], [11, "Iced Tea M",60], [12, "Iced Tea S", 40], 
[13, "Bourbon ", 50], [14, "Crack Jack ",50], [15, "Hide & Seek ",50], [16, "Jim Jam ",50] ]

amount = 5000

print("---------------------VENDING MACHINE---------------------")
sleep(1)

vending_machine= [("LAYS Blue ","LAYS Green","LAYS Yellow ","LAYS Red"), ("Rs. 30","Rs. 30","Rs. 30","Rs. 30"), ("CODE 1", "CODE 2", "CODE 3", "CODE 4")
        ,("", "", "", "", ""), ("Dairymilk XL", "Dairymilk L ", "Dairymilk M ", "Dairymilk S "), ("Rs. 150", "Rs. 100", "Rs. 80", "Rs. 30"), ("CODE 5", "CODE 6", "CODE 7", "CODE 8")
        ,("", "", "", "", "") ,("Iced Tea XL", "Iced Tea L ", "Iced Tea M ", "Iced Tea S "), ("Rs. 100", "Rs. 80", "Rs. 60", "Rs. 40"), ("CODE 9", "CODE 10", "CODE 11", "CODE 12")
        ,("", "", "", "", "") ,("Bourbon ", "Crack Jack ", "Hide & Seek ", "Jim Jam "), ("Rs. 50", "Rs. 50", "Rs. 50", "Rs. 50"), ("CODE 13", "CODE 14", "CODE 15", "CODE 16")]

print(tabulate(vending_machine, tablefmt=""))

def selection():
    print("What do you want to have today?")
    sleep(1)
    global item
    item= int(input("Enter the item code here: "))

    global itemname
    for i in itemcode:
        if i[0] == item:
            itemname = i[1]
            print(f"You've selected {itemname} for Rs.{i[2]}. Checking if we are stocked up...")
            sleep(2)
            if itemname in [i[1] for i in stock if i[0]>0]:
                print(f"We're stocked with {itemname}")
                sleep(2)
            else:
                print(f"We're out of {itemname}")
                sleep(1)
                print("You can select anything else you like.")
                selection()
            
selection()


def payment():
    global notes
    global coins
    global amount
    print("Enter the value of notes and coins you will insert.")
    notes=int(input(("Denomination with Notes: ")))
    coins=int(input(("Denomination with Coins: ")))
    print("Insert Money.")
    sleep(3)
    money= coins+notes
    sleep(2)
    
    for i in itemcode:
        if i[1] == itemname:
                price=i[2]
                if money==price:
                    print("Processing payment...")
                    amount= amount+ money
                    sleep(2)
                    print("Payment successful!")
                    order=True
                elif money>price:
                    change= money-price
                    sleep(2)
                    print(f"Processing change of {change}...")
                    amount+= money
                    amount-= change
                    sleep(2)
                    print("Change withdrawn successfully!")
                    sleep(1)
                    print("Payment successful!")
                    order= True
                else:
                    print("Amount is not sufficient. Withdrawing...")
                    sleep(1)
                    amount = amount - money
                    print("Payment not successful!")
                    sleep(1)
                    print("Withdrawal of your amount successful! Try again.")
                    order= False
                    payment()
payment()



order= True            
while order == True:
    sleep(2)
    print("Order has been processed and delivered successfully.")
    sleep(2)
    for i in stock:
        if i[1]==itemname:
            i[0]-=1
            order= False
            print(stock)
            print(amount)

                    

        


                
                
            
           




                


