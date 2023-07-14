import customtkinter as ctk
from tkinter import StringVar

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #aparciencia general de la GUI
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")
        #ventana principal

        self.geometry("500x500")
        self.title("Sudoku")
        #contenedor de modulos de la ventana
        self.frame = ctk.CTkFrame(master=self, fg_color="red")
        self.frame.pack(pady=10,padx=10,fill="both",expand=True)

        #modulo tabla
        table = ctk.CTkFrame(master=self.frame, width=400, height=400,corner_radius=0)
        # table.grid_rowconfigure(0, weight=1)
        # table.grid_columnconfigure((0, 1, 2), weight=1)
        table.pack(padx=10)

        self.botones = []
        self.valores = []
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
                variable = StringVar()  #creo una StringVar de Tkinter para no tener que cambiar el valor de cada boton manualmente
                variable.set(str(j))    
                self.valores.append(variable) #agrupo todas las StringVar en la lista valores

                self.botones.append(ctk.CTkButton(master=macro_cell,
                                       textvariable=self.valores[-1],   #cada botón tendrá una posición de memoria con su StringVar correspondiente 
                                       width=40,
                                       height=40,
                                       command= lambda pos=(i,j): self.__Prueba(pos),
                                       border_color="gray",
                                       border_width=1,
                                       corner_radius=0)
                )
                self.botones[-1].grid(row=(j//3),column=(j % 3))    #coloco los botones en grillas igual que las macro-celdas


    def modify_cell_value(self,cell_num,cell_pos, value) -> None:
        self.valores[9*cell_num + cell_pos].set(value)

    def modify_cell_style(self,cell_num,cell_pos) -> None:
        self.botones[9*cell_num + cell_pos].configure(fg_color="red")

    def __Prueba(self,position):
        ColumFil = (3*(position[0]%3)+(position[1]%3),3*(position[0]//3)+(position[1]//3))
        print(ColumFil)
        self.modify_cell_value(position[0],position[1],"20")
        self.modify_cell_style(position[0],position[1])



graficos = App()
graficos.mainloop()

