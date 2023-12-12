-- Crear la tabla de Pokémon
CREATE TABLE Pokemon (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    imagen_nombre VARCHAR(50) NOT NULL
);

-- Crear la tabla de Usuarios
CREATE TABLE Usuario (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    nivel INT NOT NULL
);

-- Crear la tabla intermedia para el Pokedex
CREATE TABLE Pokedex (
    id_usuario INT,
    id_pokemon INT,
    PRIMARY KEY (id_usuario, id_pokemon),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id),
    FOREIGN KEY (id_pokemon) REFERENCES Pokemon(id)
);

-- Inserciones de ejemplo para la tabla de Usuarios
INSERT INTO Usuario (id, nombre, nivel) VALUES
    (1, 'Ash Ketchum', 10),
    (2, 'Misty', 8),
    (3, 'Brock', 9),
    (4, 'Gary Oak', 12),
    (5, 'Serena', 7),
    (6, 'Cynthia', 15),
    (7, 'Red', 14),
    (8, 'EeveeLover23', 6),
    (9, 'PikachuFan', 5),
    (10, 'JigglypuffMaster', 3);

-- Inserciones de ejemplo para la tabla de Pokémon
INSERT INTO Pokemon (id, nombre, imagen_nombre) VALUES
    (1, 'Bulbasaur', 'bulbasaur.png'),
    (2, 'Charmander', 'charmander.png'),
    (3, 'Squirtle', 'squirtle.png'),
    (4, 'Pikachu', 'pikachu.png'),
    (5, 'Eevee', 'eevee.png'),
    (6, 'Gyarados', 'gyarados.png'),
    (7, 'Jigglypuff', 'jigglypuff.png'),
    (8, 'Snorlax', 'snorlax.png'),
    (9, 'Machamp', 'machamp.png'),
    (10, 'Alakazam', 'alakazam.png'),
    (11, 'Articuno', 'articuno.png'),
    (12, 'Zapdos', 'zapdos.png'),
    (13, 'Moltres', 'moltres.png'),
    (14, 'Dragonite', 'dragonite.png'),
    (15, 'Mew', 'mew.png'),
    (16, 'Lugia', 'lugia.png'),
    (17, 'Ho-Oh', 'ho-oh.png'),
    (18, 'Tyranitar', 'tyranitar.png'),
    (19, 'Rayquaza', 'rayquaza.png'),
    (20, 'Groudon', 'groudon.png'),
    (21, 'Kyogre', 'kyogre.png'),
    (22, 'Latias', 'latias.png'),
    (23, 'Latios', 'latios.png'),
    (24, 'Garchomp', 'garchomp.png'),
    (25, 'Lucario', 'lucario.png'),
    (26, 'Greninja', 'greninja.png'),
    (27, 'Infernape', 'infernape.png'),
    (28, 'Empoleon', 'empoleon.png'),
    (29, 'Torterra', 'torterra.png'),
    (30, 'Darkrai', 'darkrai.png'),
    (31, 'Arceus', 'arceus.png'),
    (32, 'Celebi', 'celebi.png'),
    (33, 'Deoxys', 'deoxys.png'),
    (34, 'Giratina', 'giratina.png'),
    (35, 'Regigigas', 'regigigas.png'),
    (36, 'Heatran', 'heatran.png'),
    (37, 'Cresselia', 'cresselia.png'),
    (38, 'Manaphy', 'manaphy.png'),
    (39, 'Phione', 'phione.png'),
    (40, 'Victini', 'victini.png'),
    (41, 'Reshiram', 'reshiram.png'),
    (42, 'Zekrom', 'zekrom.png'),
    (43, 'Kyurem', 'kyurem.png'),
    (44, 'Xerneas', 'xerneas.png'),
    (45, 'Yveltal', 'yveltal.png'),
    (46, 'Zygarde', 'zygarde.png'),
    (47, 'Solgaleo', 'solgaleo.png'),
    (48, 'Lunala', 'lunala.png'),
    (49, 'Necrozma', 'necrozma.png'),
    (50, 'Mewtwo', 'mewtwo.png');