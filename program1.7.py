#Prime numbers

quantity=0
n=int(input("Number: "))
while n!=0:
    prime=True
    for i in range(2, n):
        if n%i==0:
            prime=False
            break
    if prime:
        quantity+=1
    n=int(input("Number:"))
print("Prime:",quantity)
