#Encryted Messages
shifting=int(input("Shifting: ")) #corrimiento/shifting
alphabet="abcdefghijklmnñopqrstuvwxyz"

#Iteramos cinco veces
for i in range(5):
    message=input("Message to encrypt: ")
    encrypted=""
    for caracter in message:
        if caracter.lower() in alphabet:
            indice=alphabet.find(caracter.lower())
            indice=(indice+shifting)%27 #Lo puedo guardar allí porque el indice anterior no lo vamos a volver a utilizar
            encrypted+=alphabet[indice]
        else:
            encrypted+=caracter
    print("***Encrypted message:", encrypted)

 