#my_list = [10, 0, -12, 45, 23, 15, -78, 6]
my_list = [3,1,7,6]

def maximum(input_list):
    max_no = 0

    for number in input_list:
        if number > max_no:
            max_no = number

    return max_no
   


def sort_list(my_list):

    for i in range(len(my_list)): 

        for j in range(i + 1, len(my_list)): 
    
            if my_list[i] > my_list[j]: 
                    temp = my_list[i]
                    my_list[i] = my_list[j]
                    my_list[j] = temp

            print(my_list)


sort_list(my_list)  
print ("sorted result: ", my_list)

result = maximum(my_list)  
print("Maximum No: ", result)

