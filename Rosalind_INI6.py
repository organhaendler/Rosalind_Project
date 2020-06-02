# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces.
#     Words are case-sensitive, and the lines in the output can be in any order.

with open("Rosalind_INI6_ExampleData.txt", "r") as fh:
    example_data = fh.readlines()

words_in_example_data = example_data[0].split()
word_count = {}

for i in words_in_example_data:
    if i in word_count:
        word_count[i] = word_count[i] + 1
    else:
        word_count[i] = 1

print(word_count)