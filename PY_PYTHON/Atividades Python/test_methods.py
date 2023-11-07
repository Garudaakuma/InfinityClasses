def rand_num(*arg:int):
    soma = 0
    arg_arry = list(arg)
    if len(arg) != 1:
        for i in range(len(arg_arry)):
            print(arg_arry[i])
            soma+=arg_arry[i]
    else:
        soma = arg_arry[0]
    return [soma,arg_arry,arg]
    

import random as rnd
print( rand_num( rnd.randint(2,10),rnd.randint(2,10),rnd.randint(2,10) ) )