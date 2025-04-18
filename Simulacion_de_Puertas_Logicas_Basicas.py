# Función que solicita al usuario un valor binario (0 o 1) y valida la entrada.
def validar_entrada(mensaje):
    while True:  # Se crea un ciclo que se repetirá indefinidamente hasta que el usuario ingrese un valor válido (0 o 1).
        valor = input(mensaje)  # Se pide al usuario ingresar un valor.
        if valor in ["0", "1"]:  # Acepta solo si es "0" o "1". Se evalúa como texto para evitar un ValueError, ya que si lo pedimos con int() y el usuario ingresa texto, el programa se corta abruptamente.
            return int(valor)  # Convierte el valor a entero y finaliza el bucle.
        else:
            print("Entrada inválida. Por favor, ingresá 0 o 1.")

# Función que simula la puerta lógica AND (conjunción).
def puerta_and(a, b):
    return a and b

# Función que simula la puerta lógica OR (disyunción).
def puerta_or(a, b):
    return a or b

# Función que simula la puerta lógica NOT (negación) aplicada a un valor.
def puerta_not(a):
    return int(not a)  # Convierte el valor a entero para que devuelva un número y no una expresión booleana.

# Función que simula la puerta lógica NAND (negación de AND).
def puerta_nand(a, b):
    return int(not (a and b))  # Convierte el valor a entero para que devuelva un número y no una expresión booleana.

# Función que simula la puerta lógica NOR (negación de OR).
def puerta_nor(a, b):
    return int(not (a or b))  # Convierte el valor a entero para que devuelva un número y no una expresión booleana.

# Función que simula la puerta lógica XOR (disyunción exclusiva).
def puerta_xor(a, b):
    return int((a and not b) or (not a and b))  # Convierte el valor a entero para que devuelva un número y no una expresión booleana.

# Se pide al usuario ingresar valores binarios a través de la función validar_entrada, la cual verifica que los valores sean binarios.
print("Simulación de puertas lógicas")
a = validar_entrada("Ingrese el primer valor (0 o 1): ")
b = validar_entrada("Ingrese el segundo valor (0 o 1): ")

# Se muestra el resultado de las operaciones lógicas.
print("\nResultados de operaciones lógicas:")
print(f"AND:  {a} AND {b} = {puerta_and(a, b)}")
print(f"OR:   {a} OR {b} = {puerta_or(a, b)}")
print(f"NOT:  NOT {a} = {puerta_not(a)}")
print(f"      NOT {b} = {puerta_not(b)}")
print(f"NAND: {a} NAND {b} = {puerta_nand(a, b)}")
print(f"NOR:  {a} NOR {b} = {puerta_nor(a, b)}")
print(f"XOR:  {a} XOR {b} = {puerta_xor(a, b)}")