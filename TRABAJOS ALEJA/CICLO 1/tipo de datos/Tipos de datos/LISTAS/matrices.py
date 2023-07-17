def crearMat(fils, cols):
    mat = []
    for f in range (fils):
        filas = []
        for c in range(cols):
            fila.append(0)
        mat.append(fila)
    return mat

def printMat(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            print(m[f][c], end="-\t")
        print("")

fils = 3
cols = 4
m = crearMat(fils, cols)
print(m)
m[2][1] = 5 #2 ES FILA Y 1 ES COLUMNA
print(m)

"""def crearMat(fils, cols):
    mat = [[0] * cols]* fils #LISTA CON UN ELEMENTO QUE ES 0 por las columnas y filas
    return mat


fils = 3
cols = 4
m = crearMat(fils, cols)
print(m)
m[2][1] = 5 #2 ES FILA Y 1 ES COLUMNA
print(m)"""