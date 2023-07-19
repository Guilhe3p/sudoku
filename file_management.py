import sys
import os

def resource_path(relative_path):
    #función para obtener el directorio temporal que crea el ejecutable y agregarselo a nuestra ruta relativa.
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def set_game_data_directory():
    directory_path = os.path.join(os.path.expanduser('~'), "sudoku")
    full_path_to_game_data = os.path.join(directory_path, "game_data")
    
    try:
        open(full_path_to_game_data,"r")
    except FileNotFoundError:
        with open(resource_path("puzzles0_kaggle"),"r") as file:
            line:str = ""
            for char in file.readline():
                if char == ".":
                    line += "0"
                else:
                    line += char

            if not(os.path.isdir(directory_path)):
                os.mkdir(directory_path)
            
            with open(full_path_to_game_data,"w") as game_data_file:
                game_data_file.write(line*2+"0")
    finally:
        return full_path_to_game_data
