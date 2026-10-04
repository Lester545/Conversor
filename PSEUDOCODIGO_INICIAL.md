# Análisis previo (versión inicial, antes de usar IA)

## 1. Entradas, proceso, salidas
* Entrada: texto binario y opción decimal/octal.
* Proceso: validar vacío, solo 0/1, opción válida; convertir con ciclo.
* Salida: original, tipo, resultado o error.

## 2. Pseudocódigo
FUNCION binario_a_decimal(binario):
  decimal = 0
  PARA cada c EN binario:
    digito = 1 si c == '1' sino 0
    decimal = decimal * 2 + digito
  RETORNAR decimal

FUNCION binario_a_octal(binario):
  decimal = binario_a_decimal(binario)
  SI decimal == 0: RETORNAR "0"
  octal = ""
  MIENTRAS decimal > 0:
    residuo = decimal % 8
    octal = texto(residuo) + octal
    decimal = decimal // 8
  RETORNAR octal

## 3. Conversión manual 110101_2
Decimal: 1*32 + 1*16 + 0*8 + 1*4 + 0*2 + 1*1 = 53
Octal: 53 // 8 = 6 resto 5; 6 // 8 = 0 resto 6 -> 65_8.
Comprobación: 110|101 = 6|5.

## 4. Recorrido de datos
formulario -> ruta (urls.py) -> vista (views.py valida) ->
función (conversiones.py) -> plantilla (muestra resultado/error).
