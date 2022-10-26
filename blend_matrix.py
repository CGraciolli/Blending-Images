from typing import List, Set, Tuple

def average(nums:List[int]) -> int:
    """
    recives a non-empty list of integers,
    returns the average
    """
    return sum(nums)/len(nums)

def get_neighbors_indexes(matrix:List[List[int]], index_row:int, index_column:int) -> Set[Tuple[int]]:
    """
    recives a matrix with numerical values and two integers representing a position in the matrix
    returns a set of the element's neighbors' positions (represented as tuples)
    the element itself is also considered a neighbor
    """
    neighborhood = {(index_row, index_column)} ##the element itself
    if index_column > 0:
        neighborhood.add((index_row, index_column - 1)) ##neighbor to the left
    if index_column < len(matrix[0]) - 1:
        neighborhood.add((index_row, index_column + 1)) ##neighbor to the right
    if index_row > 0:
        neighborhood.add((index_row - 1, index_column)) ##neighbor above
    if index_row < len(matrix) - 1:
        neighborhood.add((index_row + 1, index_column)) ##neighbor below
    return neighborhood


def get_value_from_indexes(matrix:List[List[int]], index_row:int, index_column:int) -> int:
    """
    recives a matrix and two integers representing a position in the matrix
    returns the element of the matrix occupying that position
    """
    return matrix[index_row][index_column]

def get_neighbors(matrix:List[List[int]], index_row:int, index_column:int) -> List[int]:
    """
    recives a matrix with numerical values and two integers representing a position in the matrix
    returns a list of the element's neighbors (the element is also included in the list)
    """
    neighborhood_indexes = get_neighbors_indexes(matrix, index_row, index_column)
    neighborhood = list(map(lambda x: get_value_from_indexes(matrix, x[0], x[1]), neighborhood_indexes))
    return neighborhood

def process_element(matrix:List[List[int]], index_row:int, index_column:int) -> int:
    """
    recives a matrix with numerical values and two integers representing a position in the matrix
    returns the average between that element and its neighbors
    """
    neighbors = get_neighbors(matrix, index_row, index_column)
    print(neighbors)
    return average(neighbors)

def process_matrix(matrix:List[List[int]]) -> List[List[int]]:
    """
    recives a matrix with numerical values
    returns another matrix
    the elements in the new matrix are the average between 
    the element of the same position in the old matrix and its neighbors
    """
    new_matrix = []
    for row_index in range(len(matrix)):
        new_row = []
        for column_index in range(len(matrix[0])):
            new_element = process_element(matrix, row_index, column_index)
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix

