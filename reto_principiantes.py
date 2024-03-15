import math
import time


# 1000 - hola mundo

def holamundo():
    print("Hola mundo")

# 1001 - Extremadamente Básico
def suma():
    
    A = int(input("Ingrese #1 de la suma : \n"))
    B = int(input("Ingrese #2 de la suma : \n"))
    X = A + B
    print(f"X = {X}")

# 1002 - Area del circulo 

def area_del_circulo():
    pi = 3.14159
    radio = float(input("ingresa el valor del radio: \n"))
    area = pi * radio**2
    print(f"A={area:.4f}")

# 1003 - Suma simple
    
def suma_simple():
    A = int(input("Introuzca un digito: \n"))
    B = int(input("Introduzca otro digito: \n"))

    SOMA = A + B
    print(f"SOMA = {SOMA}")
    

# 1004 - Producto Simple
def mulitplicacion():
    A = int(input("Ingresa un digito: \n"))
    B = int(input("Ingresa otro numero: \n"))

    PROD = A * B
    print(f"PROD = {PROD}")

 # 1005 - Promedio 1

def promedio_1():
    A = float(input("Ingresa un valor numerico: \n"))
    B = float(input("Ingresa otro numero: \n"))

    media = ((A * 3.5) + (B * 7.5)) / 11

    print(f"MEDIA = {media:.5f}")
    
# 1006 - Promedio 2
def promedio_2():

    A = float(input("ingresa un numero 1: \n"))
    B = float(input("ingresa un numero 2: \n"))
    C = float(input("ingresa un numero 3: \n"))

    media = ((A / 10 * 2) + (B / 10 * 3) + (C / 10 * 5))
    print(f"MEDIA = {media:.1f}")

# 1007 - Diferencia

def diferencia():
    
    a = int(input("Ingresa un numero 1: \n"))
    b = int(input("Ingresa un numero 2: \n"))
    c = int(input("Ingresa un numero 3: \n"))
    d = int(input("Ingresa un numero 3: \n"))
    diferencia = (a * b) - (c * d)

    print("DIFERENCA =", diferencia)

# 1008 - Salario 

def salario():
    empleado = int(input("ingrese el numero de empleado: \n"))
    horas = int(input("ingreses las horas: \n"))
    horas_valor = float(input("ingrese cuanto le paga por hora: \n"))
    salario = float( horas * horas_valor)

    print(f"NUMBER = {empleado}")
    print(f"SALARY = U$ {salario:.2f}")
    
# 1009 - salario + bonus

def salario_bonus():
    empleado = str("ingresa el nombre del empleado: \n")
    salario_fijo = float(input("Ingresa el salario fijo: \n"))
    ventas = float(input("Ingresa las ventas hechas: \n"))
    salario_final = (salario_fijo + (ventas * 0.15))  #ventas por el 0.15 es el bono sumado al salario
    print(f"EMPLEADO = {empleado}")
    print(f"TOTAL = R$ {salario_final:.2f}")

# 1010 - Calculo simple

def calculo_simple():

    producto_1, producto_2 = map(float, input("Ingresa dos numeros del producto: \n").split()) # para leer los datos asignados
    valor_1, valor_2 = map(float, input("Ingresa dos digitos: \n").split())

    total = (producto_1 * producto_2) + (valor_1 * valor_2) # valor a pagar
    print(f"VALOR A PAGAR: R$ {total:.2f}")

# 1011 - Esfera 
def esfera():
    radio = float(input("Ingresa el radio : \n"))
    valor = 4/3.0
    pi = 3.14159

    formula = valor * pi * radio**3
    print(f"VOLUME = {formula:.3f}")
    
# 1012 - Area
def area():
    valores = input("Ingresa un numero cualquiera: \n").split(" ")

    triangulo = 0.5 * float(valores[0]) * float(valores[2])
    circulo = 3.14159 * (float(valores[2]) **2)
    trapecio = 0.5 * (float(valores[0]) + float(valores[1])) * float(valores[2])
    cuadrado = float(valores[1]) ** 2
    rectangulo = float(valores[0]) * float(valores[1])

    print(f"TRIANGULO: {triangulo:.3f}")
    print(f"CIRCULO: {circulo:.3f}")
    print(f"TRAPEZIO: {trapecio:.3f}")
    print(f"QUADRADO: {cuadrado:.3f}")
    print(f"RETANGULO: {rectangulo:.3f}")

