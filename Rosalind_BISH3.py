# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

example_data = "AAAACCCGGT"
transformation = str.maketrans("ATCG", "TAGC")
complement = example_data.translate(transformation)
rev_comp = complement[::-1]
print(rev_comp)