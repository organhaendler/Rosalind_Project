# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

def main():
    example_data = "GAAAAGGATCTGTCATTCCGAGGGTGTAGGGCTCTCATTTATTACTCAGGTTGATTCAACACGTATATACAAGTGGCGC" \
                   "TCATCCGAGTCCGAGGTATAAAGGCCTGACTAATAAGCTGTGAATTATATTATAGGGAGTAGTTAAACAAAGGCACGAG" \
                   "TTGTGGTCACTATCGTGTAGTAGTAGAGCCCGACCCCCCGGCTAAGAAGTTCGGTTCTATGCAATTAAGGTTGAGCAGA" \
                   "CCTGGCATGTCCAAGCAGGGGATAATGCCGACCGATAATGATTCCCTCATGTATTCAGTCCCTTAACCGGAAGTTCTCT" \
                   "GCCAGGCTACAGGGAGGTTCCGGGCTATATCGCTTGGGTAATCGGGCAGCAACTAGGTACCCTGCCTGAAGTTGTTGTT" \
                   "GCGGTTATACCACTGAATTCTGTACTCTTACGGTGTGCTCATAGTAGGGGCGTGAATGCGCATGTGATCTACGGTGTCG" \
                   "AGCGTTTTAGGTAGTCTTTGGGGAGCTTTGGTTCGCACGTGAAGCAGGCGCCATCAAACACTCCCATTCCGGTGTTCAC" \
                   "CCGTTGGGATAAATCTGTGCTGCGGGCCCTGTCGATCAGCTGAGAATTGTAGGCCAGTCATGGGCCCTAGACGGTTGTG" \
                   "AGACGCACCTTACCTGGAATCTGGGTGGTCGTGGTGTCTTACGCTTTTATTCTCACACGAGTAGGGTACGCACGGTGAG" \
                   "CTCGTTGGGCCGCAGCAATGAGTGCGTGGGCAAACAAGGGTTCCGAGAACCATGTCCCGCAGCAGCGGTTAATCTCTGC" \
                   "GCTTGACTGACCCTGTTAGACAGCTGCCGGGTACATGCGGGAGACTCACCCCGACGGTTCGAAACCTGGAGTTCGAACA" \
                   "ATACTTAGCCGGTAATATCCCAAAGCCTCTGTGCGCGCTCGAACTATAAAAGCACCGGTGACTGCTAGACG"
    transformation = str.maketrans("ATCG", "TAGC")
    complement = example_data.translate(transformation)
    rev_comp = complement[::-1]
    print(rev_comp)

if __name__ == '__main__':
        main()