#1013 - El mayor
def el_mayor():
    valor = input("Ingresa tres numeros: \n").split(" ")
    a, b, c = valor

    mayor = (int(a) + int(b) + abs(int(a) - int(b))) / 2
    resultado = (int(mayor) + int(c) + abs(int(mayor) - int(c))) / 2

    print("%d eh o maior" % resultado)
    
# 1014 - Consumo
def consumo():
    distancia = int(input("Ingresa la distancia recorrida: \n"))
    combustible = float(input("Ingresa los litros de combustible: \n"))
    consumo = distancia / combustible
    print("%.3f km/l" % consumo)

# 1015 - distancia entre dos puntos
def distancia():
    x1, y1 = map(float, input("Ingresa dos valores: \n").split())
    x2, y2 = map(float, input("Ingresa dos valores: \n").split())
    distancia = math.sqrt((x2 - x1)**2 + (y2 -y1)**2)
    print(f"{distancia:.4f}")

# 1016 - Distancia
def distancia_2():
    auto = int(input("Ingresa la distancia: \n"))
    distancia = auto * 2
    print("%d minutos" % distancia)
    
#1017 - Combustible gastado
def combustible():
    horas = int(input("Ingresa las horas: \n"))
    velocidad = int(input("Ingresa la velocidad: \n"))
    consumo = horas * velocidad / 12
    print("%.3f" % consumo)


# 1018 - Billetes

def billetes():
    numero = int(input("Ingresa un numero aqui: \n"))
    print(numero)
    print(f"{numero // 100} nota(s) de R$ 100,00")
    numero %= 100
    print(f"{numero // 50} nota(s) de R$ 50,00")
    numero %= 50
    print(f"{numero // 20} nota(s) de R$ 20,00")
    numero %= 20
    print(f"{numero // 10} nota(s) de R$ 10,00")
    numero %= 10
    print(f"{numero // 5} nota(s) de R$ 5,00")
    numero %= 5
    print(f"{numero // 2} nota(s) de R$ 2,00")
    numero %= 2
    print(f"{numero} nota(s) de R$ 1,00")
    
# 1019 - Conversion de tiempo
def conversion():
    segundos = int(input("Ingresa los segundos: \n"))

    minutos = segundos // 60
    segundos -=  minutos *60
    horas = minutos // 60
    minutos -= horas * 60

    print(f"{horas}:{minutos}:{segundos}")
    
# 1020 - Edad en dias
def edad():
    dias = int(input("Ingresa los dias: \n"))
    ano = 0
    meses = 0

    ano = dias // 365
    dias = dias % 365
    meses = dias // 30
    dias = dias % 30

    print(f"{ano} ano(s)\n{meses} mes(es)\n{dias} dia(s)")
    
# 1021 - billetes y monedas

def billetesymonedas():
    A=float(input("Ingresa un numero: \n"))
    N=A
    a=N/100
    b=N%100
    c=b/50
    d=b%50
    e=d/20
    f=d%20
    g=f/10
    h=f%10
    i=h/5
    j=h%5
    k=j/2
    l=j%2

    E=A*100
    B=(int(E))
    m=B%100
    n=m/50
    o=m%50
    p=o/25
    q=o%25
    r=q/10
    s=q%10
    t=s/5
    u=s%5
    print("NOTAS:")
    print(f"{int(a)} nota(s) de R$ 100.00")
    print(f"{int(c)} nota(s) de R$ 50.00")
    print(f"{int(e)} nota(s) de R$ 20.00")
    print(f"{int(g)} nota(s) de R$ 10.00")
    print(f"{int(i)} nota(s) de R$ 5.00")
    print(f"{int(k)} nota(s) de R$ 2.00")
    print("MOEDAS:")
    print(f"{int(l)} moeda(s) de R$ 1.00")
    print(f"{int(n)} moeda(s) de R$ 0.50")
    print(f"{int(p)} moeda(s) de R$ 0.25")
    print(f"{int(r)} moeda(s) de R$ 0.10")
    print(f"{int(t)} moeda(s) de R$ 0.05")
    print(f"{int(u)} moeda(s) de R$ 0.01")

# 1035 - prueba selecion 1
def prueba1():
    a, b, c, d = map(int, input("Ingresa numeros valores: \n").split(" "))

    if ((b > c) and (d > a) and (c+d > a+b) and (c >= 0 and d >= 0) and (a%2 == 0)):
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")

