import numpy as np

def verify_list(lis):
        for i in range(1,10):
            if np.count_nonzero(lis == i) > 1: #count_nonzero devuelve la cantidad de elementos con valor True en este caso. lis == i devuelve una lista igual a lis pero con True donde el valor sea igual a i y False donde no
                return False
        return True

def verify_sub_matrix(matrix):  #toma una matriz y se fija si hay elementos repetidos en ella. Si los hay, devuelve False
        for i in range(1,10):
            if np.count_nonzero(matrix == i) > 1: 
                return False
        return True

class Game():
    def __init__(self) -> None:
        self.matrix = np.zeros((9,9), np.uint8) #array de 0s con tipo de dato int 8 bits (0-255)
        self.__inmmutables = []
        self.state = True

    def __str__(self) -> str:
        return (str(self.matrix)+"\n"+str(self.state))

    def load_ordered(self) -> None:
        self.matrix = np.arange(81).reshape(9,9)
    def load_special_1(self) -> None:
        self.matrix = np.array([[i%9 for i in range(j,9+j)] for j in range(9)])
    def load_random(self,magnitude) -> None:
        cont = 0
        while cont < magnitude:
            #post = np.random.randint(0,9,3,np.uint8)
            pos_value = (np.random.randint(0,9),np.random.randint(0,9),np.random.randint(1,10))
            if self.matrix[pos_value[0]][pos_value[1]]==0:
                self.matrix[pos_value[0]][pos_value[1]] = pos_value[2]
                if self.verify_game():
                    cont += 1
                else:
                    self.delete(pos_value[0],pos_value[1])
        
        self.immutables = self.matrix.nonzero()
    def load_random_from_file(self,file_name) -> None:
        file = open(file_name,"r")  #abro archivo en modo lectura
        lines = file.readlines() #cargo una lista con sus renglones
        line = lines[np.random.randint(0,len(lines))]   #elijo un reglón al azar
        mat = []    #creo una lista a cargar con los valores del renglón
        
        for i in line:  #leo cada caracter y lo agrego a "mat" según corresponda
            if i == ".":
                mat.append(0)
            elif "0" <= i <= "9":
                mat.append(int(i))

        self.matrix = np.array(mat).reshape(9,9)    #le doy forma de matriz a mat
        self.__inmmutables = np.nonzero(self.matrix)    #inmmutables tendrá las posiciones con los numeros cargados y no podrá

    def __verify_game(self) -> bool:
        for c in range(9):
            if not(verify_list(self.matrix[c])):
                self.state = False
                return False
        
        for r in range(9):
            if not(verify_list(self.matrix.T[r])):
                self.state = False
                return False
            
        for f in range(3):
            for c in range(3):
                if not(verify_sub_matrix(self.matrix[f*3:(f+1)*3,c*3:(c+1)*3])):
                    self.state = False
                    return False

        self.state = True        
        return True

    def __invalid_position(self,x,y) -> bool:
        for i in range(len(self.__inmmutables[0])): #reviso si el par (x,y) existe en en __inmmutables
            if (x,y) == (self.__inmmutables[0][i],self.__inmmutables[1][i]):
                return True
        return False
    
    def play(self,x,y,value) -> str:    #temporal return str
        if self.__invalid_position(x,y):
            return False
    
        self.matrix[x][y] = value
        self.__verify_game()
        return True

    def is_finished(self) -> bool:
        return np.count_nonzero(self.matrix) == 81 and self.state
    
# juego = Game()

# facil = 45
# dificil = 17

# juego.load_random_from_file("puzzles0_kaggle")
# print(juego)
# while not(juego.is_finished()):
#     x = int(input("x:"))
#     y = int(input("y:"))
#     v = int(input("val:"))

#     print(juego.play(x,y,v))
#     print(juego)

#  [5, 9, 6, 2, 8, 7, 1, 3, 4],
#  [8, 3, 1, 4, 5, 9, 6, 2, 7],
#  [2, 7, 4, 6, 3, 1, 9, 5, 8],
#  [6, 1, 5, 9, 7, 4, 3, 8, 2],
#  [7, 2, 3, 8, 1, 6, 5, 4, 9],
#  [4, 8, 9, 3, 2, 5, 7, 6, 1],
#  [3, 6, 7, 1, 4, 8, 2, 9, 5],
#  [9, 5, 8, 7, 6, 2, 4, 1, 3],
#  [1, 4, 2, 5, 9, 3, 8, 7, 6]





