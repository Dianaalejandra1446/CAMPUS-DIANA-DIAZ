def buscarElem(lst, elem):
    for i in range(len(lst)):
        if lst[i] == elem:
            return i
        return None

def encontrarElem(lst, elem):
    for e in lst:
        if e == elem:
            return True
        return False
def myFunc(e):
    return e[2] * e[3]

cars = [[8, "carlos",100, 1000],[1, "Diana", 25 ,25000],[6, "Oscar", 80 , 50000]]

cars.sort(reverse=True,key=myFunc)
cars = ["Ford", "Nitasubishi", "BW" , "VW"]
print(cars)