from graphviz import Digraph
class Nodo():
	#Nodo de una Matriz dispersa
	def __init__(self,data):
		self.dato = data
		self.x = 0
		self.y = 0
		self.z = 0
		self.derecha = None
		self.izquierda = None
		self.arriba = None
		self.abajo = None
		self.frente = None
		self.atras = None
#-------------------------------MATRIS DISPERSA ----------------------------------
class Matriz():
	"""docstring for matriz"""
	def __init__(self):
		self.cabeza = Nodo(None)
		
	#------------------------Busquedas en cabezeras
	def BuscarX(self,x):
		nodotemp = self.cabeza
		while nodotemp != None:
			if nodotemp.x == x:
				return nodotemp
			nodotemp = nodotemp.derecha
	
	def BuscarY(self,y):
		nodotemp = self.cabeza
		while nodotemp != None:
			if nodotemp.y == y:
				return nodotemp
			nodotemp = nodotemp.abajo			
	#METODO Insertar-------------------------------------------------------------------
	def Insertar(self,x,y,z,data):
		nuevo = Nodo(data)
		if self.Buscar(x,y,z) == None:
			nuevo.x = x
			nuevo.y = y
			cabezeraX = self.BuscarX(x)
			cabezeraY = self.BuscarY(y)
			# Si no existen las cabezeras se crean 

			if cabezeraX == None:  # Cabezera en x 
				
				buscador = self.cabeza
				cabezeraX = Nodo(x)
				cabezeraX.x = x
				cabezeraX.y = 0
				while int(buscador.x)  < int(x) and buscador.derecha != None :
					if buscador.derecha.x < x:
						buscador = buscador.derecha
					else:
						break	
				
				if buscador.derecha != None:   #Si la cabezara va en medio 				
					buscador.derecha.izquierda = cabezeraX
					cabezeraX.derecha = buscador.derecha

				buscador.derecha = cabezeraX
				cabezeraX.izquierda = buscador
			
			if cabezeraY == None: # Cabezera en y 
				buscador = self.cabeza
				cabezeraY = Nodo(y)
				cabezeraY.y = y
				cabezeraY.x = 0
				while buscador.y < y and buscador.abajo != None :
					if buscador.abajo.y < y: 
						buscador = buscador.abajo
					else:
						break	
				if buscador.abajo != None:		
					buscador.abajo.arriba = cabezeraY
					cabezeraY.abajo = buscador.abajo
				buscador.abajo = cabezeraY
				cabezeraY.arriba = buscador	
			# Casos de Insercion
			#Busqueda de nodoanterior
			while cabezeraX.y < y and cabezeraX.abajo != None:
					if cabezeraX.abajo.y < y: 
						cabezeraX = cabezeraX.abajo
					else:
						break	
			while cabezeraY.x < x and cabezeraY.derecha != None:
					if cabezeraY.derecha.x < x:
						cabezeraY = cabezeraY.derecha
					else:
						break	
			#Caso insercion en medio
			if cabezeraX.abajo != None:
				cabezeraX.abajo.arriba = nuevo
				nuevo.abajo = cabezeraX.abajo
			if cabezeraY.derecha != None:
				cabezeraY.derecha.izquierda = nuevo 
				nuevo.derecha = cabezeraY.derecha
			cabezeraX.abajo = nuevo
			nuevo.arriba = cabezeraX
			cabezeraY.derecha = nuevo
			nuevo.izquierda = cabezeraY
	# Imprimir En planp -------------------------------------------------------
	def Imprimir(self):
		aux = self.cabeza
		while aux != None:
			auxt = aux
			while auxt != None:		 
				print("Estoy en el nodo y : " + str(auxt.y) + " x: " + str(auxt.x) + "Con :" + str(auxt.dato))
				auxt = auxt.derecha
			aux = aux.abajo
	def Buscar(self,x,y,z):
		aux = self.cabeza
		while aux != None:
			auxt = aux
			while auxt != None:
				if ( auxt.x == x and auxt.y == y):
					return auxt
				auxt = auxt.derecha
			aux = aux.abajo 
	def Graficar(self):
		dot = Digraph()		
		aux = self.cabeza
		
		while aux != None:
			auxt = aux
			rank = "{ rank = same; "	
			while auxt != None:
				#dot.attr("graph",style='filled')
				dot.node(str(self.GetNombre(auxt)),str(auxt.dato))
				if auxt.derecha != None:
					dot.edge(str(self.GetNombre(auxt)),str(self.GetNombre(auxt.derecha)))
				if auxt.izquierda != None:
					dot.edge(str(self.GetNombre(auxt)),str(self.GetNombre(auxt.izquierda)))
				if auxt.arriba != None:
					dot.edge(str(self.GetNombre(auxt)),str(self.GetNombre(auxt.arriba)))
				if auxt.abajo != None:
					dot.edge(str(self.GetNombre(auxt)),str(self.GetNombre(auxt.abajo)))			
				rank = rank + " "+str(self.GetNombre(auxt))
				auxt = auxt.derecha
			rank = rank + "}"
			dot.body.append(rank)
			aux = aux.abajo 
		dot.format = 'png' 
		dot.render('lista')	
		print ( dot.source)			
	def GetNombre(sef,nodo):
		nombre = str("X"+str(nodo.x)+"Y"+str(nodo.y)+"Z"+str(nodo.z))
		return nombre	
MatrizPruebas = Matriz()
MatrizPruebas.Insertar(3,6,0,"holitas")
MatrizPruebas.Insertar(1,1,0,"holitas")
MatrizPruebas.Insertar(5,1,0,"holitas")
MatrizPruebas.Insertar(2,1,0,"repetidosssakjdhsakjdaksj")	
MatrizPruebas.Insertar(2,3,0,"holitas")
MatrizPruebas.Insertar(2,1,0,"adios")	
MatrizPruebas.Graficar()
		