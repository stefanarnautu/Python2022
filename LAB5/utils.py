import math
def process_item(x):
    while True:
        x = x + 1
        ok = 1
        if x > 1:
            for d in range(2,int(math.sqrt(x))+1):
                if x % d == 0:
                    ok = 0

            if ok == 1:
                return x

try:
    x = int(input("Enter the number:\n"))
    print(process_item(x))
except TypeError as e:
    print("Is not integer\n")


