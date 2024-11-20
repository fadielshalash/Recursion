def find_subsets(my_list):
    if not my_list:
        return [[]]
    first_subset = find_subsets(my_list[1:])
    second_subset = [sub_set + [my_list[0]] for sub_set in first_subset]
    return first_subset + second_subset
list_numbers = input("Enter numbers for your list(dont forget the space): ")
user_input_list = list(map(int, list_numbers.split()))
result = find_subsets(user_input_list)
print(result)


