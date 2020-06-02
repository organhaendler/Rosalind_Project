# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces.
#     Words are case-sensitive, and the lines in the output can be in any order.

def element_count_in_dict(set):
    element_count = {}
    for element in set:
        if element in element_count:
            element_count[element] = element_count[element] + 1
        else:
            element_count[element] = 1
    return element_count

with open("Rosalind_INI6_ExampleData.txt", "r") as fh:
    example_data = fh.readlines()
word_list = example_data[0].split()
word_count = element_count_in_dict(word_list)
for i,j in word_count.items():
    print(i,j)