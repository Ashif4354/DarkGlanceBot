import random

def func_test_1(a):
    print("This is func_test_1.",a)

def func_test_2(a):
    print("This is func_test_2.",a)

def func_test_3(a):
    print("This is func_test_3.",a)

my_list = [func_test_1, func_test_2, func_test_3]

random.choice(my_list)(4)