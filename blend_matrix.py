from typing import List

def process_matrix(matrix:List[List[int]]) -> List[List[int]]:
    """
    recives a matrix with numerical values
    returns another matrix
    the elements in the new matrix are the average between 
    the element of the same position in the old matrix and its neighbors
    """
    new_matrix = []
    for row_index, row in enumerate(matrix):
        new_row = []
        for column_index, element in enumerate(row):
            list_neighbors = [element]
            if column_index > 0:
                list_neighbors.append(row[column_index - 1]) ##neighbor to the left
            if column_index < len(row) - 1:
                list_neighbors.append(row[column_index + 1]) ##neighbor to the right
            if row_index > 0:
                list_neighbors.append(matrix[row_index - 1][column_index]) ##neighbor above
            if row_index < len(matrix) - 1:
                 list_neighbors.append(matrix[row_index + 1][column_index]) ##neighbor below
            new_element = sum(list_neighbors)/len(list_neighbors)
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix

