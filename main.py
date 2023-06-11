import numpy as np

def verify_list(lis):
        for i in range(1,10):
            if np.count_nonzero(lis == i) > 1: #count_nonzero devuelve la cantidad de elementos con valor True en este caso. lis == i devuelve una lista igual a lis pero con True donde el valor sea igual a i y False donde no
                return False
        return True

def verify_sub_matrix(matrix):
        for i in range(1,10):
            if np.count_nonzero(matrix == i) > 1: 
                return False
        return True

class Game():
    def __init__(self):
        self.matrix = np.zeros((9,9), np.uint8) #array de 0s con tipo de dato int 8 bits (0-255)
        self.matrix = np.arange(81).reshape(9,9)
        
    def verify_game(self):
        for c in range(9):
            if not(verify_list(self.matrix[c])):
                return False
        
        for r in range(9):
            if not(verify_list(self.matrix.T[r])):
                return False
            
        for f in range(3):
            for c in range(3):
                verify_sub_matrix(self.matrix[f*3:(f+1)*3,c*3:(c+1)*3])

        return True

    def delete(self,x,y):
         self.matrix[x][y] = 0
    
    def play(self,x,y,value):
         preValue = self.matrix[x][y]
         self.matrix[x][y] = value

         if self.verify_game():
            return "JUGADA VALIDA"
         else:
            self.matrix[x][y] = preValue
            return "JUGADA INVALIDA"
    
juego = Game()

print(juego.play(0,0,101))



