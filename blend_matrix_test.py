import pytest
from blend_matrix import process_matrix, process_matrix_dic

def test_empty():
    assert process_matrix([[]]) == [[]]

def test_process_matrix():
    m1 = [[3, 0], [0, 3]]
    zeroes = [[0, 0, 0], [0, 0, 0]]
    one_row = [[1, 2, 3]]
    one_column = [[1], [-1], [10]]
    
    assert process_matrix(m1) == [[1, 2], [2, 1]]
    assert process_matrix(zeroes) == zeroes
    assert process_matrix(one_row) == [[1.5, 2, 2.5]]
    assert process_matrix(one_column) == [[0], [10/3], [4.5]]

def test_empty_dic():
    assert process_matrix_dic([[]]) == [[]]

def test_process_matrix_dic():
    m1 = [[3, 0], [0, 3]]
    zeroes = [[0, 0, 0], [0, 0, 0]]
    one_row = [[1, 2, 3]]
    one_column = [[1], [-1], [10]]
    
    assert process_matrix_dic(m1) == [[1, 2], [2, 1]]
    assert process_matrix_dic(zeroes) == zeroes
    assert process_matrix_dic(one_row) == [[1.5, 2, 2.5]]
    assert process_matrix_dic(one_column) == [[0], [10/3], [4.5]]