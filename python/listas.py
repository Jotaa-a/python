import os
def limpieza():
    input("...")
    os.system("clear")
    os.system("cls" if os.name == "nt" else "clear")
opt = 0
productos = ["Papa", "Arroz", "yuca", "Papa", "Cebolla"]
print(productos)
while(True):
    print("1. Agregar producto\n2. Editar posición\n3. Número de productos registrados\n4. Insetar en posición\n5. Insertar elementos en lista\n6. Eliminar productos\n7. Pop a un producto\n8. Conteo producto\n9. Ordenar productos\n10. Invertir lista\n11. Vaciar lista")
    opt = int(input("\n¿Que desea hacer? ->") or 0)
    match(opt):
        case 1:
            productos.append(input("Nombre del producto: "))
            print("Producto agregado....")   
        case 2:
            posc = int(input("Posición del producto"))
            print(f"Producto a editar: {productos[posc]}")
            productos[posc] = input("Nuevo producto: ")
            print("Producto editado....")
        case 3: 
            print(f"Productos registrados: {len(productos)}")
            input("...")
        case 4: 
            posc = int(input("¿En que posición agregar? "))
            prod = input("Nombre del producto: ")
            productos.insert(posc, prod)
            print("Producto agregado")
        case 5:
             otrosProd = ["Detergente", True, 5000, ["Campus", "Camper"]]
             productos.extend(otrosProd)
             print("Lista extendida")
        case 6:
            prod = input("Elemento a elimiar: ")
            productos.remove(prod)
            print("producto eliminado")
        case 7:
            posc = int(input("Posicion del producto a eliminar: "))
            print(f"Elemento eliminado: {productos.pop(posc)}")
        case 8:
            prod = input("Nombre de producto: ")
            print(f"El producto {prod} se repite {productos.count(prod)}")
        case 9:
            productos.sort()
            print("Productos ordenados...")
        case 10:
            productos.reverse()
            print("Lista invertida")
        case 11:
            productos.clear()
            print("Lista vacia...")
    
    
    
    
    
    
    
    limpieza()

    print(productos)
    if opt == 0: 
        print("bye bye")
        break