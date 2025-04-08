def get_last_element(numbered_list):
    return numbered_list[len(numbered_list) - 1]


def get_greater_element(numbered_list):
    greater_element = 0
    for element in numbered_list:
        if element > greater_element:
            greater_element = element
    return greater_element


def generate_list_of_even_numbers(numbered_list):
    even_list = []
    for element in numbered_list:
        if element % 2 == 0 and element != 0:
            even_list.append(element)
        even_list.sort()
    return even_list


def element_is_present(numbered_list, source):
    for element in numbered_list:
        if element == source:
            return True
    return False


def get_mean_of_elements(numbered_list):
    return float(sum(numbered_list) / len(numbered_list))


def get_elements_greater_than_mean(numbered_list, mean):
    elements_greater_than_mean = []
    for element in numbered_list:
        if element > mean:
            elements_greater_than_mean.append(element)
    elements_greater_than_mean.sort()
    return elements_greater_than_mean


def list_is_growing(numbered_list):
    last_element = numbered_list[0]
    for element in numbered_list:
        if last_element > element:
            return False
    return True


my_list = [1, 2, 3, 4, 5, 6, 7, 9, 8, 0]
number_to_search = 6
mean_of_list = get_mean_of_elements(my_list)

print(f'Last element: {get_last_element(my_list)}')
print(f'Greater element: {get_greater_element(my_list)}')
print(f'List of even numbers: {generate_list_of_even_numbers(my_list)}')
print(f'{number_to_search} is present? {element_is_present(my_list, number_to_search)}')
print(f'Mean of elements: {mean_of_list:.2f}')
print(f'Elements greater than mean: {get_elements_greater_than_mean(my_list, mean_of_list)}')
print(f'List is growing? {list_is_growing(my_list)}')
