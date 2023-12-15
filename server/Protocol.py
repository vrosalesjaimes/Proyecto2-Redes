import socket
import threading
import time
from enum import Enum
from server.ProtocolCodes import ProtocolCodes
from server.Database import Database

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Servidor escuchando en {self.host}:{self.port}")
        self.pockedex = Database()

    def handle_client(self, client_socket, address):
        print(f"Conexión aceptada desde {address}")

        try:
            # Estado s0
            self.send_message(client_socket, ProtocolCodes.SOLICITAR_ID)

            # Estado s1
            user_id = self.receive_message(client_socket)
            if not self.authenticate_user(user_id):
                self.send_message(client_socket, ProtocolCodes.NO)
                return

            self.send_message(client_socket, ProtocolCodes.SI)

            # Estado s2
            request_code = self.receive_message(client_socket)
            if request_code == ProtocolCodes.SOLICITAR_POKEMON:
                # Lógica para manejar la solicitud de Pokémon
                pass
            elif request_code == ProtocolCodes.CAPTURAR_POKEMON:
                # Lógica para manejar la captura de Pokémon
                pass
            elif request_code == ProtocolCodes.SOLICITAR_LISTA_POKEMONES:
                # Lógica para manejar la solicitud de la lista de Pokémon
                pass
            else:
                self.send_message(client_socket, ProtocolCodes.ERROR_USUARIO_NO_ENCONTRADO)
                return

            # Estado s3
            self.send_message(client_socket, ProtocolCodes.ENVIAR_POKEMON)

            # Estado s4
            response_code = self.receive_message(client_socket)
            if response_code == ProtocolCodes.SI:
                # Lógica para manejar la confirmación del cliente
                pass
            elif response_code == ProtocolCodes.NO:
                # Lógica para manejar el rechazo del cliente
                pass
            else:
                self.send_message(client_socket, ProtocolCodes.ERROR_USUARIO_NO_ENCONTRADO)
                return

            # Implementa más estados según sea necesario

        except Exception as e:
            print(f"Error en la conexión con {address}: {e}")
        finally:
            client_socket.close()
            print(f"Conexión cerrada con {address}")

    def send_message(self, socket, code):
        # Implementa la lógica para enviar mensajes al cliente
        pass

    def receive_message(self, socket):
        # Implementa la lógica para recibir mensajes del cliente
        pass

    def authenticate_user(self, user_id):
        self.pockedex.user_by_id(user_id)

    def start(self):
        try:
            while True:
                client_socket, address = self.server_socket.accept()
                client_handler = threading.Thread(target=self.handle_client, args=(client_socket, address))
                client_handler.start()

        except KeyboardInterrupt:
            print("Servidor interrumpido. Cerrando conexiones.")
        finally:
            self.server_socket.close()

if __name__ == "__main__":
    server = Server("localhost", 9999)
    server.start()
