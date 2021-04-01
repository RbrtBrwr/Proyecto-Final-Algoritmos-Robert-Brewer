from inventario import Inventory



class Player:
    def __init__(self, nombre, edad, contrasena, avatar, tiempo, vida, pistas, inventario, nuevo=False):
        self.nombre = nombre
        self.__edad = edad
        self.__contrasena = contrasena
        self.avatar = avatar
        self.tiempo = tiempo
        self.vida = vida
        self.pistas = pistas
        self.inventario = Inventory(inventario)
        self.nuevo = nuevo
        self.vida_inicial = vida

    def get_age_password(self):
        # metodo para mostrar edad y contrasena
        age = self.__edad
        password = self.__contrasena
        return age, password

    def check_inventory(self, item):
        # Chequea si el usuario tiene el item en su inventario
        if item == 'false':
            return True
        else:
            return self.inventario.check_inventory(item)

    def add_inventory(self, item):
        # Agrega item al inventario
        if item == 'vida extra':
            if self.vida == self.vida_inicial:
                pass
            elif (self.vida + 1) > self.vida_inicial:
                self.vida = self.vida_inicial
            else:
                self.vida += 1
        else:
            self.inventario.agregar(item)
                

    def ver_inventario(self):
        # Muestra inventario
        self.inventario.show_inventory()
