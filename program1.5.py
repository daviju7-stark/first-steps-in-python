#program that allows to process amounts 

total=0
amount=float(input("Amount of a sale:$"))
while amount!=0: 
    if amount<0:
        print("Amount no valid")
    else: 
        total+= amount
    amount=float(input("Amount of a sale:$"))
if total>1000:
    total-=total*0.1 #Percentage 
print("Total amount to pay: $",total)    


