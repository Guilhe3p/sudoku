import app 

if __name__ == "__main__":
    aplication = app.App()
    #aplication.new_game()
    aplication.load_game()

    aplication.crono_update()
    aplication.mainloop()