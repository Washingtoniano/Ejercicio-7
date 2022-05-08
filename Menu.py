from Lista import lista
class menu():
    __lista=lista()
    def __init__(self):
        self.__lista=lista()
    def inicializar (self):
        self.__lista.agregar()
    def manejador (self,op):
        if (op==1):
            self.opcion1()
        elif (op==2):
            self.opcion2()
        elif (op==3):
            self.opcion3()
        elif (op==4):
            self.opcion4()
        else:
            print ("Error")
    def opcion1(self):
        self.__lista.opcion1()
    def opcion2(self):
        self.opcion4()
        self.__lista.opcion2()
    def opcion3(self):
        self.opcion4()
        self.__lista.opcion3()
    def opcion4(self):
        self.__lista.mostrar()
