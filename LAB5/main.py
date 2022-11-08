print("ex2---------------------------------------")
my_anonymous_function = lambda *args, **kwargs: sum(kwargs.values())
def my_function(*args, **kwargs):
    return sum(kwargs.values())

print(my_anonymous_function(1, 2, c=3, d=4))
print(my_function(1, 2, c=3, d=4))

print("\nex3-------------------------------------")

def ex3_function(s):
    rez = list()
    s = s.lower()
    vowel = ['a','e','i','o','u']
    for c in s:
        if c in vowel:
            rez.append(c)
    return rez

ex3_anonymous = lambda s: [c for c in s if c in "aeiouAEIOU"]

def ex3_filter(s):
   return list(filter(lambda c: c in "aeiou", s))


print(ex3_function("Programming in Python is fun"))
print(ex3_anonymous("Programming in Python is fun"))
print([c for c in "Programming in Python is fun".lower() if c in "aeiou"])
print(ex3_filter("Programming in Python is fun"))

print("\nex4-------------------------------------")

def ex4(*args,**kwargs):
    rez = list()
    for l in args:
        if type(l) == dict and len(l)>=2 and len([key for key in l.keys() if type(key)==str if len(key)>=3])>0:
            rez.append(l)
    for key,value in kwargs.items():
        if type(value) == dict and len(value)>=2 and len([key for key in value.keys() if type(key)==str if len(key)>=3])>0:
            rez.append(value)
    return rez
print(ex4({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3],{'abc': 4, 'def': 5},3764,dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},test={1: 1, 'test': True}))

print("\nex5-------------------------------------")

def ex5(l):
    return [el for el in l if type(el) == int or type(el) == float]

print(ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

print("\nex6-------------------------------------")

def ex6(l):
    odd = list()
    even = list()
    for el in l:
        if el%2 == 0:
            even.append(el)
        else: odd.append(el)
    return list(zip(even,odd))

print(ex6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

print("\nex7-------------------------------------")

def sum_digits(x):
    return sum(map(int, str(x)))

def process(**kwargs):
    fib = [0,1]
    for i in range(2,100):
        fib.append(fib[i-1]+fib[i-2])

    if "filters" in kwargs.keys():
        for filtru in kwargs["filters"]:
            fib = list(filter(filtru,fib))

    if kwargs.keys().__contains__("offset"):
        fib = fib[kwargs["offset"]:]

    if kwargs.keys().__contains__("limit"):
        fib = fib[:kwargs["limit"]]
    return fib
print(process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],limit=2,offset=2))

print("\nex8-a)----------------------------------")

def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

def default_return(*args,**kwargs):
    return

def print_arguments(function):
    function_string = """
def new_function(*args, **kwargs):
        print("Arguments are:(",end=" ")
        for x in args:
            print(x,",",end=" ") 
        print("),{",end=" ")    
        for x in kwargs:
            print(x,",",end=" ")
        print("}")
        return functia_aleasa(*args,**kwargs)"""
    globals()["functia_aleasa"] = function
    exec(function_string,globals())
    return new_function

augmented_multiply_by_two = print_arguments(multiply_by_two)
print(augmented_multiply_by_two(10))

augmented_add_numbers = print_arguments(add_numbers)
print(augmented_add_numbers(3, 4))

print("\nex8-b)----------------------------------")

def multiply_by_three(x):
    return x * 3

def default_return_multiply(x):
    return x

def multiply_output(function):
    function_string = """
def new_function(*args, **kwargs):
        return 2 * functia_aleasa(*args,**kwargs)"""
    globals()["functia_aleasa"] = function
    exec(function_string,globals())
    return new_function

augmented_multiply_by_three = multiply_output(multiply_by_three)
print(augmented_multiply_by_three(10))

print("\nex8-c)----------------------------------")

def add_numbers(a, b):
    return a + b

def augment_function(function,decorators):
    function_string = """
def new_function(*args, **kwargs):
        rez = functia_aleasa(*args,**kwargs)
        for decorator in dec:
            if "print_arguments" in str(decorator):
                x = decorator(default_return)
                x(*args,**kwargs)
            if "multiply_output" in str(decorator):
                x = decorator(default_return_multiply)
                rez = x(rez)     
        return rez
        """
    globals()["functia_aleasa"] = function
    globals()["dec"] = decorators
    exec(function_string,globals())
    return new_function

decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
print(decorated_function(3, 4))


print("\nex9-------------------------------------")

def ex9(**kwargs):
    '''rez = list()
    l = kwargs.get("pairs")
    print(l)
    for el in l:
        a = dict()
        a["sum"] = el[0]+el[1]
        a["prod"] = el[0]*el[1]
        a["pow"] = pow(el[0],el[1])
        rez.append(a)
    return rez'''
    return [{"sum":el[0]+el[1],"prod":el[0]*el[1],"pow":pow(el[0],el[1])} for el in kwargs.get("pairs")]

print(ex9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)]))









