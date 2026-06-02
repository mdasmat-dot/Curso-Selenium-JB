# Validar registro
def validar_registro(correo, clave, confirmacion):

    # Validar campos vacíos
    if correo == "" or clave == "" or confirmacion == "":
        return "Debe completar todos los campos"

    # Validar correo
    if "@" not in correo:
        return "El correo no es válido"

    # Validar longitud de clave
    if len(clave) <= 6:
        return "La clave debe tener más de 6 caracteres"

    # Validar confirmación
    if clave != confirmacion:
        return "Las contraseñas no coinciden"

    return "Registro exitoso"


# Generar correo
def generar_correo(rol, nombre):

    # Validar parámetros vacíos
    if rol == "" or nombre == "":
        return "Debe completar rol y nombre"

    return f"{rol}.{nombre}@mail.com"