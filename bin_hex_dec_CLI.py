import argparse, sys
from ast import Store
import pandas as pd

"""
Exercise
Write a simple CLI that converts numbers and strings between binary, ascii etc. Add pytests as well to test the input and output.
Examples

Ex 1

python3 format-converter.py 'hello world' --ascii_sum 

-> 1116
"""
hex_dic = {
    "A": "10",
    "B": "11",
    "C": "12",
    "D": "13",
    "E": "14",
    "F": "15",
}


parser = argparse.ArgumentParser()
parser.add_argument("-as", "--ascii_sum")
parser.add_argument("-a", "--ascii")
parser.add_argument("-de", "--dec")
parser.add_argument("-b", "--bin", type=int)
args = parser.parse_args()

if args.ascii_sum:
    print(sum([ord(i) for i in args.ascii_sum]))
if args.ascii:
    print([ord(i) for i in args.ascii])
if args.dec:
    print(sum([(int(i) * (2**pos)) for pos, i in enumerate(args.dec[::-1])]))
if args.bin:
    num_bin = []
    while args.bin > 0:
        num_bin.append(str(0 if (args.bin % 2) == 0 else 1))
        args.bin = args.bin // 2
    print("0b" + "".join(num_bin[::-1]))


"""
input 
    python3 bin_hex_dec.py -as 'hello world' 
    python3 bin_hex_dec.py -de "00100111"  
    python3 bin_hex_dec.py -b 45  
"""
