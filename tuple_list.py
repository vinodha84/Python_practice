
numbers = [1,2,3,4,5,67,8]

converted_list = []

def convert_list(number):

    for x in (numbers):
        converted_list.append(str(x))

    converted_tuple = tuple(converted_list)
    return converted_tuple

converted_tuple = convert_list(numbers)
print('Original List', numbers)

print(converted_list)
print(converted_tuple)