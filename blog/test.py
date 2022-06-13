def add(x):
    return x+1

def sub(x):
    return x-1

funcs=[add, sub]

for func in funcs:
    print(func(10))
