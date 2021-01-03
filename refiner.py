import sys
def RF():
    try:
        with open('UserCustom.ini', 'r') as f:
            text = f.read()
            word = text.split()
            ss=[]
            for e in word:
                if "+CVars=" in e:
                    ss.append(e)
                else:
                    pass
            pure=[]
            for t in ss:
                vv =t.replace("+CVars=", "")
                pure.append(vv)
        with open('UserCustomDec.ini','w') as t:
            for i in pure:
                t.write(i + str("\n"))
            t.close()

    except:
        print("[King] Don't found file in current directory.")
        sys.exit(1)
