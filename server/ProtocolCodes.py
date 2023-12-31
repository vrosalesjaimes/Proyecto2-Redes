from enum import Enum

class ProtocolCodes(Enum):
    SOLICITAR_ID = 10
    SOLICITAR_POKEMON = 11
    SOLICITAR_LISTA_POKEMONES = 12

    CAPTURAR_POKEMON = 20
    INTENTAR_CAPTURA_NUEVO = 21
    ENVIAR_POKEMON = 22
    ENVIAR_LISTA_POKEMONES = 23

    SI = 30
    NO = 31
    TERMINAR_SESION = 32

    CONSULTAR_DATOS_USUARIO = 40
    INSERCION_EN_BASE_DE_DATOS = 41
    CONSULTANDO_POKEMONES = 42

    ERROR_USUARIO_NO_ENCONTRADO = 50