
categories = [{
            "code": "C001",
            "name": "Elementos de limpieza",
            "productos":[{
            "code": "002",
            "name": "repuestos",
            "price": "120000."
            },
            {
            "code": "003",
            "name": "aceite",
            "price": "60000"
            }]
            },
            
            ]


def findIndex(datalist, code):
    print(datalist)
    ind = -1
    for i in range(len(datalist)):
        if productos[i]["code"] == code:
            ind = i
            break
    return ind

def findProduct(categoryCode, productCode):
    catgIndex = findIndex(categories, categoryCode)
    if catgIndex == -1:
        print("categoria no existe...")
        return
    else: 
        prodIndex = findIndex(categories[catgIndex]["productos"], productCode)
        if prodIndex == -1:
            print("Producto no existe...")
        else:
            print(categories[catgIndex]["products"][prodIndex]) 

findProduct("c001", "002")
kjsadka