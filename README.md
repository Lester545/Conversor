# Conversor numérico en Django

Convierte números binarios a decimal y octal sin usar `int(x, 2)` ni `oct()`.

## Ejecutar

```bash
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

Abrir: http://127.0.0.1:8000/

## Estructura MVT

* `conversor/conversiones.py`: lógica. `binario_a_decimal` (ciclo `decimal*2+digito`),
  `binario_a_octal` (primero a decimal, luego divisiones entre 8, caso `0`).
* `conversor/views.py:index`: recibe POST, valida en servidor, llama conversión, envía contexto.
* `conversor/templates/conversor/index.html`: formulario, resultado, error.
* Modelo: no se usa BD. Si hubiera historial, un modelo `Conversion(binario, tipo, resultado, fecha)`
  guardaría cada cálculo; la vista lo crearía y la plantilla lo listaría.

## Validaciones (servidor en `views.py`)

* Vacío -> "Ingrese un número binario."
* Caracteres distintos de 0/1 -> rechazo (`10201`, `abc`, `10 01`).
* Tipo no permitido -> rechazo.

## Algoritmos

Decimal: la posición importa. Recorrer de izquierda a derecha con
`decimal = decimal*2 + digito` equivale a sumar `bit * 2^posición`.

Octal: `residuo = decimal % 8` da el dígito menos significativo,
`decimal //= 8` lo quita. Se anteponen los dígitos para leer en orden correcto.
Caso `0` devuelve `"0"`.

Ejemplo `110101`:
`32+16+0+4+0+1=53`, luego `53//8=6 resto 5`, `6//8=0 resto 6` -> `65`.

## Pruebas

Válidas: `0->0/0`, `1->1/1`, `1010->10/12`, `110101->53/65`,
`11111111->255/377`, `000101->5/5`.

Inválidas: `""`, `10201`, `abc`, `"10 01"` -> muestran error y permiten reintentar.

## Arquitectura

* La computadora usa binario porque el hardware distingue dos estados (apagado/encendido).
* Octal agrupa 3 bits (`2^3=8`), ej. `110|101 = 6|5`.
* Mayor entero sin signo con 8 bits: `255` (`11111111`).
