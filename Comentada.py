import time

def sumar(num1,num2):
    resultado_suma = num1 + num2
    return(resultado_suma)

def restar(num1,num2):
    resultado_resta = num1 - num2
    return(resultado_resta)

def dividir(num1,num2):
    try:
        resultado_division = num1 / num2
        return(resultado_division)
    except ZeroDivisionError:
        time.sleep(3)
        print("Error, no se puede dividir por cero.")

def multiplicar(num1,num2):
    resultado_multiplicar =  num1 * num2
    return(resultado_multiplicar)

def mostrar_menu():
    print("─── ･ ｡ﾟ☆: *.☽ .* :☆ﾟ. ───")
    print("MENÚ DE CALCULADORA EN PYTHON૮ ˶ᵔ ᵕ ᵔ˶ ა")
    print("─── ･ ｡ﾟ☆: *.☽ .* :☆ﾟ. ───")
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4. DIVIDIR")
    print("5. SALIR")

def obtener_numero():
    while True:
        try:
            num1 = int(input("Ingrese el primer número a operar:\n"))
            num2 = int(input("Ingrese el segundo número a operar:\n"))
            return num1,num2
        except ValueError:
            print("Error, ingrese números válidos.")

def main():

    #CICLO PARA REPETIR MENÚ
    
    while True:
        #Llamar a la función mostrar menú.
        mostrar_menu()
        #Menú opciones según el número ingresado.


        #Ingresar una opción.
        try:
            op = int(input("\nPor favor, ingresa una opción del 1 al 5."))
        except ValueError:
            print("Error, ha ingresado un valor no númerico.")
            time.sleep(3)

        #Validar que el número ingresado sea una opción de 1 a 5
        if op < 1 or op > 5:
            print("Ha ingresado una opción no válida.")
            time.sleep(3)
        
        #Si la opción ingresada es una de esas 4 opciones, pasa dentro del
        if op in [1,2,3,4]:
            #En la variable num1 y num2 guardan los datos ingresados.
            #En la función obtener números.
            num1,num2 = obtener_numero()

            if op == 1:
                resultado = sumar(num1,num2)
                print(f"El resultado de la suma es: {resultado}\n")
                time.sleep(2)

            if op == 2:
                resultado = restar(num1,num2)
                print(f"El resultado de la resta es: {resultado}\n")
                time.sleep(2)

            if op == 3:
                resultado = multiplicar(num1,num2)
                print(f"El resultado de la multiplicación es: {resultado}\n")
                time.sleep(2)

            if op == 4:
                resultado = dividir(num1,num2)
                print(f"El resultado de la división es: {resultado}\n")
                time.sleep(2)

        if op == 5:
            print("Muchas gracias por utilizar este programa. ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧")
