from so_calc.operation import add, add_numpy

def test_add():
    x = 2
    y = 4
    assert add(x,y) == 6

def test_add_negative():
    x = 4
    y = -4
    assert add(x,y) == 0

def test_add_numpy():
    num_list = [3,3,3]
    assert add_numpy(num_list) == 9

