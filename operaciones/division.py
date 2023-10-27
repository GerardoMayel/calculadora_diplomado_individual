from numerical_validation import is_number


def dividir(num1, num2):
    if not is_number(num1) or not is_number(num2):
        raise ValueError("Error: Alguna de las entradas no es un número.")

    n1 = float(num1)
    n2 = float(num2)

    if n2 == 0:
        raise ValueError("Error: División por cero no permitida.")

    return n1 / n2
