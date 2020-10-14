from caso_D import caso_D
from caso_L import caso_L
from graficar3d import ver_reticulado_3d

import matplotlib.pyplot as plt

ret_D = caso_D()
ret_L = caso_L()

peso = ret_D.calcular_peso_total()

print(f"peso = {peso}")

ver_reticulado_3d(ret_D, 
	axis_Equal=True, 
	opciones_barras={
	"ver_numeros_de_barras": False
	}, 
    llamar_show=True,
    zoom=180.,
    deshabilitar_ejes=True)


ret_D.ensamblar_sistema()
ret_D.resolver_sistema()
f_D = ret_D.recuperar_fuerzas()

#Carga Viva
ret_L.ensamblar_sistema()
ret_L.resolver_sistema()
f_L = ret_L.recuperar_fuerzas()


#Combinaciones de arga
f_1 = 1.4*f_D           #Combinacion 1
f_2 = 1.2*f_D + 1.6*f_L #Combinacion 2

#Calcular factores 

FU_caso1 = ret_D.recuperar_factores_de_utilizacion(f_1)
FU_caso2 = ret_D.recuperar_factores_de_utilizacion(f_2)



ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("Tensiones en caso 1: 1.4 D ")
plt.savefig("1.png")
plt.show()



ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)


plt.title("Tensiones en caso 1: 1.2 D + 1.6 L")
plt.savefig("2.png")
plt.show()




ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU caso 1: 1.4 D ")
plt.savefig("3.png")
plt.show()



ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU caso 2: 1.2 D + 1.6 L")
plt.savefig("4.png")
plt.show()

#Fu = #definir

barras_a_rediseñar = [0,1,2,23,26]
barrasD = ret_D.obtener_barras()
barrasL = ret_L.obtener_barras()
for i in barras_a_rediseñar:
    barrasD[i].rediseñar(1.2*f_D[i]+1.6*f_L[i],ret_D)
    barrasL[i].rediseñar(1.2*f_D[i]+1.6*f_L[i],ret_D)
ret_D.ensamblar_sistema()
ret_D.resolver_sistema()
FU_caso1_rediseñado = ret_D.recuperar_factores_de_utilizacion(1.2*f_D+1.6*f_L)
f_D = ret_D.recuperar_fuerzas()


ret_L.ensamblar_sistema()
ret_L.resolver_sistema()
FU_caso2_rediseñado = ret_D.recuperar_factores_de_utilizacion(1.2*f_D+1.6*f_L)
f_L = ret_L.recuperar_fuerzas()



ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
        "datos_desplazamientos_nodales": 1.6*ret_L.u+1.2*ret_D.u,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_D*1.2 + f_L*1.6,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("Tensiones en caso D rediseñado: 1.2 D + 1.6 L")
plt.savefig("Tension1.png")
plt.show()



ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
        "datos_desplazamientos_nodales": 1.6*ret_L.u+1.2*ret_D.u,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso1_rediseñado,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU caso D rediseñado: 1.2 D + 1.6L")
plt.savefig("Fu1.png")
plt.show()
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
        "datos_desplazamientos_nodales": 1.4*ret_D.u,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_D*1.4,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("Tensiones en caso D rediseñado: 1.4 D ")
plt.savefig("Tension2.png")
plt.show()



ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
        "datos_desplazamientos_nodales": 1.4*ret_D.u,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso2_rediseñado,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU caso D rediseñado: 1.4 D ")
plt.savefig("Fu2.png")
plt.show()

desplazamiento = min(1.2*ret_D.u + 1.6*ret_L.u)
print(f"El desplazamiento maximo es {desplazamiento} m")
