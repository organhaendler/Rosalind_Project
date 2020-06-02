# Given: A string s of length at most 200 letters and four integers a, b, c and d
# Return: The slice of this string from indices a through b and c through d (with space in between),
#     inclusively. In other words, we should include elements s[b] and s[d] in our slice.
# Sample Dataset: Rosalind_INI2.2_ExampleData.txt
# Testchange

with open("Rosalind_INI3_ExampleData.txt") as fh:
    example_data = fh.readlines()

example_string = example_data[0]
example_values = example_data[1].split()
solutions = [example_string[int(example_values[0]):int(example_values[1])+1],
            example_string[int(example_values[2]):int(example_values[3])+1]]

print(solutions)