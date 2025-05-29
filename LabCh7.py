from functools import reduce


def square(x):
    return x * x
def get_even(n):
    return n % 2 == 0
def add(x,y):
    return x+y

def higher_order():
    try:
        my_list = map(int, input("enter a list of numbers seperated by spaces: ").split())
        square_list = list(map(square, my_list))
        filtered_list = list(filter(get_even, square_list))
        if filtered_list:
            product_of_list = reduce(add, filtered_list)
            print("The sum of the even squares is:", product_of_list)
        else:
            print("No even squares found.")
            main()
    except ValueError:
        print("Invalid entry.")
        main()



def main():
    higher_order()

if __name__ == "__main__":
    main()

