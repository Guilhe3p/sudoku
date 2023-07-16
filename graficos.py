import customtkinter as ctk
import main as lg
from tkinter import StringVar

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #establezco nuestra partida lógica
        self.match = lg.Game()

        #aparciencia general de la GUI
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")
        #ventana principal

        #self.geometry("500x600")
        self.title("Sudoku")
        #contenedor de modulos de la ventana
        self.frame = ctk.CTkFrame(master=self, fg_color="white")
        self.frame.pack(pady=10,padx=10,fill="both",expand=True)

        #modulo tabla
        table = ctk.CTkFrame(master=self.frame, width=400, height=400,corner_radius=0)
        # table.grid_rowconfigure(0, weight=1)
        # table.grid_columnconfigure((0, 1, 2), weight=1)
        table.pack(padx=10)

        self.botones = [[None for i in range(9)] for i in range(9)]
        self.valores = [[None for i in range(9)] for i in range(9)]
        #modulos macro-celdas
        for i in range(9):
            macro_cell = ctk.CTkFrame(master=table,
                                      fg_color="blue",
                                      width=120,
                                      height=120,
                                      border_color="black",
                                      border_width=2,
                                      corner_radius=0)

            macro_cell.grid(row=(i//3),column=(i % 3),padx=1,pady=1)    #coloco las macro-celdas en "table" en grillas
            
            #coloco los botones dentro de cada macro-celda
            for j in range(9): 
                x = 3*(i%3)+(j%3)       #defino las posiciones reales de acuerdo con la macro-celda y botón que me encuentro
                y = 3*(i//3)+(j//3)

                self.valores[x][y] = StringVar()    #creo una StringVar de Tkinter para no tener que cambiar el valor de cada boton manualmente 
                self.valores[x][y].set("0") #agrupo todas las StringVar en la matriz valores

                cell_button = ctk.CTkButton(master=macro_cell,
                                       textvariable=self.valores[x][y],   #cada botón tendrá una posición de memoria con su StringVar correspondiente 
                                       width=40,
                                       height=40,
                                       command= lambda pos=(x,y): self.__Prueba(pos),
                                       fg_color="#C2DAAA",
                                       border_color="gray",
                                       border_width=1,
                                       corner_radius=0)
                
                cell_button.grid(row=(j//3),column=(j % 3))    #coloco los botones en grillas igual que las macro-celdas
                self.botones[x][y] = cell_button

                self.selectedCell = (0,0) #establezco a la posicion 0,0 como la seleccionada para evitar errores


        #creo la botonera
        self.keypad = ctk.CTkFrame(master=self.frame)
        self.keypad.pack(pady=10)

        for i in range(9):
            input_button = ctk.CTkButton(
                master=self.keypad,
                text=str(i+1),
                width=40,
                height=40,
                border_color="black",
                command = lambda num = i+1: self.__input(num),
                border_width=2,
                corner_radius=0)

            input_button.grid(row=(i//3),column=(i % 3),padx=1,pady=1)
        input_button = ctk.CTkButton(master=self.keypad,text="",width=40,height=40,border_color="black",command = lambda: self.__input("0"),border_width=2,corner_radius=0)
        input_button.grid(row=3,column=1,padx=1,pady=1)

    def load_game(self):
        self.match.load_random_from_file("puzzles0_kaggle")
        
        for i in range(9):
            for j in range(9):
                if self.match.matrix[j][i] == 0:
                    self.modify_cell_value(i,j,"")
                else:
                    self.modify_cell_value(i,j,self.match.matrix[j][i])

        print(self.match)

    def modify_cell_value(self,x,y,value) -> None:
        self.valores[x][y].set(value)
        

    def __Prueba(self,position):
        for i in range(9):
            self.botones[self.selectedCell[0]][i].configure(fg_color="#C2DAAA")
            self.botones[i][self.selectedCell[1]].configure(fg_color="#C2DAAA")

        for i in range(9):
            self.botones[position[0]][i].configure(fg_color="red")
            self.botones[i][position[1]].configure(fg_color="red")

        self.botones[position[0]][position[1]].configure(fg_color="red")

        self.selectedCell = (position[0],position[1])
    
    def __input(self,number):
        if self.match.play(self.selectedCell[1],self.selectedCell[0],number):
            if number == "0":
                self.valores[self.selectedCell[0]][self.selectedCell[1]].set(" ")
            else:
                self.valores[self.selectedCell[0]][self.selectedCell[1]].set(number)



graficos = App()
graficos.load_game()
graficos.mainloop()

