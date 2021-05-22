#The item code for the item to be fetched
itemcode = "HYPERSHIP"


mdict = {}
mnat = open("library/nats.txt")
mnats = mnat.readlines()

def lmat(mtag, man):
    file = open("library/prunmat/"+mtag.strip()+".txt")
    content = file.readlines()
    mats = int(content[1])
    for i in range(mats):
        x = (i*2+2)
        y = content[x]
        co = float(content[x+1])
        num = co*man
        if y in mdict:
            mdict[y] += num
        else:
            mdict[y] = num
        lmat(y, num)

def graphing(tags):
    lmat (tags, 1)
    fnat = open("library/matlistnat.txt", "w")
    f = open("library/matlist.txt", "w")
    for m, b in mdict.items():
        mlist = str(m.strip() + " = " + str(round(b, 3)))
        if m in mnats:
            fnat.write(mlist + "\n")
            print (mlist)
        f.write(mlist + "\n")


graphing(itemcode)