# 1036 - La formula de Bhaskara

def formula_bhaskara():
    A, B, C = input("Ingresa tres numeros: \n").split()
    A = float(A)
    B = float(B)
    C = float(C)
    if A==0 or ((B*B)-(4*A*C)) < 0:
        print("Impossivel calcular")
    else:
        x1 = (-B + (math.sqrt((B * B) - (4 * A * C))))/(2*A)
        x2 = (-B - (math.sqrt((B * B) - (4 * A * C))))/(2*A)
        print("R1 = {0:.5f}".format(x1))
        print("R2 = {0:.5f}".format(x2))
        
# 1037 - Intervalo
def intervalo():
    numero = float(input("Ingresa un numero: \n"))
    if numero > 75.00001 and numero <= 100:
        print("Intervalo (75,100]")
    elif numero > 50.00001 and numero <= 75:
        print("Intervalo (50,75]")
    elif numero > 25.00001 and numero <=50:
        print("Intervalo (25,50]")
    elif numero >= 0 and numero <= 25:
        print("Intervalo [0,25]")
    else:
        print("Fora de intervalo")
        
        
# Estructuras de Control

menu = """
       ****************************************************
       *        MENU PRINCIPAL DE LA APLICACION           * 
       **************************************************** 
       
       Elija la opciòn del reto que desea ejecutar:
       1000 :  Hola Mundo
       1001 :  Extremadamente Básico
       1002 :  Area Criculo
       1003 :  Suma simple
       1004 :  Producto simple
       1005 : Promedio 1
       1006 : Promedio 2
       1007 : Diferencia
       1008 : Salario
       1009 : Salario + bono
       1010 : Calculo simple
       1011 : Esfera
       1012 : Area
       1013 : El mayor
       1014 : Consumo
       1015 : Distancia entre dos puntos
       1016 : Distancia
       1017 : Combustible gastado 
       1018 : Billetes
       1019 : Conversion de tiempo
       1020 : Edad en dias
       1021 : billetes y monedas
       1035 : prueba seleccion 1
       1036 : La formula de bhaskara
       1037 : Intervalo
         0  : Salir del programa  
"""
bandera = True


while bandera:
    print(menu)
    opcion = int (input("Elija una opción: \n"))
    if opcion == 0:
        print("Hasta pronto!!")
        break
    elif opcion == 1000:
        holamundo()
        time.sleep(0.25)
    elif opcion == 1001:
        suma()
        time.sleep(0.25)
    elif opcion == 1002:
        area_del_circulo()
        time.sleep(0.25)
    elif opcion == 1003:
        suma_simple()
        time.sleep(0.25)
    elif opcion == 1004:
        mulitplicacion()
        time.sleep(0.25)
    elif opcion == 1005:
        promedio_1()
        time.sleep(0.25)
    elif opcion == 1006:
        promedio_2()
        time.sleep(0.25)
    elif opcion == 1007:
        diferencia()
        time.sleep(0.25)
    elif opcion == 1008:
        salario()
        time.sleep(0.25)
    elif opcion == 1009:
        salario_bonus()
        time.sleep(0.25)
    elif opcion == 1010:
        calculo_simple()
        time.sleep(0.25)
    elif opcion == 1011:
        esfera()
        time.sleep(0.25)
    elif opcion == 1012:
        area()
        time.sleep(0.25)
    elif opcion == 1013:
        el_mayor()
        time.sleep(0.25)
    elif opcion == 1014:
        consumo()
        time.sleep(0.25)
    elif opcion == 1015:
        distancia()
        time.sleep(0.25)
    elif opcion == 1016:
        distancia_2()
        time.sleep(0.25)
    elif opcion == 1017:
        combustible()
        time.sleep(0.25)
    elif opcion == 1018:
        billetes()
        time.sleep(0.25)
    elif opcion == 1019:
        conversion()
        time.sleep(0.25)
    elif opcion == 1020:
        edad()
        time.sleep(0.25)
    elif opcion == 1021:
        billetesymonedas()
        time.sleep(0.25)
    elif opcion == 1035:
        prueba1()
        time.sleep(0.25)
    elif opcion == 1036:
        formula_bhaskara()
        time.sleep(0.25)
    elif opcion == 1037:
        intervalo()
        time.sleep(0.25)
    else:
        print("Opción incorrecta")
        
        
        

