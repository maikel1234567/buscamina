matriz= [[0,0,1,0],
         [0,0,0,1],
         [0,1,0,0],
         ]

elusuario= [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            ]

def mostrar_tablero(tablero):
    for f in enumerate(tablero):
        print(f)
        
while True:
    print("bienvenido a mi jugo:")
    print("este es el tablero")
    mostrar_tablero(elusuario)

    fila= int(input("ingrese na fila:"))
    columna=int(input("ingrese una columna:"))

    if matriz[fila][columna]==1:
        
        elusuario[fila][columna]="x"
        mostrar_tablero(elusuario)
        print("aleluya!!!!!")
        
    else:
        print("no hay nada , recorcholi :(")
        mostrar_tablero(elusuario)
        print("no hay bomba!!!")
