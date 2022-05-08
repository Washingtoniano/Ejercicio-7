from Viajero import ViajeroFrecuente
import csv
class lista():
	__indice=[]
	def __init__ (self):
		self.__indice=[]
	def agregar(self):
		archivo=open("Prueba.csv","r")
		reader=csv.reader(archivo,delimiter=';')
		bandera=False
		for fila in reader:
			if bandera==False:
				bandera=True
			else:
				unviajero=ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4])
				self.__indice.append(unviajero)
		archivo.close()
		return self.__indice
	def mostrar(self):
		for viajero in self.__indice:
			print (viajero)
	def opcion1(self):
		band=False
		master =int(input ("Ingrese la cantidad de millas que desea comparar\n"))
		for viajero in self.__indice:
			if (viajero.Millas()==master):
				band=True
				print (viajero)
		if band==False:
			print ("Ningun viajero posee {} millas".format(master))
	def opcion2 (self):
		num=int (input("Ingrese el numero del viajero con el que desea acumular millas"))
		band=False
		for viajero in self.__indice:
			if (viajero.numero()==num):
				band=True
				millas =float(input ("Ingrese la cantidad de millas a acumular\n"))
				viajero=viajero+millas
				print (viajero)
		if band==False:
			print ("Error")
	def opcion3(self):
		num=int (input("Ingrese el numero del viajero con el que desea canjear millas"))
		band=False
		for viajero in self.__indice:
			if (viajero.numero()==num):
				band=True
				millas =float(input ("Ingrese la cantidad de millas a canjear\n"))
				viajero=viajero-millas
				print (viajero)
		if band==False:
			print ("Error")
