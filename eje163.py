estado_civil = input ("ingrese estado civil (s,c):")
edad= int(input("ingrese su edad:"))
buena_persona = input ("es buena persona? (s,n):")
linda = input ("es linda? (s,n):")
if estado_civil=="c":
    print ("no me caso! ni me comprometo")
elif edad <= 30 and linda =="s" or buena_persona =="s":
    print("si me caso!")
else:
    print ("solo me comprometo")