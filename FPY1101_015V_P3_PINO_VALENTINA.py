import time,os,random
os.system("cls")

#listas
ciudadanos=[]

#definiciones 

#opcion1
def menu():
            print("1.Ingresar NIF")
            print("2.Buscar NIF")
            print("3.Imprimir certificados")
            print("4.Salir")
            

#Registrar ciudadano
#id mas pais

def obtener_NIF():
    
    try:
        pais=input("Ingrese pais de nacimiento: \n").lower()
    except:
        print("Pais no valido, ingrese nuevamente").lower()

    if pais=="españa":
        pais_corto ="SP"
    else:
        pais_corto="UE"

    #nif 

    Nif=input("Ingrese ID(Solo numeros)\n")
    while len(Nif)>9:
        Nif=(input("Ingrese ID(Solo numeros)\n"))
        return Nif

    NIF_str=(Nif)
    nif_final=NIF_str +"-"+ pais_corto
    print(" Tu NIF")
    print(nif_final)
            
#obtener nombre

def obtener_nombre():
    nombre=input("Ingrese su nombre completo\n").lower()
    while len(nombre)<8:
        nombre=input("Ingrese su nombre completo\n").lower()
        return nombre
    
    

#obtener edad
def obtener_edad():
    edad=int(input("Ingrese su edad(debes ser mayor o igual a 15)\n"))
    while edad <15:
        edad=int(input("Ingrese su edad(debes ser mayor o igual a 15)\n"))
        return edad
#fecha de nacimiento
def obtener_fechadenacimiento():
    fecha=input("Ingrese su fecha de nacimiento\n")
    if fecha=="" or " ":
        print("fecha ingresada no valida")
    else:
        print("")
        return fecha
        
def registrar_ciudadano():
    while True:
        id_ciudadano=obtener_NIF()
        nombre_ciudadano=obtener_nombre()
        edad_ciudadano=obtener_edad()
        nacimiento_ciudadano=obtener_fechadenacimiento()
        ciudadano=[id_ciudadano,nombre_ciudadano,nacimiento_ciudadano,edad_ciudadano]
        ciudadanos.append(ciudadano)
        
        print("Ciudadano Registrado")
        print("desea registrar a otro ciudadano?")
        seguir=int(input("1.SI / 2.NO\n"))
        if seguir==1:
            continue
        else:
            break

#opcion2
def mostrar_ciudadano():
    buscar_NIF=input("Ingrese NIF a buscar\n")
    for ciudadano in ciudadanos:
        if buscar_NIF==ciudadano[0]:
            print(f"NIF: {ciudadano[1]}")
            print(f"Nombre: {ciudadano[2]}")
            print(f"Edad: {ciudadano[3]}")
            return
        else:
            print("Ciudadano no registrado")
            return

#opcion3
def imprimir_certificados():
    search_nif= input("Ingrese NIF\n")
    for ciudadano in ciudadanos:
        if search_nif==ciudadano[0]:
            print("Imprimir Certificados")
            print("1.certificado de nacimiento")
            print("2.Certificado conyugal")
            print("3.Pertenencia a la Union Europea")
            try:
                opcion=int(input("Ingrese opcion\n"))
            except:
                print("Opcion no valida")
                
            if opcion==1:
                print("--------Certificado de Nacimiento--------")
                print(obtener_fechadenacimiento)
                time.sleep(2)
                return
            if opcion==2:
                estado_conyugal=input("Ingrese estado conyugal")
                print("--------Certificado Conyugal--------")
                print(estado_conyugal)
                time.sleep(2)
                return
            if opcion==3:
                print("--------Union Europea--------")
                print(f"El ciudadano de NIF {ciudadano[1]}, NOMBRE {ciudadano[2]} es parte de la Union Europea")
                time.sleep(2)
                return

#opcion4
def salir():
    print("Saliendo....")
    time.sleep(2)
    print("*Valentina Pino Norambuena*")
    


#main code
while True:
    print("-------------Registro De Ciudadanos de la Union Europea------------")
    menu()
    opcion=int(input("Ingrese una opcion\n"))
    
    if opcion==1: 
        registrar_ciudadano()

    elif opcion==2:
        mostrar_ciudadano()
        
    elif opcion==3:
        imprimir_certificados()
        
    elif opcion==4:
        salir()
        break
    
    
    
