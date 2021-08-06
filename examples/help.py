import re, sys, time, random
# import arctan
# from . import pyntegrate.arctan as arctan
import pyntegrate.arctan as arctan

class help:
    def __init__(self):
        self.arr = []
        self.padding = 28

    def add(self, minSymbol="", fullSymbol="", inputSymbol="", message=""):
        self.arr.append({"minSymbol":minSymbol, "fullSymbol":fullSymbol, "inputSymbol":inputSymbol, "message":message})

    def parsing(self, minSymbol=None, fullSymbol=None, inputSymbol=None, message=None):
        if (minSymbol == None and fullSymbol == None) or message == None:
            print('error')
            return

        if minSymbol == None and fullSymbol != None:
            string = ('    ' + fullSymbol).ljust(self.padding, ' ') + message
            if inputSymbol != None:
                string = ('    ' + fullSymbol).ljust(self.padding, ' ') + ' ' + inputSymbol + ' '  + message
            return string

        if minSymbol != None and fullSymbol == None:
            string = (' ' + minSymbol + ' ').ljust(self.padding, ' ')
            if inputSymbol != None:
                string = ((' ' + minSymbol + ' ').ljust(self.padding-(2*len(inputSymbol)), ' ') + ' ' + inputSymbol).ljust(self.padding, ' ')
            string = string + message
            return string

        a = ' ' + minSymbol + ' ' + fullSymbol
        if inputSymbol != None:
            a = (' ' + minSymbol + ', ' + fullSymbol).ljust(self.padding-(2*len(inputSymbol)), ' ') + ' ' + inputSymbol
        if len(a) >= self.padding:
            self.padding = len(a) + 5

        if minSymbol != None and fullSymbol != None:
            string = (' ' + minSymbol + ', ' + fullSymbol).ljust(self.padding, ' ')
            if inputSymbol != None:
                string = ((' ' + minSymbol + ' ' + fullSymbol).ljust(self.padding-(2*len(inputSymbol)), ' ') + ' ' + inputSymbol).ljust(self.padding, ' ')
            string = string + message
            return string

    def __str__(self):
        out = ""
        for line in self.arr:
            self.parsing(line["minSymbol"], line["fullSymbol"], line["inputSymbol"], line["message"])
        for i in range(len(self.arr)):
            line = self.arr[i]
            out += self.parsing(line["minSymbol"], line["fullSymbol"], line["inputSymbol"], line["message"]) + "\n"
            if i > 0 and (self.arr[i]["minSymbol"].split("=")[0] != self.arr[i-1]["minSymbol"].split("=")[0]) and (self.arr[i]["minSymbol"].split("=")[0][-1] == "P" and self.arr[i-1]["minSymbol"].split("=")[0][-1] == "C"):
                out += "\n"
        return ' ' + out.strip()

def getN(string):
    if '=' in string:
        tmp = string.split('=')[1]
        if re.search("^[0-9]+$", tmp):
            return int(tmp)

def printSortTime(sort, n, lang, time):
    if n < 1000 and len(sort)+len(lang) <= 11:
        print("%s on %s elements (%s):\t\t %0.5f seconds" % (sort, '{:,}'.format(n), lang, time))
    elif n < 100 and len(sort)+len(lang) <= 12:
        print("%s on %s elements (%s):\t\t %0.5f seconds" % (sort, '{:,}'.format(n), lang, time))
    else:
        print("%s on %s elements (%s):\t %0.5f seconds" % (sort, '{:,}'.format(n), lang, time))

def isSorted(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

def printHeading(s, t):
    print('%s: %s\n' % (s, '{:,}'.format(t)))

def printSorted(a=None, b=None):
    if a != None: print('`a` is sorted' if isSorted(a) else '`a` is not sorted')
    if b != None: print('`b` is sorted' if isSorted(b) else '`b` is not sorted')

def printTime(t):
    print("C is", round(t, 3), "times faster than Python")

def printTime2(s, t, m="\t"):
    print("%s:%s%0.5f seconds" % (s, m, t))

def printTime3(s, t):
    print("%s:\t%0.6f seconds" % (s, t))

def makeArrLin(n):
    return [i*i for i in range(n)]

def makeArrMin(n, seed=25):
    #random.seed(seed)
    #return [random.randint(0, n*n) for i in range(n)]
    return arctan.makeArrMin(n)

def makeArr(n, seed=25):
    return makeArrMin(n, seed), makeArrMin(n, seed)

def printArr(arr, n=5):
    for i in range(len(arr)):
        val = str(arr[i]).rjust(6, ' ')
        if (i+1) % n == 0 or i == len(arr)-1:
            print(val)
        else:
            print(val, end=" ")
