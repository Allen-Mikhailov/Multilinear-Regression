def dice(string: str):
    rows = []
    rs = string.split("\n")
    for i in range(len(rs)):
        rows.append(rs[i].split(","))

    return rows

def opencsv(filename):
    return dice(open(filename).read())

def getHeaders(rows):
    return rows[0]

def getHeaderIndex(Header, Headers):
    for i in range(len(Headers)):
        if Headers[i] == Header:
            return i
    return 0

def getCollum(diced, collum):
    if type(collum) == str:
        collum = getHeaderIndex(collum, getHeaders(diced))
    
    collumdata = []
    for i in range(len(diced[0])-1):
        collumdata.append(diced[i+1][collum])
    return collumdata