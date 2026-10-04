from django.shortcuts import render

from .conversiones import binario_a_decimal, binario_a_octal


def index(request):
    """Muestra el formulario (GET) y procesa la conversión (POST)."""
    resultado = None
    error = None
    valor = ""
    tipo = "decimal"

    if request.method == "POST":
        # 1. Recibir datos del formulario
        valor = request.POST.get("binario", "").strip()
        tipo = request.POST.get("tipo", "decimal")

        # 2. Validar en el servidor
        if valor == "":
            error = "Ingrese un número binario."
        elif any(c not in "01" for c in valor):
            error = "Solo se permiten los caracteres 0 y 1."
        elif tipo not in ("decimal", "octal"):
            error = "Tipo de conversión no permitido."
        else:
            # 3. Procesar con la función de conversión
            if tipo == "decimal":
                resultado = str(binario_a_decimal(valor))
            else:
                resultado = binario_a_octal(valor)

    # 4. Mostrar plantilla con el contexto
    contexto = {
        "valor": valor,
        "tipo": tipo,
        "resultado": resultado,
        "error": error,
        "cantidad_digitos": len(valor) if valor else 0,
    }
    return render(request, "conversor/index.html", contexto)
