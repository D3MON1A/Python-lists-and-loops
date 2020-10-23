import random

# def matrixBuilder(i):
#     numb_of_matrix = i
#     # matrix = []
#     matrix = [1] * numb_of_matrix
#     for i in range(numb_of_matrix):
#         matrix[i] = [1] * numb_of_matrix 
        
#     print(matrix)


# matrixBuilder(5)
# import random
# #Create the function below:
# matrix = []
# def matrixBuilder(param):
#   my_list = []
#   for i in range(0, param, 1):
#     my_list.append(random.randint(1,1))
#     for x in range(0, param, 1):
#       matrix.append(my_list)
#   return matrix
# print(matrixBuilder(5)) 
def matrixBuilder(numb):
    new_list =[[1 for i in range(numb)] for x in range (numb)]
    return new_list
print(matrixBuilder(5))
