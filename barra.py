import numpy as np


g = 9.81 #kg*m/s^2


class Barra(object):

	"""Constructor para una barra"""
	def __init__(self, ni, nj, R, t, E, ρ, σy):
		super(Barra, self).__init__()
		self.ni = ni
		self.nj = nj
		self.R = R
		self.t = t
		self.E = E
		self.ρ = ρ
		self.σy = σy

	def obtener_conectividad(self):
		"""Implementar"""
		return [self.ni, self.nj]

	def calcular_area(self):
		"""Implementar""" 
		return (np.pi*self.R**2) - (np.pi*(self.R - self.t)**2)

	def calcular_largo(self, reticulado):
		"""Devuelve el largo de la barra. 
		xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
		xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
		"""
		"""Implementar""" 
		xi = reticulado.obtener_coordenada_nodal(self.ni)
		xj = reticulado.obtener_coordenada_nodal(self.nj)
		dij = xi - xj
		return np.sqrt(np.dot(dij, dij))


	def calcular_peso(self, reticulado):
		"""Devuelve el largo de la barra. 
		xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
		xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
		"""
		"""Implementar"""
		L = self.calcular_largo(reticulado)
		A = self.calcular_area()
		return A * L * g * self.ρ


	def obtener_rigidez(self, ret):
		"""Devuelve la rigidez ke del elemento. Arreglo numpy de (4x4)
		ret: instancia de objeto tipo reticulado
		"""
		
		#implementar
		L = self.calcular_largo(ret)
		A = self.calcular_area()
		k = self.E * A /L
		
		nix = ret.xyz[self.ni, 0]
		niy = ret.xyz[self.ni, 1]

		njx = ret.xyz[self.nj, 0]
		njy = ret.xyz[self.nj, 1]

		cos = (njx - nix) / L
		sen = (njy - niy) / L

		Ttheta = np.array([-cos, -sen, cos, sen])
		ke = k * Ttheta.T @ Ttheta 

		return ke

	def obtener_vector_de_cargas(self, ret):
		"""Devuelve el vector de cargas nodales fe del elemento. Vector numpy de (4x1)
		ret: instancia de objeto tipo reticulado
		"""
		
		#Implementar

		W = self.calcular_peso(ret)
		fe = np.array([0,-1,0,-1]).T*W/2

		return fe


	def obtener_fuerza(self, ret):
		"""Devuelve la fuerza se que debe resistir la barra. Un escalar tipo double. 
		ret: instancia de objeto tipo reticulado
		"""

		#Implementar
		L = self.calcular_largo(ret)
		A = self.calcular_area()

		nix = ret.xyz[self.ni, 0]
		niy = ret.xyz[self.ni, 1]

		njx = ret.xyz[self.nj, 0]
		njy = ret.xyz[self.nj, 1]

		cos = (njx - nix) / L
		sen = (njy - niy) / L

		Ttheta = np.array([-cos, -sen, cos, sen])

		ue = np.array([ret.u[self.ni*2], ret.u[((2*self.ni)+1)], ret.u[2*self.nj], ret.u[((2*self.nj)+1)]])

		se = (self.E * A / L) * Ttheta.T @ ue


		return se








