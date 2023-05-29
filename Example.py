#crear lista
lista = [1, 5, 25, 100, 500]
print ("inicial:" ,lista)

#append=permite agregar un dato a la lista
lista.append (250)
print("append: ", lista)

#extend=toma una segunda lista y la agrega a sus datos
lista2 = [75, 125]
lista.extend(lista2)
print("extend: ",lista)

#insert=agregamos dato en la pocision
lista.insert(2,400)
print("insert: ",lista)

#remove=busca y elimina el dato entregado
lista.remove(400)
print("remove: ",lista)

#pop()=elimina el ultimo registro
#pop(posicion)=elimina la posicion entregada
lista.pop()
print("pop:  ",lista)
lista.pop(2)
print("pop(2):  ",lista)

#reverse=invierte el orden de la lista
lista.reverse()
print("revrse: ",lista)

#sort=ordenar de menor a mayor
lista.sort()
print("sort: ",lista)

#sort(reverse=true)=ordena de mayor a menor
lista.sort(reverse=True)
print("sort(r): ",lista)
