a = 33
class A(Exception):
    pass
class B(Exception):
    pass
try:
    if a == 1:
        raise A 
    else:
        raise B 
except A:
    print(1)
except B:
    print(2)