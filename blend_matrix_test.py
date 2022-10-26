import pytest
from blend_matrix import process_matrix, average, get_neighbors_indexes, get_value_from_indexes, process_element

def test_average():
    l1 = [0, 0, 0]
    l2 = [-4]
    l3 = [0.5, -0.5, 3]

    assert average(l1) == 0
    assert average(l2) == -4
    assert average(l3) == 1

def test_get_neighbors_indexes():
    m1 = [[3, 0, 1], [0, 3, 1]]
    one_number = [[2]]

    assert get_neighbors_indexes(m1, 0, 0) == {(0, 0), (0, 1), (1, 0)}
    assert get_neighbors_indexes(m1, 1, 0) == {(0, 0), (1, 0), (1, 1)}
    assert get_neighbors_indexes(m1, 0, 1) == {(0, 1), (0, 0), (0, 2), (1, 1)}
    assert get_neighbors_indexes(one_number, 0, 0) == {(0, 0)}

def test_get_value_from_indexes():
    m1 = [[3, 0, 1], [0, 6, -9]]

    assert get_value_from_indexes(m1, 0, 0) == 3
    assert get_value_from_indexes(m1, 0, 2) == 1
    assert get_value_from_indexes(m1, 1, 2) == -9

def test_process_element():
    m1 = [[3, 0], [0, 3]]

    assert process_element(m1, 0, 0) == 1

def test_process_matrix():
    m1 = [[3, 0], [0, 3]]
    zeroes = [[0, 0, 0], [0, 0, 0]]
    m2 = [[1, 4], [-3, -9], [0, -13]]
    one_row = [[1, 2, 3]]
    one_column = [[1], [-1], [10]]
    one_number = [[4]]
    empty = [[]]
    
    assert process_matrix(m1) == [[1, 2], [2, 1]]
    assert process_matrix(zeroes) == zeroes
    assert process_matrix(one_row) == [[1.5, 2, 2.5]]
    assert process_matrix(one_column) == [[0], [10/3], [4.5]]
    assert process_matrix(m2) == [[2/3, -4/3], [-11/4, -21/4], [-16/3, -22/3]]
    assert process_matrix(one_number) == one_number
    assert process_matrix(empty) == empty

