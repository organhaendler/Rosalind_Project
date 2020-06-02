# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the
#     symbols 'A', 'C', 'G', and 'T' occur in s.

sample_data = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
A = int()
G = int()
C = int()
T = int()

for i in sample_data:
    if i == "A":
        A += 1
    elif i == "G":
        G += 1
    elif i == "C":
        C += 1
    elif i == "T":
        T += 1

print(A, T, G, C)
# Could have used dictionary like in INI6. Rework when there is time.