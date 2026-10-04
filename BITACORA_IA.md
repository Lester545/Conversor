# Bitácora de uso de IA (ejemplo para completar)

## 1. Comprensión
* Consulté: "Revisa mi pseudocódigo de conversión binaria, señala errores y dame pistas sin escribir la solución completa".
* Recomendó: usar `decimal*2+digito` en vez de potencias y tratar el cero aparte en octal.
* Acepté el ciclo `*2` porque es más simple y muestra el peso posicional. Descarté usar `pow()`.
* Verifiqué: calculé a mano 110101 -> 53.

## 2. Desarrollo
* Consulté: "Mi formulario no envía datos a la vista, ¿por qué?".
* Recomendó: revisar `method="post"`, `name="binario"`, `{% csrf_token %}` y `request.POST.get()`.
* Acepté y corregí el `name` del input.
* Verifiqué: envié 1010 y llegó a la vista.

## 3. Verificación
* Consulté: "Revisa mis casos de prueba y sugiere entradas que revelen errores".
* Recomendó: probar `0`, `000101`, `""`, `10201`, `abc`, `"10 01"` y tipo inválido.
* Acepté todos y comprobé que los inválidos muestren error.
* Verifiqué: tabla de pruebas en README coincide con la app.
