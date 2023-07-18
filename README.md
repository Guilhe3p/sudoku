Este proyecto trata sobre la realización del juego Sudoku en Python con una interfaz gráfica integrada 

-La librería elegida para la GUI es CustomTkinter. Su código se encuentra en "app.py".
Para el cronómetro de la partida he usado también el módulo "time". La implementación es hecha mediante una clase "App" que hereda
los métodos y atributos de "customtkinter.CTk".

-La lógica del juego es independiente de la GUI y se encuentra en el archivo "game_logic.py" implementada mediante la clase Game.
Para crear una nueva partida el método load_random_from_file() carga una partida aleatoria de "puzzles0_kaggle". Este archivo con-
tiente 100.000 partidas de sudoku "bien definidas" es decir con única solución.

-Por último game_data almacena los datos de la última partida. La primera linea almacena los datos iniciales del juego, es decir
las grillas que no pueden ser modificadas, la segunda almacena la partida actual y la tercera el tiempo de juego.

-El flujo de información podría definirse como

puzzles0_kaggle ------> game_logic -<->-\
                            |            |
                            |        game_data
                            |            |
                           app ----->---/
                            |
                            |
                          |main|
