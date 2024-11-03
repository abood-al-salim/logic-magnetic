from tree import tree
from shaps import shaps
import numpy as np
from helper import helper


class gride(helper,shaps , tree ) :

    ## contructer
    def __init__(self , size1 , size2 , pos_pos , pos_neg , pos_sto):
        super().__init__(pos_pos ,pos_neg,pos_sto)
        self.size1 = size1
        self.size2 = size2


        ## create an initial gride
    def make_gride (self):
        matrix = np.full((self.size1, self.size2), '•')
        for i in range(len(self.pos_sto)):
            j = self.pos_sto[i][0]
            k = self.pos_sto[i][1]
            matrix[j][k] = "♦"
        for i in range(len(self.pos_pos)):
            j = self.pos_pos[i][0]
            k = self.pos_pos[i][1]
            matrix[j][k] = '+'
            for i in range(len(self.pos_neg)):
                j = self.pos_neg[i][0]
                k = self.pos_neg[i][1]
                matrix[j][k] = '-'
        return matrix


    ## print the gride
    def print_gride(self , gride ):
        for row in gride:
            print(" ".join(row))
        print('\n')
        print("____________________")
        print('\n')
    def create_space(self , gride , ini_pos , dp , tree):
        if ini_pos in dp :
            return False
        gride1 = gride(self.size1 , self.size2 , ini_pos ,self.pos_neg , self.pos_sto)
        helper1 = helper()
        if helper1.is_valid(gride1,ini_pos) :
        tree.
