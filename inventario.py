from random import randrange


class Inventory:

    # El inventario siempre se inicializa vacio
    def __init__(self, rewards):

        # Contrasena para computadora 2
        self.contrasena = str(randrange(1000, 10000))
        self.items = {}
        for i in rewards:
            if i == 'contraseña':
                i = 'contraseña: ' + self.contrasena
                self.items[i] = False
            else:
                self.items[i] = False

        



    # Si un item es True es porque lo tenemos, de lo contrario no aparecera en consola
    def show_inventory(self):
        """
        Muestra los items que el jugador ha encontrado
        """
        print('Inventario:\n')
        i = 0
        for k in self.items.keys():
            if self.items[k]:
                i = 1
                print(k)
        if i == 0:
            print('Tu inventario esta vacio')

    
    # Se cambia el valor del item para agregarlo a la lista que mostraremos al jugador
    def agregar(self, reward):
        """
        Agrega el objeto al inventario

        Args:
            objeto ([str]): cambia el valor del objeto en el diccionario de False a True
        """

        if reward != False:
            if reward == 'contraseña':
                reward = 'contraseña: ' + self.contrasena
                self.items[reward] = True
            else:    
                self.items[reward] = True



    # Revisar si se tiene el item que se necesita
    # se tiene que meter el nombre bien
    def check_inventory(self, item):
        """
        Revisa el inventario a ver si ya se tiene el item pedido

        Args:
            item (str)

        Returns:
            [bool]: Si el item esta en el inventario, regresa True, else regresa False
        """
        if item == 'Mensaje':
            item = 'Mensaje: Si estas gradudado puedes pisar el Samán'

        if not self.items:
            return False

        elif self.items[item] == True:
            return True
        else:
            return False

 
