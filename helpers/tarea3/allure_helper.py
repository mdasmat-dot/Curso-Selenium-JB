import allure

def adjuntar_error(ruta_imagen):

    allure.attach.file(
        str(ruta_imagen),
        name="captura_error",
        attachment_type=allure.attachment_type.PNG
    )