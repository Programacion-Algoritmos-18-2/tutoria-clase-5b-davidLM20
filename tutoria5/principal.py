from mipaquete.modelo import *# se inporta todo lo de paquete

p = Pais()  # se crea el objeto de pais
p.setNombre_pais("Ecuador")
p.setCapital("Quito")

est1 = Est_Distancia() # se crea el objeto de estudiante a distancia
est1.setNombre("Jose") # se a;ade un nombre
est1.setApellido("Diaz") # se a;ade un apellido
est1.setCodigo("11012") #se a;ade un codigo
est1.setNum_materias(5) # se a;ade numero de materias
est1.setModulo("Noveno") # se a;ade el modulo
est1.setPais(p)#se a;ade el valor de pais y capital al objeto de estudiante
print(est1.presentar_informacion())
