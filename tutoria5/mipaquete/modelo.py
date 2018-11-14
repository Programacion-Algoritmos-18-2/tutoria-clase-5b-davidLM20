# clase padre: Clase principal de la cual se hereda los atributos generales
class Persona(object):
	# se crea los atributos de la clase que se van a enviar a las demas clases
	def __init__(self):
		self.nombre = ""
		self.apellido = ""
		self.pais = Pais() #esta variable es de tipo pais 

	#se crea los metodos para agregar el nombre y apellido	
	def setNombre(self,n):
		self.nombre = n

	def setApellido(self,a):
		self.apellido = a

	def setPais(self,p):
		self.pais = p	
	#se crea los metodos para retornar los valores de nombre, apellido y Pais	 
	def getNombre(self):
		return self.nombre

	def getApellido(self):
		return self.apellido

	def getPais(self):
		return self.pais

	#metodo que envia la primera cadena esta contiene los valores 	
	def presentar_informacion(self):
		c = "Informacion:\n\tNombres:%s %s" % (self.getNombre(), self.getApellido())
		return c
	
#Esta clase funcionara como padre e hija a su ves pues hereda atributos de Persona y envia atributos a las otra dos clases
class Estudiante(Persona):
	def __init__(self):
		#se hereda los atributos de persona
		super(Estudiante, self).__init__()
		#se crea el atributo codigo que se enviara a las otras dos clases
		self.codigo = ""

	#se crea el metodo para agregar el codigo
	def setCodigo(self,c):
		self.codigo = c
	#se crea el metodo para retornar el codigo	
	def getCodigo(self):
		return self.codigo

	# se crea un metodo para enviar la informacion esta ya contiene la informacion de clase persona	
	def presentar_informacion(self):
		c = "%s\n\tCodigo:%s\n\tProcedencia: pais: %s capital:%s" % (super(Estudiante,self).presentar_informacion(),self.getCodigo(), self.pais.getNombre_pais(), self.pais.getCapital())
		return c
		

#clase hija que funciona para los estudiantes presenciales esta hereda atributos de persona y estudiante
class Est_Presencial(Estudiante):
	def __init__(self):
		super(Est_Presencial, self).__init__()
		self.num_creditos = 0
		self.ciclo = 0

	# se crea los metodos para agregar los creditos y el ciclo
	def setNum_creditos(self,nc):
		self.num_creditos = nc

	def setCiclo(self,c):
		self.ciclo = c

	#se crea los metodos para retornar los valores de los creditos y el ciclo	
	def getNum_creditos(self):
		return self.num_creditos

	def getCiclo(self):
		return self.ciclo

	#se crea el metodo para enviar la informacion esta contiene la informacion de las dos clases persona y estudiante	
	def presentar_informacion(self):
		c = "%s\n\tNumero de creditos:%s\n\tCiclo: %s" % (super(Est_Presencial,self).presentar_informacion(),self.getNum_creditos(), self.getCiclo())
		return c


#clase hija que funciona para los estudiantes a distancia esta hereda atributos de persona y estudiante
class Est_Distancia(Estudiante):
	def __init__(self):
		super(Est_Distancia, self).__init__()
		self.num_materias = 0
		self.modulo = ""

	#se crea los metodos para agregar la materia y el modulo	
	def setNum_materias(self,m):
		self.num_materias = m

	def setModulo(self,M):
		self.modulo = M

	#se crea los metodoas para retornar los valores de materia y modulo 	
	def getNum_materias(self):
		return self.num_materias

	def getModulo(self):
		return self.modulo

 	#se crea el metodo para enviar la informacion esta contiene la informacion de las dos clases persona y estudiante	
	def presentar_informacion(self):
		c = "%s\n\tNumero de materias:%s\n\tModulo: %s" % (super(Est_Distancia,self).presentar_informacion(),self.getNum_materias(), self.getModulo().upper())
		return c
	
class Pais(object):
	
	def __init__(self):
		self.nombre = ""
		self.capital = ""
	
	def setNombre_pais(self,np):
		self.nombre = np
	
	def setCapital(self,ct):
		self.capital= ct

	def getNombre_pais(self):
		return self.nombre

	def getCapital(self):
		return self.capital