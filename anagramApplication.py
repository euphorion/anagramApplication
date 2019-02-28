from sys import argv
from time import time
import codecs

def main():
    start_time = time()
    charToPrimes = {
        'a': 2,
        'b': 3,
        'c': 5,
        'd': 7,
        'e': 11,
        'f': 13,
        'g': 17,
        'h': 19,
        'i': 23,
        'j': 29,
        'k': 31,
        'l': 37,
        'm': 41,
        'n': 43,
        'o': 47,
        'p': 53,
        'q': 59,
        'r': 61,
        's': 67,
        't': 71,
        'u': 73,
        'v': 79,
        'w': 83,
        'x': 89,
        'y': 97,
        'z': 101,
        'ä': 103,
        'õ': 107,
        'ö': 109,
        'ü': 113,
        'ð': 127,
        'š': 131,
        'ž': 137,
        ' ': 139,
        '-': 149,
        'þ': 151,
        '\'': 157,
        '!': 163,
        'é': 167}
    if len(argv) < 3:
        print("Bad arguments list")
        exit()
    with codecs.open(argv[1], "r",encoding='iso8859-1') as f:
        lines = f.read().splitlines()
        table = dict()
        lookupword = " ".join(argv[2:])
        for word in lines:
            if len(lookupword) == len(word):
                key = 1
                for sym in word.lower():
                    key *= charToPrimes[sym]
                if key not in table:
                    table[key] = [word]
                else:
                    table[key].append(word)
        key = 1
        result = ""
        for sym in lookupword.lower():
            key *= charToPrimes[sym]
        if key in table:
            result = ",".join(table[key])
            print("%s,%s" % ((time() - start_time)*1000, result))
        else:
            print("%s" % (time() - start_time)*1000)
    
if __name__ == "__main__":
    main()
