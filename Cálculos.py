# CALCULO MODULO DE REACCIÓN DEL SUELO EN LOSAS
print('\nMODULO DE REACCIÓN VERTICAL DEL SUELO')
print('\nDatos iniciales')
from Clases import *
geom = Geometria()
suelo = Suelo()
vesic = Vesic()
braja = Braja()


# DATOS INICIALES

suelo.u = 0.30                            
suelo.Es = 30000                           # Modulo de elasticidad del suelo _ [kN/m²]
geom.B = 3.2                             # Lado corto de la losa _ [m]
geom.L = 5.7                            # Lado largo de la losa _ [m]
braja.K30 = 300000                           # Coeficiente de balasto orientado _ [kN/m³] 
suelo.Tipo = 0                            # Tipo de suelo, 0: Suelo cohesivo  1: Suelo granular         
                                
print("u = %.2f" %suelo.u)
print("Es = %.2f _ [kNm²]" %suelo.Es)
print("B = %.2f _ [m]"%geom.B)
print("L = %.2f _ [m]" %geom.L)
print("K30 = %.0f _ [kN/m³]" %braja.K30)  


# SOLUCIÓN
print('\nMetodo de Vesic, A.B 1961 y Klepikov')
geom.A = geom.Area(geom.B, geom.L)                                 # Área de de la losa _ [m] 
#geom.r = geom.Relacion(geom.B, geom.L)                             # Realción L/B
geom.w = geom.Coeficiente(geom.B, geom.L)                          # Coeficiente "w"
                
if (geom.L == geom.B):
    vesic.Kz = vesic.LosaCuadrada(suelo.Es, geom.B, suelo.u)            # Coeficiente de reaccion vertical losas cuadradas _ [kN/m³]                 
else:
    vesic.Kz = vesic.LosaRectang(suelo.Es, geom.w, geom.A, suelo.u)     # Coeficiente de reaccion vertical losas rectangulares _ [kN/m³]

vesic.Kxy = 0.75*vesic.Kz                                               # Coeficiente de reaccion horizontal _ [kN/m³]
print("A = %.2f _ [m²]" %geom.A) 
#print("L/B = %.2f " %geom.r) 
print("w = %.2f " %geom.w) 
print("Kz = %.1f _ [kN/m³]" %vesic.Kz)
print("Kxy = %.1f _ [kN/m³]" %vesic.Kxy)

print('\nMetodo Braja M. Das')

if (suelo.Tipo == 0):
    suelo.Tipo = "Cohesivo"
    braja.Kz = braja.SueloCohesivo(braja.K30, geom.B, geom.L)       # Coeficiente de reaccion vertical suelos cohesivo _ [kN/m³]
    print(suelo.Tipo)
else:
    suelo.Tipo = "Granular"
    braja.Kz = braja.SueloGranular(braja.K30, geom.B, geom.L)       # Coeficiente de reaccion vertical suelos granulares _ [kN/m³]
    print(suelo.Tipo)
                   
braja.Kxy= 0.75*braja.Kz                                            # Coeficiente de reaccion horizontal _ [kN/m³]
print("Kz = %.1f _ [kN/m³]" %braja.Kz)
print("Kxy = %.1f _ [kN/m³] \n" %braja.Kxy)

    