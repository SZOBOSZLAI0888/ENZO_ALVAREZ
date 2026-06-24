def mostrar_menu():
    print(":::::::::::::::MENU::::::::::::::::")
    print("1. agregar estudiante")
    print("2. buscar estudiante")
    print("3. eliminar estudiante")
    print("4. actualizar estados")
    print("5. mostrar estudiantes")
    print("6. salir")
    print(":::::::::::::::::::::::::::::::::::")
    
    
def leer_opcion():
    while True:
        try:
            opcion=int(input("ingrese alguna opcion : "))
            if 1 <= opcion <= 6:
                    return opcion
            else:
                    print("error debe ingresar un numero entre 1 y 6")
        except ValueError:
                print("error debe ingresar un dato numerico entero")
                
                
def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_edad(edad):
    return edad > 0

def validar_nota(nota):
    return 1.0 <= nota <= 7.0


def agregar_estudiante(estudiantes):
    nombre=input("ingrese nombre del estudiante : ")
    if not validar_nombre(nombre):
        print("error el nombre no puede estar vacio")
        return
    try:
        edad=int(input("ingrese la edad del alumno : "))
    except ValueError:
        print("error la edad debe ser un numero entero")
        return
    if not validar_edad(edad):
        print("error la edad debe ser mayor que 0")
    try:
        nota=float(input("ingrese nota : "))
    except ValueError:
        print("error la nota debe ser un numero decimal")
        return
    if not validar_nota(nota):
        print("error la nota debe estar entre 1.0 y 7.0")
        
    estudiante = {"nombre":nombre,
                  "edad":edad,
                  "nota":nota,
                  "aprobado":False
                  }
    
    estudiantes.append(estudiante)
    print("estudiante agregado correctamente")
    
    
def buscar_estudiante(estudiantes,nombre):
    
    for posicion in range(len(estudiantes)):
        if estudiantes[posicion]["nombre"] == nombre:
            return posicion
        return -1
    
    
def eliminar_estudiante(estudiantes):
    nombre=input("ingrese el nombre del alumno que desea eliminar: ")
    posicion=buscar_estudiante(estudiantes,nombre)
    
    if posicion != -1:
        estudiantes.pop(posicion)
        print("estudiante eliminado correctamente")
    else:
        print("el estudiante '{nombre}' no se encuentra registrado")
        
        
def actualizar_estados(estudiantes):
    for estudiante in estudiantes:
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"]=True
        else:
            estudiante["aprobado"]=False
            
            
def mostrar_estudiantes(estudiantes):
    actualizar_estados(estudiantes)
    print(":::::: LISTA DE ESTUDIANTES ::::::")
    
    if len(estudiantes)==0:
        print("no hay estudiantes registrados")
        return
    
    for estudiante in estudiantes:
        estado = "aprobado"
        
        if not estudiante["aprobado"]:
            estado = "reprobado"
            
        print("nombre: {estudiante}['nombre']")
        print("edad: {estudiante['edad']}")
        print("nota: {estudiante['nota']}")
        print("estado: {estado}")
        
        
estudiantes = []

while True:
    mostrar_menu()
    opcion=leer_opcion()
    
    if opcion == 1:
        agregar_estudiante(estudiantes)
    elif opcion == 2:
        nombre = input("ingrese nombre que desea buscar : ")
        posicion = buscar_estudiante(estudiantes,nombre)
        if posicion != -1:
            estudiante = estudiantes[posicion]
            print("estudiante encontrado")
            print("posicion:",posicion)
            print("nombre:",estudiante["nombre"])
            print("edad:",estudiante["edad"])
            print("nota:",estudiante["nota"])
            print("aprobado:",estudiante["aprobado"])
            
        else:
            print("estudiante no encontrado")
    elif opcion == 3:
        eliminar_estudiante(estudiantes)
    elif opcion == 4:
        actualizar_estados(estudiantes)
        print("estados actualizados correctamente")
    elif opcion == 5:
        mostrar_estudiantes(estudiantes)
    elif opcion == 6:
        print("gracias por usar nuestro sistema vuelva pronto.......")
        break
        
        

        
    
              
    
            

         
                
            