from .utilities import compile_and_return_result

def test_and():
    _and = compile_and_return_result("print (1 & 1);")
    assert _and == 1
    not_and = compile_and_return_result("print (1 & 0);")
    assert not_and == 0
    also_not_and = compile_and_return_result("print (0 & 1);")
    assert also_not_and == 0
    definitely_not_and = compile_and_return_result("print (0 & 0);")
    assert definitely_not_and == 0

def test_or():
    _or = compile_and_return_result("print (1 | 0);")
    assert _or == 1
    also_or = compile_and_return_result("print (0 | 1);")
    assert also_or == 1
    both_or = compile_and_return_result("print (1 | 1);")
    assert both_or == 1
    not_or = compile_and_return_result("print (0 | 0);")
    assert not_or == 0

def test_xor():
    xor = compile_and_return_result("print (1 ^ 1);")
    assert xor == 0
    not_xor = compile_and_return_result("print (1 ^ 0);")
    assert not_xor == 1
    also_not_xor = compile_and_return_result("print (0 ^ 1);")
    assert also_not_xor == 1
    definitely_not_xor = compile_and_return_result("print (0 ^ 0);")
    assert definitely_not_xor == 0