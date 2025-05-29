def towers_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    towers_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    towers_of_hanoi(n-1, auxiliary, source, target)

towers_of_hanoi(3, 'A', 'B', 'C')


#work from LabCh7
def square_numbers(my_list):
    numbers = map(int, my_list)
    square_numbers = map(square, numbers)
    squared_list = list(square_numbers)
    filter_even(squared_list)


def filter_even(squared_list):
    filtered_list = list(filter(get_even, squared_list))

    product_of_list(filtered_list)

def product_of_list(filtered_list):
    list_product = reduce(add, filtered_list)
    print(list_product)

def get_list():
    my_list = input("enter a list of numbers: ")
    my_list = my_list.split()

    higher_order(my_list)