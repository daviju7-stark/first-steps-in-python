#Constant (Variables constanes)
CAPACITYM2=4
PERCENTAGEBYTIERS=0.2
ESPECIALPERCENTAGE= 0.3
COMMONPERCENTAGE=0.7

#stadium dimensions in square meter (Dimensiones del estadio en metro cuadrado)
dimensions=float(input("Stadium dimensions in square meter:"))
number_of_people=int(input("Number of peaple that can fit in the stands:"))
percentage_of_the_stage=int(input("Porcentage that occupies the stage:"))
m2steps=dimensions*PERCENTAGEBYTIERS
m2stage=dimensions*(porcentage_of_the_stage/100)
m2available=dimensions-m2steps-m2stage
availablepeaple=(m2available*4)+number_of_people
print(availablepeaple,"peaple fit")

#Total sales revenue (Ingreso total de ventas)
especial_price_of_tickets=float(input("Especial price of ticket of the stadium:$"))
normal_price_of_tickets=float(input("Normal price of tickets of the stadium:$"))
print("Total sales revenue:$", 
      (availablepeaple*ESPECIALPERCENTAGE)*especial_price_of_tickets + 
      (availablepeaple*COMMONPERCENTAGE)*normal_price_of_tickets)

