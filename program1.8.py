anioInicio=int(input("Año inicial: "))
anioFinal=int(input("Año final: "))
for anio in range(anioInicio, anioFinal): 
    if not anio%10==0:
        continue
    if not anio%4==0:
        continue
    if anio%100!=0 or anio%400==0:
        print(anio)
