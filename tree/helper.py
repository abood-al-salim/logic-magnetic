from tree.gride import gride


class helper :
    def __init__(self):
        pass
    def get_index (self , gride , value):
        for i, row in enumerate(gride):
            for j, element in enumerate(row):
                if element  == value:
                    return [i, j]
        return None



    ## cheack if there stone in the same row
    def cheak_row_pos (self , gride  , curr_index ):
          for i in gride[curr_index]:
             if i == '♦'  :
                 return True
          else:
                return False
        # mat_of_index_big = []
        # mat_of_index_samll = []
        # for row in gride:
        #     for i, item in enumerate(row):
        #         if item == '♦' and item > curr_index :
        #             mat_of_index_big.append(item)
        #         if item == '♦' and item > curr_index :
        #             mat_of_index_samll.append(item)
        # for index in mat_of_index_big:
        #     if index < len(row) - 1:  # Ensure the index is not the last one
        #         element = row.pop(index)  # Remove the element from the current index
        #         row.insert(index + 1, element)  # Insert the element at the next index
        #         row[index] = '•' # Replace the old position with the '.'
        # for index in mat_of_index_samll:
        #     if index < len(row) - 1:  # Ensure the index is not the last one
        #         element = row.pop(index)  # Remove the element from the current index
        #         row.insert(index + 1, element)  # Insert the element at the next index
        #         row[index] = '•' # Replace the old position with the '.'
        # return gride



    ##cheking if there stonse in the same col
    def cheak_col_pos ( self ,gride , curr_index ):
        i = 0
        while( i < len(gride) ):
            if gride [i][curr_index] == '♦':
                return True
            else:
                i +=1
        return False


    ## checking if valid to move magnets
    def is_valid(self ,gride , cur_index  ):
        ## chaking if the place is empty so I can move
          if gride[cur_index[0]][cur_index[1]] != '•':
              return False
        ## see if the adj cells is magntes
          for i in range (max(0,cur_index[0]-1), min(len(gride),cur_index[0]+2)):
              for j in range(max(0,cur_index[1]-1), min(len(gride[0]),cur_index[1]+2)):
                  if gride [i][j] == '+' or gride[i][j] == '-':
                      return False
          return True


