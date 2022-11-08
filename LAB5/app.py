from utils import process_item

while True:
    x = input("Enter a number:\n")
    if x == "q":
        break
    print(process_item(int(x)))