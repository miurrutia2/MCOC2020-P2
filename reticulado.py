import numpy as np

class Reticulado(object):
	"""Define un reticulado"""

	__NNodosInit__ = 100

	def __init__(self):
		super(Reticulado, self).__init__()
		
		self.xyz = np.zeros((Reticulado.__NNodosInit__, 3), dtype=np.double)
		self.Nnodos = 0
		self.barras = []
		self.cargas = {}
		self.restricciones = {}

	def agregar_nodo(self, x, y, z=0):
		if self.Nnodos+1 > Reticulado.__NNodosInit__:
			self.xyz.resize((self.Nnodos+1, 3))
		self.xyz[self.Nnodos, :] = [x, x, z]
		self.Nnodos += 1
		
	def agregar_barra(self, barra):
		self.barras.append(barra)

	def obtener_coordenada_nodal(self, n): 
		if n >= self.Nnodos:
			return
		return self.xyz[n, :]

	def calcular_peso_total(self):
		peso = 0.
		for b in self.barras:
			peso += b.calcular_peso(self)
		return peso

	def obtener_nodos(self):
		return self.xyz[0:self.Nnodos, :].copy()

	def obtener_barras(self):
		return self.barras

	def agregar_restriccion(self, nodo, gdl, valor=0.0):
		if nodo not in self.restricciones:
			slef.restricciones[nodo] = [[gdl, valor]]
		else:
			self.restricciones[nodo].append([gdl, valor])

	def agregar_fuerza(self, nodo, gdl, valor):
		if nodo not in self.cargas:
			slef.cargas[nodo] = [[gdl, valor]]
		else:
			self.cargas[nodo].append([gdl, valor])

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
		s = "nodos:\n"
		for n in range(self.Nnodos):
			s += f" {n} : ( {self.xyz[n, 0]}, {self.xyz[n, 1]}, {self.xyz[n, 2]}"
		s += "\n\n"
		s += "barras:\n"
		for i, b in enumerate(self.barras):
			n = b.obtener_conectividad()
			s += f" {i} : [ {n[0]} {n[1]} ] \n"
		s += "restricciones:\n"
		for nodo in self.restricciones:
			s += f"{nodo} : {self.restricciones[nodo]}\n"
		s += "cargas:\n"
		for nodo in self.cargas:
			s += f"{nodo} : {self.cargas[ndo]}\n"

		return s


