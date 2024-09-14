import sympy as sp

#funcion que devuelve el resultado del sistema de ecuaciones
def def_res():
    #Se definen las variables, donde x = cantera1, y = cantera2, z = cantera3
    x, y, z = sp.symbols('x y z')
    #Se definen las ecuaciones
    eq1 = sp.Eq(0.52*x + 0.20*y + 0.25*z, 4800)
    eq2 = sp.Eq(0.30*x + 0.50*y + 0.20*z, 5810)
    eq3 = sp.Eq(0.18*x + 0.30*y + 0.55*z, 5690)
    #Se obtiene la solucion
    sol = sp.solve((eq1, eq2, eq3), (x,y,z))
    valores = [0,0,0]
    j = 0
    for i in sol.values(): 
        valores[j] = i
        j+=1
    return valores

#funcion que devuelve las matrices generadas por metodo jacobi
def def_jacobi():
    matrizA = [[0.52, 0.2, 0.25], [0.3, 0.5, 0.2], [0.18, 0.3, 0.55]]
    matrizB = [4800, 5810, 5690]
    
    matrizM = [[0,0,0], [0,0,0], [0,0,0]]
    matrizC = [0,0,0]
    i = 0
    for x in matrizA:
        j = 0
        for y in x:
            if(i==j):
                matrizM[i][j]=0
            else:
                matrizM[i][j]=-1*(y/x[i])
            j+=1
        matrizC[i] = matrizB[i]/x[i]
        i+=1
    return matrizM, matrizC

#funcion que devuelve el valor alfa
def def_alfa(matriz):
    may = 0
    for x in matriz:
        s = 0
        for y in x:
            s+=abs(y)
        if(may<s):
            may = s
    return may   

#funcion que determina las iteraciones
def def_iteraciones(matriz1, matriz2, tol):
    #Definir variables
    resultados = [0,0,0]
    x1 = 0; x2 = 0; x3 = 0; i=0
    while True:
        #primero se deben calcular las variables posteriores a los resultados anteriores
        x1 = resultados[1]*matriz1[0][1]+resultados[2]*matriz1[0][2]+matriz2[0]
        x2 = resultados[0]*matriz1[1][0]+resultados[2]*matriz1[1][2]+matriz2[1]
        x3 = resultados[0]*matriz1[2][0]+resultados[1]*matriz1[2][1]+matriz2[2]
        #se resta el valor anterior y el valor generado, si la resta es menor igual a la tolerancia, se empieza a notar una mejor convergencia y 
        #termina el programa
        if(abs(resultados[0]-x1)<=tol): return (resultados, i)
        resultados[0] = x1
        resultados[1] = x2
        resultados[2] = x3
        i+=1
        
#Inicializar las variables con los resultados obtenidos
valores = def_res()
matrizM, matrizC = def_jacobi()
alfa = def_alfa(matrizM)
#Definir tolerancia
tol = 0.01
resultado_jacobi, iteraciones = def_iteraciones(matrizM, matrizC, tol)
print(f"""Valores reales: {valores}
Valores obtenidos con el metodo de jacobi {resultado_jacobi} con {iteraciones} iteracioens con tolerancia de {tol}""")
