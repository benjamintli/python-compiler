from .utilities import compile_and_return_result

def test_equals():
    equivalent = compile_and_return_result("print(1 == 1);")
    assert equivalent == 1
    not_equivalent = compile_and_return_result("print(1 == 0);")
    assert not_equivalent == 0

def test_not_equals():
    not_equals = compile_and_return_result("print (1 != 0);")
    assert not_equals == 1
    equals = compile_and_return_result("print(1 != 1);")
    assert equals == 0

def test_greater_than():
    greater_than = compile_and_return_result("print (10 > 0);")
    assert greater_than == 1
    greater_than_equal = compile_and_return_result("print (10 >= 0);")
    assert greater_than_equal == 1

def test_not_greater_than():
    not_greater_than = compile_and_return_result("print (0 > 10);")
    assert not_greater_than == 0
    not_greater_than_equal = compile_and_return_result("print (0 >= 10);")
    assert not_greater_than_equal == 0

def test_less_than():
    less_than = compile_and_return_result("print (0 < 10);")
    assert less_than == 1
    less_than_equal = compile_and_return_result("print (0 <= 10);")
    assert less_than_equal == 1

def test_not_less_than():
    not_less_than = compile_and_return_result("print (0 < 0);")
    assert not_less_than == 0
    not_less_than_equal = compile_and_return_result("print (10 <= 0);")
    assert not_less_than_equal == 0

