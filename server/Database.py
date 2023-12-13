import psycopg2
from typing import List, Tuple

class Database:
    """Clase para gestionar la base de datos."""

    def __init__(self, dbname: str = 'Pokemon', user: str = 'postgres', password: str = '1234', host: str = 'localhost'):
        """Inicializa la conexión a la base de datos."""
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host
        )
        self.cur = self.conn.cursor()

    def execute_query(self, query: str, params: Tuple = None) -> None:
        """Ejecuta una consulta SQL en la base de datos."""
        try:
            if params:
                self.cur.execute(query, params)
            else:
                self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")

    def fetch_all(self, query: str, params: Tuple = None) -> List[Tuple]:
        """Recupera todos los resultados de una consulta."""
        try:
            if params:
                self.cur.execute(query, params)
            else:
                self.cur.execute(query)
            return self.cur.fetchall()
        except Exception as e:
            print(f"Error al recuperar resultados: {e}")
            return []


    def check_pokemon_user_association(self, user_id: int, pokemon_id: int) -> bool:
        """Consulta si el id de un Pokémon está asociado al id de un usuario en el Pokedex."""
        query = """
            SELECT EXISTS (
                SELECT *
                FROM Pokedex
                WHERE id_usuario = %s AND id_pokemon = %s
            );
        """
        params = (user_id, pokemon_id)
        result = self.fetch_all(query=query, params=params)
        return result[0][0] if result else False

    def get_user_pokemons(self, user_id: int) -> List[Tuple[int, str]]:
        """Consulta los Pokémon que están asociados al id de un usuario en el Pokedex."""
        query = """
            SELECT id, nombre
            FROM Pokemon
            WHERE id IN (
                SELECT id_pokemon
                FROM Pokedex
                WHERE id_usuario = %s
            );
        """
        params = (user_id,)
        return self.fetch_all(query=query, params=params)

    def insert_into_pokedex(self, user_id: int, pokemon_id: int) -> None:
        """Inserta un registro en la tabla Pokedex."""
        query = """
            INSERT INTO Pokedex (id_usuario, id_pokemon)
            VALUES (%s, %s);
        """
        params = (user_id, pokemon_id)
        self.execute_query(query=query, params=params)

    def close_connection(self) -> None:
        """Cierra la conexión a la base de datos."""
        self.cur.close()
        self.conn.close()