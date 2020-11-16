#   Serialización

import pickle
class Guitarra():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo

    def print(self):
        print(self.marca,self.modelo)

    def __str__(self):
        return "{}-{}".format(self.marca,self.modelo)


class ListaGuitarras:

    guitarras=[]

    def __init__(self):
        try:
            listaDeGuitarras=open("fichero_guitarras","ab+") #para añadir
            listaDeGuitarras.seek(0) #nos despalzamos a la posición 0

            self.guitarras=pickle.load(listaDeGuitarras)
            print("Cargadas {} guitarras".format(len(self.guitarras)))
        except:
            print("Fichero vacío")
        finally:
            listaDeGuitarras.close()
            del(listaDeGuitarras)

    def guardarGuitarrasFichero(self):
        listaDeGuitarras = open("fichero_guitarras", "wb")
        pickle.dump(self.guitarras,listaDeGuitarras)
        listaDeGuitarras.close()
        del (listaDeGuitarras)


    def anadirGuitarra(self,p):
        self.guitarras.append(p)
        self.guardarGuitarrasFichero()

    def mostrarGuitarras(self):
        for item in self.guitarras:
            print(item)

def creaFicheroLista():
    lista=["Murcia","Alicante"]
    fichero_lista_binario=open("fichero_ciudades","wb")
    pickle.dump(lista,fichero_lista_binario)
    fichero_lista_binario.close()
    del(fichero_lista_binario)

def leeFicheroLista():
    fichero_lista_binario = open("fichero_ciudades", "rb")
    lista=pickle.load(fichero_lista_binario)
    fichero_lista_binario.close()
    del (fichero_lista_binario)
    print(lista)


def creaFicheroGuitarra():
    guitarra=Guitarra("Fender","telecaster")
    guitarra1=Guitarra("Fender","Stratocaster")
    lista=[guitarra,guitarra1]
    ficheroBinario=open("fichero_guitarras","wb")
    pickle.dump(lista,ficheroBinario)
    ficheroBinario.close()
    del(ficheroBinario)

def leeFicheroGuitarra():
    ficheroBinario = open("fichero_guitarras", "rb")
    lista=pickle.load(ficheroBinario)
    ficheroBinario.close()
    del (ficheroBinario)
    for itemguitarra in lista:
        #itemguitarra.print()
        print(itemguitarra)




#creaFicheroLista()
#leeFicheroLista()

#creaFicheroGuitarra()
#leeFicheroGuitarra()

listaGuitarras=ListaGuitarras()
guitarra = Guitarra("Fender", "telecaster 1966")
listaGuitarras.anadirGuitarra(guitarra)
guitarra = Guitarra("Fender", "Stratocaster 1958")
listaGuitarras.anadirGuitarra(guitarra)

listaGuitarras.mostrarGuitarras()
