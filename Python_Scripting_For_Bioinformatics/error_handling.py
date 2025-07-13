import sys
def parse(file):
    seq=file
    try:
        with open(seq,'r') as f:
            lines=f.readlines()
            header=lines[0].strip()
            print(header)
            seq=''
            for i in lines[1:]:
                seq+=i.strip()
            print(seq)
        return
    except FileNotFoundError:
        print("file not found")

if __name__=='__main__':
    if len(sys.argv)!=2:
        sys.exit("invalid argument")
    
    sequence=sys.argv[1]
    parse(sequence)