#Diccionarios vacíos 
A=dict()
B={}
#Diccionarios con elementos 
traducciones={"hola":"hello", "adiós":"bye", "día":"day", "noche":"night"}
print(len(traducciones))
calendario=[("enero",1), ("febrero",2), ("marzo",3)]
meses=dict(calendario) #La función dict' tiene mi lista como argumeto
print(type(meses))
print(meses)

for clave in traducciones.keys():
    print(clave)
    
for valor in traducciones.values():
    print(valor)
    
for clave, valor in traducciones.items():
    print(clave, "==>", valor)
    
#Alternativa para acceder al valor 
for clave in traducciones.keys():
    print(clave, "==>", traducciones[clave]) #La clave es como si fuera el índice 

#Con una soloa variable
for par in traducciones.items():
    print(par[0], "--", par[1])
    
    
equipo={7:["Daniel",16,2], 9:["Rulo",16,2], 11:["Farfán",17,1], 4:["Joel",15,3]}
print(len(equipo))
for datos in equipo.values():
    print("nombre:", datos[0],"- edad:",datos[1],"- años en el equipo:",datos[2])


    
    

    

    
    


