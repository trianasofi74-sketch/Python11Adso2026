edad = int(input("Ingrese su edad"))
if edad >= 18:
    print ("puede votar")
else:
    if edad >= 17:
       print ("En un año o menos podra votar")
    else:
        print ("No puede votar")