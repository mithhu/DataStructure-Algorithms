"""
ID: mithhu61
LANG: PYTHON3
PROG: ride
"""

fin = open("ride.in", "r")
fout = open('ride.out', 'w')


def modCalc(string):
    prod = 1
    for char in string:
        if char == "\n":
            prod *= 1
        else:
            prod *= (ord(char) - 64)
    rem = prod % 47
    return rem


comet = modCalc(fin.readline())
group = modCalc(fin.readline())


if comet == group:
    fout.write("GO" + "\n")
else:
    fout.write("STAY" + "\n")
fout.close()
