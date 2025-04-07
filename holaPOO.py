class Saludo:
    def __init__(self,mensaje):
        self.mensaje = mensaje
    
    def Mostar_mensaje(self):
        print(self.mensaje)
        
saludo = Saludo("hola mundo")
saludo.Mostar_mensaje()