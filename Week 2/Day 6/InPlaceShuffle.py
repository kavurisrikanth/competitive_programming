import random

def shuffle(the_list):
    # Shuffle the input in place

    for index in range(len(the_list)):
        to_index = random.randint(0, len(the_list) - 1)
        the_list[index], the_list[to_index] = the_list[to_index], the_list[index]


sample_list = [1, 2, 3, 4, 5]
print(
'Sample list:', sample_list)



print (
'Shuffling sample list...')
shuffle(sample_list)
print(
sample_list)