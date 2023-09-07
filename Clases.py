class Geometria ():
    def __init__(self):
        self.B = 1                  # Lado corto de la losa _ [m]
        self.L = 1                  # Lado largo de la losa _ [m]
        self.A = 1                  # Área de de la losa _ [m] 
        self.w = 1                  # Coeficiente "w"
    
    def Area (self, B, L):
        Area = B * L
        return Area
        
    def Coeficiente (self, B, L):
        w = 100/((4.03*(L/B)) + 109.05)
        return w
    
    
class Suelo ():
    def __init__(self):
        self.u = 0.30               # Coeficiente de Poisson
        self.Es = 4500              # Modulo de elasticidad del suelo _ [kN/m²]
        self.Tipo = 1               # Tipo de suelo, 0: Suelo cohesivo  1: Suelo granular


class Vesic ():
    def __init__(self):
        self.Kz = 1                 # Coeficiente de reaccion vertical  _ [kN/m³]
        self.Kxy = 1                # Coeficiente de reaccion horizontal _ [kN/m³]

    def LosaCuadrada(self, Es, B, u):
        Kz = Es/(B*(1-u**2)) 
        return Kz

    def LosaRectang(self, Es, w, A, u):
        Kz = Es/(w*A**0.5*(1-u**2)) 
        return Kz
    

class Braja ():
    def __init__(self):
        self.K30 = 1                    # Coeficiente de balasto orientado _ [kN/m³] 
        self.Kz = 1                     # Coeficiente de reaccion vertical  _ [kN/m³]
        self.Kxy = 1                    # Coeficiente de reaccion horizontal _ [kN/m³]

    def SueloCohesivo (self, K30, B, L):
        KzB = (K30*1000)*(0.30/B)
        Kz = (KzB*(1+(B/(2*L))))/1.5
        return Kz 
        
    def SueloGranular (self, K30, B, L):
        KzB = (K30*1000)*((B + 0.30)/(2*B))**2
        Kz = (KzB*(1+(B/(2*L))))/1.5
        return Kz 



