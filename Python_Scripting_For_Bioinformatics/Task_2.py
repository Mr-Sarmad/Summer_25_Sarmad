import sys


def gc(seq):
    content = seq.count('G') + seq.count('C')
    length = len(seq)
    percentage = ( content / length ) *100
    print("GC content is: ", int(percentage))
    return int(percentage)

    


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("invalid arguments")

    dna = sys.argv[1]
    gc(dna)