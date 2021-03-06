# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file.
#     Assume 1-based numbering of lines.

def isolate_even_lines(example_data):
    even_lines_only = []
    line_numbers = int()
    for i in example_data:
        line_numbers = line_numbers + 1
        if not line_numbers%2:
            even_lines_only.append(i)
    return even_lines_only

def main():
    with open("Rosalind_INI5_ExampleData.txt", "r") as fh:
        example_data = fh.readlines()
    even_lines_only = isolate_even_lines(example_data)
    with open("Rosalind_INI5_Results.txt", "w") as fh:
        for i in even_lines_only:
         fh.write(i)

if __name__ == '__main__':
    main()