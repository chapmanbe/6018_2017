import re
import argparse

testString = """Brian has a nephew named Ben. Br. Chapman died yesterday. Brian Chapman Brian E. Chapman Brian Earl Chapman Wendy Webber Chapman Clare 1234 4321.1234
python python.org http://python.org www.python.org jython zython Brad Bob cpython brian http://www.python.org perl Perl PERL"""

def read_fasta(fname):
    seqs = {}
    with open("sequence.fasta") as f0:
        for line in f0:
            if line[0] == ">":
                try:
                    seqs[key] = seq
                except NameError:
                    pass
                key = line[1:].strip()
                seq = ""
            elif line[0] in set("ACTG"):
                seq += line.strip()
        seqs[key] = seq
    return seqs

def ex1(txt):
    rex1 = re.compile(r"""\w*ython""")
    return rex1.findall(txt)
def ex2(txt):
    rEx2 = re.compile(r"""Brian""",re.I)
    return rEx2.findall(txt)

def ex3(txt):
    rEx3 = re.compile(r"""jython|python""",re.I)
    return rEx3.findall(txt)

def ex4(txt):
    rEx4 = re.compile(r"""B[a-z]*""") 
    return rEx4.findall(txt)

def ex5(fname):
    seq = read_fasta("sequence.fasta")["exercise5"]
    rEx5 = re.compile(r"""C[ACTG]{1,3}?C""")
    return rEx5.findall(seq)




def main():
    parser = argparse.ArgumentParser(description='run regex examples')
    parser.add_argument('--ex_1', action='store_true')
    parser.add_argument('--ex_2', action='store_true')
    parser.add_argument('--ex_3', action='store_true')
    parser.add_argument('--ex_4', action='store_true')
    parser.add_argument('--ex_5', action='store_true')
    args = parser.parse_args()
    if args.ex_1:
        print(ex1(testString))
    if args.ex_2:
        print(ex2(testString))
    if args.ex_3:
        print(ex3(testString))
    if args.ex_4:
        print(ex4(testString))
    if args.ex_5:
        print(ex5(testString))

if __name__ == '__main__':
    main()
