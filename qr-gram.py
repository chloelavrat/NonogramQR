#----------------------------------------------------------
# Name: QR-Gram
# Autor: azerty-waves
# Site: azerty-waves.github.io
# Comments: 
# from the previous work of the redditor 
# r/TheBlackCat13/
#----------------------------------------------------------
from itertools import zip_longest
import pyqrcode, argparse


def get_qrcode(string):
    qr = pyqrcode.create(string)
    bin = qr.text(quiet_zone=0)
    bin = bin.replace('1' , '*')
    bin = bin.replace('0' , ' ')
    return bin[:-1]

def print_qrcode(string):
    qr = pyqrcode.create(string)
    print(qr.terminal(quiet_zone=1))
    pass

def get_counts(pic):
    """Gets the counts of the items in the rows and columns.

    `pic` is a multi-line string, where each line is a row."""
    rows = pic.split('\n')
    cols = (''.join(x) for x in zip_longest(*rows, fillvalue=' '))
    count = lambda lines: [[str(len(y)) for y in x.split()] for x in lines]
    return count(cols), count(rows)

def format_count(counts):
    """Get the right number of elements for each count."""
    maxnum = max(len(x) for x in counts)
    maxlet = max(max(len(y) for y in x) for x in counts)
    counts = ([y.rjust(maxlet) for y in x] for x in counts)

    maxspc = ' '*maxlet
    return [[maxspc]*(maxnum-len(x)) + x for x in counts]

def print_counts(pic):
    """Print the results in the format requested by the question."""
    colcounts, rowcounts = get_counts(pic)

    colcounts = format_count(colcounts)
    rowcounts = format_count(rowcounts)

    rowcounts = [' '.join(x) for x in rowcounts]

    colpad = ' '*(len(rowcounts[0])+1)
    colcounts = (' '.join(x) for x in zip(*colcounts))
    colcounts = (colpad+x for x in colcounts)

    print(*colcounts, sep='\n')
    print(*rowcounts, sep='\n')

def export_csv(pic, filename):
    """Export the result into CSV"""

    f= open(filename+".csv","w+")
    colcounts, rowcounts = get_counts(pic)

    mod = len(colcounts)+len(rowcounts)
    colcounts = format_count(colcounts)
    rowcounts = format_count(rowcounts)

    rowcounts = [';'.join(x) for x in rowcounts]

    colpad = ';'*(len(rowcounts[0])+1)
    colcounts = (';'.join(x) for x in zip(*colcounts))
    colcounts = (colpad+x for x in colcounts)

    for c in colcounts:
        f.write(c+";")
        f.write('\n')
    for r in rowcounts:
        f.write(r+";")
        f.write('\n')
    f.close()

#######################################################

if __name__ == "__main__":
    ## arguments parser 
    parser=argparse.ArgumentParser(
        description='''This script change a string into a QR-Code and then convert it into a nonogram.''',
        epilog="""have fun :)""")
    parser.add_argument('message', nargs='*', default="https://github.com/azerty-waves", help='put the message to encode here')
    args=parser.parse_args()

    ## encode into a nonogram
    print(">>> String to encode: "+args.message)
    string = args.message
    pic_2 = get_qrcode(string)
    print_qrcode(string)
    print_counts(pic_2)
    export_csv(pic_2,"my-nono")
