number = int(input("Number:"))
f=1
if number != 0:
    for i in range(1, number+1):
        f = f*i

print("Factorial:",f)

