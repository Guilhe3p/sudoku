import customtkinter as ctk

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
        table.grid_rowconfigure(0, weight=1)
        table.grid_columnconfigure((0, 1, 2), weight=1)
        table.pack(padx=10)

        #modulos macro-celdas
        for i in range(9):
            macro_cell = ctk.CTkFrame(master=table,
                                      fg_color="blue",
                                      width=120,
                                      height=120,
                                      border_color="black",
                                      border_width=2,
                                      corner_radius=0)

            macro_cell.grid(row=(i//3),column=(i % 3),padx=1)
                
            for j in range(9):
                ctk.Ctk
                button = ctk.CTkButton(master=macro_cell,
                                       text=str(i),
                                       width=40,
                                       height=40,
                                       command= lambda: self.__Prueba(j),
                                       border_color="gray",
                                       border_width=1,
                                       corner_radius=0)
                button.grid(row=(j//3),column=(j % 3))



    def start(self):
        self.mainloop()

    def __Prueba(self,position):
        print(position)
        #((j//3),(j % 3))

graficos = App()
graficos.start()


# def Prueba():
#     print("probando")
#     print("numero ingresado:",entry1.get())

# frame = ctk.CTkFrame(master=root)
# frame.pack(pady=20,padx=10,fill="both",expand=True)

# label = ctk.CTkLabel(master=frame,text="Prueba Sudoku")
# label.pack(pady=12,padx=10)

# entry1 = ctk.CTkEntry(master=frame,placeholder_text="numeros del 0 al 9")
# entry1.pack(pady=12,padx=10)

# button = ctk.CTkButton(master=frame,text="enviar numero", command=Prueba)
# button.pack(pady=12,padx=10)

# root.mainloop()
