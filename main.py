import sys

class convertor:
    def __init__(self):
        self.string = ''
        self.binList = []
        self.hexList = []

    def toBin(self):
        for x in self.string:
            self.binList.append(bin(ord(x))[2:len(bin(ord(x)))])

        return self.binList

    def toHex(self):
        for x in self.binList:
            h = str(hex(int(x, 2)))
            self.hexList.append(h.replace('0x',''))

        return self.hexList


def main():
    strings = ['acorn', 'xbox', 'amiga']
    myConv = convertor()

    for i in strings:
        myConv.string = i
        x = myConv.toBin()
        y = myConv.toHex()
        print(myConv.string)

        for b in x: sys.stdout.write(f'{b} ')
        sys.stdout.write('\n')

        for h in y: sys.stdout.write(f'{h} ')
        sys.stdout.write('\n\n')

        myConv.binList = []
        myConv.hexList = []

if __name__ == '__main__':
    main()
