def Validar(email): #El nombre/ Usa las misma reglas para una variable | Los parámetros son datos de cualquier tipo y puede tenerlos ilimtadamente o no tenerlos una función 
    caracterBuscado="@" #Cuerpo de la función puede ser tan complejo como queramos  
    emailValido=False 
    for c in email:
        if c==caracterBuscado:
            emailValido=True
    return emailValido

#Programa principal
direccion=input("Tu email: ")
if Validar(direccion):
    print("Dirección Válida")
else:
    print("Dirección inválida")
    