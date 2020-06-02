# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the
#     symbols 'A', 'C', 'G', and 'T' occur in s.

def element_count_in_dict(set):
    element_count = {}
    for element in set:
        if element in element_count:
            element_count[element] = element_count[element] + 1
        else:
            element_count[element] = 1
    return element_count

def main():
    sample_data = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    base_count = element_count_in_dict(sample_data)
    for x,y in base_count.items():
        print(x,y)

if __name__ == 'main':
    main()