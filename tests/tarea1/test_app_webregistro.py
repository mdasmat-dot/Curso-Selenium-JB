import pytest

from playground.tarea1.app_web_registro import (
    validar_registro,
    generar_correo
)
# =====================================
# FIXTURE CASOS REGISTRO
# =====================================

@pytest.fixture(scope="session")
def casos_registro():

    return [

        {
            "correo": "",
            "clave": "1234567",
            "confirmacion": "1234567",
            "mensaje": "Debe completar todos los campos"
        },

        {
            "correo": "adminmail.com",
            "clave": "1234567",
            "confirmacion": "1234567",
            "mensaje": "El correo no es válido"
        },

        {
            "correo": "admin@mail.com",
            "clave": "1234567",
            "confirmacion": "1234567",
               "mensaje": "Registro exitoso"
        }

    ]


# =====================================
# TEST CASOS REGISTRO
# =====================================

def test_casos_registro_fixture(casos_registro):

    for caso in casos_registro:

        resultado = validar_registro(
            caso["correo"],
            caso["clave"],
            caso["confirmacion"]
        )

        assert resultado == caso["mensaje"]


# =====================================
# TEST SMOKE
# =====================================

@pytest.mark.smoke
def test_generar_correo_smoke():

    correo = generar_correo(
        "admin",
        "mario"
    )

    assert correo == "admin.mario@mail.com"