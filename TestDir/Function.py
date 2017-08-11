list_of_numbers= [1,2,3,4]
def get_median(list_of_numbers):
    list_of_numbers.sort()
    if len(list_of_numbers) % 2 ==1:
        middle = list_of_numbers[len(list_of_numbers)//2]
    else:
        middle = (list_of_numbers[len(list_of_numbers) // 2] + list_of_numbers[len(list_of_numbers) // 2-1 ]) /2

    return middle
print"woalahhh"
print(get_median(list_of_numbers))