import os
def limpieza():
    input("...")
    os.system("clear")
    os.system("cls" if os.name == "nt" else "clear")


opt = 0
productos = [{
            "code": "001",
            "name": "Llantas",
            "price": "150000"
            },
            {
            "code": "002",
            "name": "repuestos",
            "price": "120000."
            },
            {
            "code": "003",
            "name": "aceite",
            "price": "60000"
            }
            ]

def productosIndex(code):
    ind = -1
    for i in range(len(productos)):
        if productos[i]["code"] == code:
            ind = i
            break
    return ind

print(productos)
while(True):
    print("1. Agregar producto\n2. Modificar producto\n3. Vaciar diccionario")
    opt = int(input("\n¿Que desea hacer? ->") or 0)
    match(opt):
        case 1:
            productos.append({
                "code": input("codigo del producto ->"),
                "name": input("Nombre del producto ->"),
                "price": input("precio del producto ->")
            })
            print("Producto agregado....") 
        case 2: 
            code = input("Codigo de producto a modifica: ->")
            prodind = productosIndex(code)
            if prodind == -1:
                print(f"El codigo {code} no ha sido encontrado")
            else:
                print(f"Código: {productos[prodind].get('code')}")
                print(f"Nombre: {productos[prodind].get('name')}")
                print(f"Precio: {productos[prodind].get('price')}")
                print(f"Activo: {productos[prodind].get('active')}")
        case 3:
            producto = {
                "code": "001",
                "name": "Llantas",
                "price": "150000"
            }
            # producto.clear()
            # items = producto.items() 
            #print(items)
            #for itm in items:
            #    print(itm)
            print(producto.keys())
            print(producto.values())
            keys = producto.keys()
            for k in keys:
                print(f"{k} {producto[k]}")
    limpieza()

    print(productos)
    if opt == 0: 
        print("bye bye")
        break