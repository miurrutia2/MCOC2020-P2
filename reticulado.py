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
		s = "Hola soy un reticulado!\n"
		s += "mis nodos son"
		s += f"{self.xyz}"
		return s

