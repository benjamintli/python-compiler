import subprocess
import sys
from python_compiler.src.run import compile
import tempfile 
import os


def compile_and_return_result(test_code):
    linker = tempfile.NamedTemporaryFile()
    compile(test_code, linker.name, file=False)
    subprocess.check_output(["llc", "-filetype=obj", linker.name])
    subprocess.check_output(["gcc", "-no-pie", linker.name + ".o", "-o", "test"])
    proc = subprocess.Popen(["./test"], stdout=subprocess.PIPE)
    stdout_value = proc.communicate()[0]
    exe_result_as_int = int(stdout_value.decode().rstrip())
    subprocess.check_output(["rm", "test"])
    return exe_result_as_int
