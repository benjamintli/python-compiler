from .utilities import compile_and_return_result

def test_addition():
    add = compile_and_return_result("print (1 + 1);")
    assert add == 2

def test_subtract():
    sub = compile_and_return_result("print (1 - 1);")
    assert sub == 0

def test_multiply():
    mult = compile_and_return_result("print (10 * 12);")
    assert mult == 120

def test_divide():
    div = compile_and_return_result("print (100 / 10);")
    assert div == 10

def test_modulo():
    mod = compile_and_return_result("print (10 % 10);")
    assert mod == 0
    mod_club = compile_and_return_result("print (10 % 9);")
    assert mod_club == 1