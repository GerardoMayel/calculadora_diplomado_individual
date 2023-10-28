from operaciones.suma import sumar
from operaciones.resta import restar
from operaciones.multiplicacion import multiplicar
from operaciones.division import dividir


def is_number(value):
    """Verifica si el valor es un número."""
    try:
        float(value)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    # Entrada del usuario
    while True:
        num1 = input("Ingresa el primer número (o 'salir' para terminar): ")
        if num1.lower() == 'salir':
            break

        if not is_number(num1):
            print("Error: El primer número ingresado no es válido.")
            continue

        num2 = input("Ingresa el segundo número: ")

        if not is_number(num2):
            print("Error: El segundo número ingresado no es válido.")
            continue

        operacion = input("Elige una operación (+, -, *, /): ")

        try:
            if operacion == '+':
                resultado = sumar(num1, num2)
            elif operacion == '-':
                resultado = restar(num1, num2)
            elif operacion == '*':
                resultado = multiplicar(num1, num2)
            elif operacion == '/':
                resultado = dividir(num1, num2)
            else:
                print("Operación no válida.")
                continue

            print(f"Resultado: {resultado}\n")
        except ValueError as e:
            print(f"{e}\n")
