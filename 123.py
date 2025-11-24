#    lista1 = [[1, 0], [5, 10], [[50, 100], 30]]


 #   for item in lista1:
  #      for subitem in item:
        
#lista1[2][0][1] = "Modificado"
#print(lista1)

tupla = (1, 2, 3)
print(tupla)

tupla2 = "a", "b", "c"
print(tupla2)

tupla3 = 1, 2, ('a', 'b'), 3
print(tupla3)

print(tupla2[2])
print(tupla3[2][0])

#Convertir lista a tupla 
lista = [1, "a", 2, "b", 3]
tupla4 = tuple(lista)
print(tupla4, type(tupla4))
#- inversa
list1 = list(tupla4)
print(list1, type(list1))

# Recorer tupla
for valor in tupla3:
    print(valor)
for i in range(len(tupla3)):
    print(tupla3[i])

# asignar el valor de la tupla
x, y, z = tupla
print(f"x={x}, y={y}, z={z}")

# Contar cuantas veces aparece
tupla5 = 1, 2, 3, 4, 5, 5, 6, 6, 1, 5, 9
print(tupla5.count(5))

list1 = [1, 2]
x, y = list1
print(x, y)

print(tupla5.index(9))
print(tupla5.index(5, 3))