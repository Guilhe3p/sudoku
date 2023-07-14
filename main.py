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
    def __init__(self):
        self.matrix = np.zeros((9,9), np.uint8) #array de 0s con tipo de dato int 8 bits (0-255)
        self.state = True

    def __str__(self) -> str:
        return str(self.matrix)

    def load_ordered(self):
        self.matrix = np.arange(81).reshape(9,9)
    def load_special_1(self):
        self.matrix = np.array([[i%9 for i in range(j,9+j)] for j in range(9)])
    def load_random(self,magnitude):
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
    def load_random_from_file(self,file_name):
        file = open(file_name,"r")
        lines = file.readlines() 
        line = lines[np.random.randint(0,len(lines))]
        mat = []
        
        for i in line:
            if i == ".":
                mat.append(0)
            elif "0" <= i <= "9":
                mat.append(int(i))

        self.matrix = np.array(mat).reshape(9,9)


    def verify_game(self):
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

    def delete(self,x,y):
         self.matrix[x][y] = 0

    def __invalid_position(self,x,y):
        for i in range(len(self.immutables[0])):
            if (x,y) == (self.immutables[0][i],self.immutables[1][i]):
                return True
        return False
    
    def play(self,x,y,value):
        if not(self.invalid_position(x,y)):
            self.matrix[x][y] = value
            return "JUGADA VALIDA"
        
        return "JUGADA INVALIDA"

    def is_finished(self):
        return np.count_nonzero(self.matrix) == 0 and self.state
    
juego = Game()

facil = 45
dificil = 17

'''juego.load_random(facil)
print(juego)
while not(juego.is_finished()):
    x = int(input("x:"))
    y = int(input("y:"))
    v = int(input("val:"))

    print(juego.play(x,y,v))
    print(juego)
    print(juego.sta)'''

juego.load_random_from_file("puzzles0_kaggle")
print(juego)



