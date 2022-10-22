import os
import dis

def f(a, /, b=3, *args, c=4, d=5, **kwargs):
    a="x"
    x="xyz"
    print(os.pid())

code = f.__code__
print(code)

# number of arguments
# (not include keyword only arguments, * or ** args)
print(code.co_argcount)

# number of positional only arguments
# args before "/"  
print(code.co_posonlyargcount)

# number of keyword only arguments
# (args after *, not including **args)
print(code.co_kwonlyargcount)

# bytecode
dis.dis(f)

print(f"nlocals: {code.co_nlocals}")

print(f"varnames: {code.co_varnames}")
print(f"co_names: {code.co_names}")
print(f"cellvars: {code.co_cellvars}")
print(f"freevars: {code.co_freevars}")

print(f"consts: {code.co_consts}")