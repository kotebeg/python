def some_funct():
    """will be defined later"""


def square(x):
    return x ** 2


def apply_func(func, *args):
    results = []
    for arg in args:
        results.append(func(arg))    
    
    return results

apply_func(square, 3, 5, 6) # use square as input argument


def cube(x):
    return x ** 3

func_mapping = {'square': square, 'cube': cube}  # store functions in a dict
func_mapping


func_mapping['square']
