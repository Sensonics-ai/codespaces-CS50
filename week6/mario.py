from cs50 import get_int

def main():
    height = get_int("Height: ")
    for i in range(height):
        print("#")


def get_height():
    while True:
     try:                                    # try to get an integer from the user
        n = int(input("Height: "))          # if successful, return the integer
        if n >= 1 and n <= 8:               # if the integer is between 1 and 8, inclusive
            return n                        # return the integer
        except ValueError:               # if the user did not input an integer
            print("Invalid input")          # print an error message

main()
