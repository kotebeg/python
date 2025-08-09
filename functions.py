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



#  Returning Functions
def get_func(func_name):
    func_mapping = {'square': square, 'cube': cube}
    return func_mapping.get(func_name, None)  # return function


my_func = get_func('cube')
my_func(7)



#  Arguments Provided by Position

def sub_number(minuend, subtrahend):
  print(f"{minuend}-{subtrahend}={minuend - subtrahend}")

sub_number(3, 1) # 3 assigned to minuend, 1 – subtrahend, 


sub_number(1, 3) # 1 assigned to minuend, 3 – subtrahend



# Arguments Provided by Name
def sub_number(minuend, subtrahend):
  print(f"{minuend}-{subtrahend}={minuend - subtrahend}")


sub_number(minuend=3, subtrahend=1) # 3 assigned to minuend, 1 – subtrahend


sub_number(subtrahend=1, minuend=3) # the same herA


def show_arguments(*args, **kwargs):
  print(f"args: {args}; kwargs: {kwargs}")


show_arguments(1, 'name', arg1=[1, 2, 3], arg2='value')

#args: (1, 'name'); kwargs: {'arg1': [1, 2, 3], 'arg2': 'value'}


def show_arguments(*args, **kwargs):
  print(args[1:-1])
  print(kwargs['name'])

show_arguments(1, 'name', 'value', 10, name='arg1', arg2='Tom')

('name', 'value')
arg1