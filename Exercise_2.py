#first way
def arg_func(*args):
    '''
    The method returns second ascending value from the args with considering of repeatable values
    '''
    new_list = []
    for arg in args:
        if arg not in new_list:
            new_list.append(arg)
    new_list.sort()
    return new_list[1]

args = [2,2,2,2,199,2,4,87,45,100,1000]

print(arg_func(*args))

#second way
def arg_func2(*args2):
    '''
    The method returns second ascending value from the args with considering of repeatable values
    '''
    new_list1 = list(set(args2))
    new_list1.sort()
    return new_list1[1]

args2 = [2,2,2,2,199,2,4,87,45,100,1000]

print(arg_func2(*args2))
