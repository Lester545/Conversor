# Lógica de conversión. No usa int(x, 2), oct(), eval().
# Solo se permiten operaciones aritméticas: + * // %


def binario_a_decimal(binario: str) -> int:
    """Convierte texto binario a decimal usando ciclo.

    Cada posición vale el doble que la anterior:
    decimal = decimal * 2 + digito
    """
    decimal = 0
    for c in binario:
        digito = 1 if c == "1" else 0
        decimal = decimal * 2 + digito
    return decimal


def binario_a_octal(binario: str) -> str:
    """Convierte binario a octal en dos pasos.

    1. binario -> decimal con binario_a_decimal.
    2. decimal -> octal con divisiones sucesivas entre 8.
       El residuo (% 8) es el dígito, se lee de atrás hacia adelante.
    """
    decimal = binario_a_decimal(binario)
    if decimal == 0:
        return "0"
    digitos = ""
    while decimal > 0:
        residuo = decimal % 8
        # str(residuo) solo pasa el número a texto, no convierte bases.
        digitos = str(residuo) + digitos
        decimal = decimal // 8
    return digitos
