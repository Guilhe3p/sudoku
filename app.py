from customtkinter import CTk,set_appearance_mode,set_default_color_theme,CTkFrame,CTkLabel,CTkButton
from time import time
from tkinter import StringVar
import game_logic as lg
import file_management

class App(CTk):
    def __init__(self) -> None:
        super().__init__()
        #busco la ruta de nuestros archivos
        self.game_data_path = file_management.set_game_data_directory()
            
        #establezco nuestra partida lógica
        self.match = lg.Game()

        #aparciencia general de la GUI
        set_appearance_mode("System")
        set_default_color_theme("blue")

        #ventana principal
        self.resizable(False,False)
        self.title("Sudoku")

        #contenedor de modulos de la ventana
        self.frame = CTkFrame(master=self, fg_color="white")
        self.frame.pack(pady=10,padx=10,fill="both",expand=True)

        #modulo superior
        self.top_module = CTkFrame(master=self.frame,fg_color="white")
        self.top_module.pack(pady=20)
            #botón nueva partida
        self.new_game_button = CTkButton(master=self.top_module,text="Nueva Partida",command=lambda: self.new_game())
        self.new_game_button.grid(row=0,column=0,padx=20)

            #reloj
        self.cronometro = CTkLabel(master=self.top_module, text="00:00:00", width=100, height=30,corner_radius=0, fg_color="white")
        self.cronometro.grid(row=0,column=1,padx=20)

        #modulo tabla
        table = CTkFrame(master=self.frame, width=400, height=400,corner_radius=0, fg_color="black", border_color="black", border_width=20)
        table.pack(padx=10)

            #matrices con los objetos botones y sus StringVar asociadas
        self.botones:list = [[None for i in range(9)] for i in range(9)]
        self.valores:list = [[None for i in range(9)] for i in range(9)]
            #modulos macro-celdas
        for i in range(9):
            macro_cell = CTkFrame(master=table,
                                      fg_color="blue",
                                      width=120,
                                      height=120,
                                      border_color="black",
                                      border_width=2,
                                      corner_radius=0)

            macro_cell.grid(row=(i//3),column=(i % 3),padx=1,pady=1)    #coloco las macro-celdas en "table" en grillas
            
            #coloco los botones dentro de cada macro-celda
            for j in range(9): 
                x:int = 3*(i%3)+(j%3)       #defino las posiciones reales de acuerdo con la macro-celda y botón que me encuentro
                y:int = 3*(i//3)+(j//3)

                self.valores[x][y] = StringVar()    #creo una StringVar de Tkinter para no tener que cambiar el valor de cada boton manualmente 
                self.valores[x][y].set("0") #agrupo todas las StringVar en la matriz valores

                cell_button = CTkButton(master=macro_cell,
                                       textvariable=self.valores[x][y],   #cada botón tendrá una posición de memoria con su StringVar correspondiente 
                                       text_color="black",
                                       width=40,
                                       height=40,
                                       command= lambda pos=(x,y): self.__pointer(pos),
                                       fg_color="white",
                                       hover_color="#98B9E2",
                                       font=("Arial",16),
                                       border_color="gray",
                                       border_width=1,
                                       corner_radius=0)
                
                cell_button.grid(row=(j//3),column=(j % 3))    #coloco los botones en grillas igual que las macro-celdas
                self.botones[x][y] = cell_button

                self.selectedCell = (0,0) #establezco a la posicion 0,0 como la seleccionada para evitar errores

            #creo la botonera
        self.keypad = CTkFrame(master=self.frame,fg_color="white")
        self.keypad.pack(pady=10)

        for i in range(9):
            input_button = CTkButton(
                master=self.keypad,
                text=str(i+1),
                font=("Arial",16),
                width=40,
                height=40,
                border_color="black",
                command = lambda num = i+1: self.__input(num),
                border_width=2,
                corner_radius=0)

            input_button.grid(row=(i//3),column=(i % 3),padx=1,pady=1)
        input_button = CTkButton(master=self.keypad,text="",width=124,height=40,border_color="black",command = lambda: self.__input("0"),border_width=2,corner_radius=0)
        input_button.grid(row=3,column=0,padx=1,pady=1,columnspan=3)
        #fin __init__

    def new_game(self) -> None:
        self.start_time = time()
        self.match.load_random_from_file()
        game_data_file = open(self.game_data_path,"w")

        line:str = ""
        
        for i in range(9):
            for j in range(9):
                line += str(self.match.matrix[i][j])

        game_data_file.write(line+"\n"+line+"\n0")

        game_data_file.close()

        self.load_game()

    def load_game(self) -> None:
        #abro game_data y establezco el nuevo tiempo de inicio para el cronómetro
        game_data_file = open(self.game_data_path,"r")
        game_data_file.seek(164)
        self.start_time = time() - int(game_data_file.readline())

        #cargo la partida lógica
        self.match.load_from_game_data()

        #obtengo los datos de la matriz "logica" y los coloco en la tabla central
        for i in range(9):
            for j in range(9):

                if self.match.matrix[j][i] == 0:
                    self.modify_cell_value(i,j,"")
                    self.botones[i][j].configure(text_color="black")
                else:
                    self.modify_cell_value(i,j,self.match.matrix[j][i])
                    self.botones[i][j].configure(text_color="black")
                    if self.match.invalid_position(j,i):
                        self.botones[i][j].configure(text_color="green") #font=("Arial",16,"bold")

        game_data_file.close()
        #fin load_game()

    def save_current_game_data(self):
        game_data_file = open(self.game_data_path,"r+")
        game_data_file.seek(82)
        
        for i in range(9):
            for j in range(9):
                game_data_file.write(str(self.match.matrix[i][j]))

        game_data_file.close()

    def modify_cell_value(self,x,y,value) -> None:
        self.valores[x][y].set(value)
        
    def __pointer(self,position):
        for i in range(9):
            self.botones[self.selectedCell[0]][i].configure(fg_color="white")
            self.botones[i][self.selectedCell[1]].configure(fg_color="white")

        for i in range(9):
            self.botones[position[0]][i].configure(fg_color="#98B9E2")
            self.botones[i][position[1]].configure(fg_color="#98B9E2")

        self.botones[position[0]][position[1]].configure(fg_color="#8DB0DB")

        self.selectedCell = (position[0],position[1])
    
    def __input(self,number):
        if self.match.play(self.selectedCell[1],self.selectedCell[0],number):
            if number == "0":
                self.valores[self.selectedCell[0]][self.selectedCell[1]].set("")
            else:
                self.valores[self.selectedCell[0]][self.selectedCell[1]].set(number)
            
            self.save_current_game_data()

            if self.match.is_finished():
                print("Haz ganado")
                self.after_cancel(self.crono_function_id)
                
    def crono_update(self) -> None:
        self.match_time = int(time()-self.start_time)
        hours = str(self.match_time // 3600)
        if len(hours)==1:
            hours = "0"+hours

        minutes = str((self.match_time // 60)%60)
        if len(minutes)==1:
            minutes = "0"+minutes

        seconds = str(self.match_time%60)
        if len(seconds)==1:
            seconds = "0"+seconds

        tiempo = f'{hours}:{minutes}:{seconds}'

        self.cronometro.configure(text=tiempo)

        with open(self.game_data_path,"r+") as game_data_file:
            game_data_file.seek(164)
            game_data_file.write(str(self.match_time))
        
        self.crono_function_id = self.after(1000,self.crono_update)



