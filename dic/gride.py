from pickle import FALSE

from magintes import magnites
import numpy as np
from colorama import init, Fore, Back, Style
from solve import solve


class gride(magnites):
    ##, solve):
    def __init__(self, size1,size2, pos_of_magnites, pos_of_stones,fin_pos_magnets, fin_pos_stones ): ##, pos_of_empty## ):
        super().__init__(pos_of_magnites, pos_of_stones )##, pos_of_empty)
        ##super().__init__(fin_pos_magnets, fin_pos_stones )
        self.fin_pos_stones  =fin_pos_stones
        self.fin_pos_magnets = fin_pos_magnets
        self.size1= size1
        self.size2= size2

    # def color_char_ansi(char, color_code):
    #     return f"\033[{color_code}m{char}\033[0m"

    def make_gride(self):
        matrix = np.full((self.size1, self.size2), '•')
        for i in range(len(self.pos_of_stones)):
            j = self.pos_of_stones[i][0]
            k = self.pos_of_stones[i][1]
            matrix[j][k] = "♦"
        for i in range(len(self.pos_of_magnites)):
            j = self.pos_of_magnites[i][0]
            k = self.pos_of_magnites[i][1]
            matrix[j][k] = '+'
        return matrix
        # for i in range(len(self.pos_of_empty)):
        #     j = self.pos_of_empty[i][0]
        #     k = self.pos_of_empty[i][1]
        #     matrix[j][k] = "○"


    def print_gride(self,gride):
        ##print the gride line by line
            for row in gride:
                print(" ".join(row))
    print('\n')
    print("____________________")
    print('\n')

    def is_valid(self ,matrix ,  row , col ):
        ## chaking if the place is empty so I can move
          if matrix[row][col] != '•':
              return False
        ## see if the adj cells is magntes
          for i in range (max(0,row-1), min(self.size1,row+2)):
              for j in range(max(0,col-1), min(self.size2, col+2)):
                  if matrix [i][j] == '+' or matrix[i][j] == '-':
                      return False
          return True



    def find_element (self ,matrix , element):
        ## it use for finding the current pos of magnets
        dp = []
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == element:
                    dp.append(i)
                    dp.append(j)
                    return dp
        return None




    def cheak_stones_pos (self ,dp ):
        ## cheak and moveing sotnes if there a colse magnet
        ##dp = self.find_element( matrix , '+')
        for i in self.pos_of_stones:
            if dp[0] == i[0] and i[0] > dp[0] and i[0] < self.size1-1 :
                i[0] +=1
            if dp[0] == i[0] and i[0] < dp[0] and i[0] > 0 :
                i[0] -=1
            if dp[1] == i[1] and i[1] > dp[1] and i[1] < self.size1-2 :
                i[1] +=1
            if dp[1] == i[0] and i[1] < dp[0] and i[1] > 0 :
                i[1] -=1
            return self.pos_of_stones

    def cheak_dp (self , pos ,dp):
        ## cheak if the current pos in dp
        for i in dp :
            if pos [0] == i[0] and pos[1] == i[1]:
                return False
        return True


    def solve_rec (self  ,row ,col, dp):
        ##moving on gride withe rec
        if [row,col]==self.fin_pos_stones and self.pos_of_magnites == self.fin_pos_magnets :
            return True
        else:
            matrix = []
            matrix.append(row)
            matrix.append(col)
            dp.append(matrix)
            if row < self.size1-1 and col < self.size2-1 and self.cheak_dp([row+1 , col+1] ,dp ) :
                self.solve_rec(self , row+1 , col+1 ,dp )
                a = self.cheak_stones_pos([row+1 , col+1])
                b = gride(self.size1,self.size2 ,[row+1,col+1] ,a , self.fin_pos_magnets,self.fin_pos_stones)
                self.print_gride(b)

            if row < self.size1-1 and col == self.size2-1 and self.cheak_dp([row+1 , col] ,dp ):
                self.solve_rec(self , row +1 , col ,dp )
                a = self.cheak_stones_pos([row + 1, col ])
                b = gride(self.size1, self.size2, [row + 1, col ], a, self.fin_pos_magnets, self.fin_pos_stones)
                self.print_gride(b)

            if row == self.size1 - 1 and col < self.size2 - 1 and self.cheak_dp([row , col+1] ,dp ):
                self.solve_rec(self , row  , col +1,dp )
                a = self.cheak_stones_pos([row , col + 1])
                b = gride(self.size1, self.size2, [row , col + 1], a, self.fin_pos_magnets, self.fin_pos_stones)
                self.print_gride(b)

            else:
                return "there no way to solve"


            # i = row
            # j = col
            # i1 = row+1
            # i2 = row-1
            # j1 = col+1
            # j2 = col-1

            # if row == 0  and col == 0  and self.cheak_dp and ([i1 ,j] , dp) :
            #     self.pos_of_magnites [0] +=1
            #     self.pos_of_magnites [1] += 1
            #     self.solve_rec(matrix , i1 , j1)
            #     self.pos_of_magnites[0] += 1
            #     self.solve_rec(matrix, i1, j).
            #     self.pos_of_magnites[1] += 1
            #     self.solve_rec(matrix, i, j1)
            # if row == 0 and col == self.size2-1  and self.cheak_dp and ([i1, j], dp):
            #     self.pos_of_magnites[0] += 1
            #     self.pos_of_magnites[1] -= 1
            #     self.solve_rec(matrix, i1, j2)
            #     self.pos_of_magnites[1] -= 1
            #     self.solve_rec(matrix, i, j2)
            # if row < self.size1 - 1 and col == self.size2 - 1 and self.cheak_dp([i1, j], dp):
            #     self.pos_of_magnites[0] += 1
            #     self.solve_rec(matrix, i1, j)
            #     self.pos_of_magnites[1] =-1
            #     self.solve_rec(matrix,i1,j2)
            # if row == self.size1 - 1 and col < self.size2 - 1 and self.cheak_dp([i1, j], dp):
            #     self.pos_of_magnites[1] += 1
            #     self.solve_rec(matrix, i, j1)
            #     self.pos_of_magnites[0] =-1
            #     self.solve_rec(matrix , i2, j1)
            # if row == self.size1 - 1 and col == self.size2 - 1 and self.cheak_dp([i1, j], dp):
            #     self.pos_of_magnites[0] -= 1
            #     self.pos_of_magnites[1] -= 1
            #     self.solve_rec(matrix, i2, j2)



    def start_play(self):
        matrix = self.make_gride()
        dp = self.find_element( matrix , '+')
        self.solve_rec(0 ,0 ,dp)







