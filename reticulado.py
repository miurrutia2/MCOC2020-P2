import numpy as np

class Reticulado(object):
	"""Define un reticulado"""

	def __init__(self):
		super(Reticulado, self).__init__()
		
		self.xyz = np.zeros((0,3), dtype=np.double)
		self.Nnodos = 0
		self.barras = []
		self.cargas = {}
		self.restricciones = {}

	def agregar_nodo(self, x, y, z=0):
		#Cambiar Tamaño
		self.xyz.resize((self.Nnodos+1,3))
		self.xyz[self.Nnodos,:] = [x,y,z]
		self.Nnodos +=1
		return
		
	def agregar_barra(self, barra):
		"""Implementar"""
		return

	def obtener_coordenada_nodal(self, n): 
		"""Implementar"""
		return 

	def calcular_peso_total(self):
		"""Implementar"""
		return 

	def obtener_nodos(self):
		"""Implementar"""

		return self.xyz

	def obtener_barras(self):
		"""Implementar"""
		return self.barras

	def agregar_restriccion(self, nodo, gdl, valor=0.0):
		"""Implementar"""
		return

	def agregar_fuerza(self, nodo, gdl, valor):
		"""Implementar"""
		return

	def ensamblar_sistema(self):
		"""Implementar"""
		return

	def resolver_sistema(self):
		"""Implementar"""
		return

	def recuperar_fuerzas(self):
		"""Implementar"""
		return

	def __str__(self):
		#datos nodos
		s = "nodos:\n"
		for i in range(self.Nnodos):
			s += f" {i} : ({self.xyz[i,0]}, {self.xyz[i,1]}, {self.xyz[i,2]})\n "
		s += "\n" * 2
		#datos barras
		s += "barras:\n"

		for i in range(len(self.barras)):
			
			s += f"{i} : [ {self.barras[i].ni} {self.barras[i].nj} ]\n "
		s += "\n"
		s += f"peso_total = {self.calcular_peso_total()}"
		return s
