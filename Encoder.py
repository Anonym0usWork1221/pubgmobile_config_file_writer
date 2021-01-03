from textwrap import wrap
class enc:
    def encod(self):
        with open('UserCustomDec.ini', 'r') as f:
            text = f.read()
            word = text.split()
        ecode = []
        for ls in word:
            relt = []
            enc = wrap(ls, 1)
            for i in enc:
                en = i.replace("1", "48").replace("2", "4B").replace("3", "4A").replace("4", "4D").replace("5", "4C").replace(
                    "6", "4F").replace("7", "4E").replace("8", "41").replace("9", "40").replace("0", "49").replace("A",
                                                                                                                   "38").replace(
                    "B", "3B").replace("C", "3A").replace("D", "3D").replace("E", "3C").replace("F", "3F").replace("G",
                                                                                                                   "3E").replace(
                    "H", "31").replace("I", "30").replace("J", "33").replace("K", "32").replace("L", "35").replace("M",
                                                                                                                   "34").replace(
                    "N", "37").replace("O", "36").replace("P", "29").replace("Q", "28").replace("R", "2B").replace("S",
                                                                                                                   "2A").replace(
                    "T", "2D").replace("U", "2C").replace("V", "2F").replace("W", "2E").replace("X", "21").replace("Y",
                                                                                                                   "20").replace(
                    "Z", "23").replace("a", "18").replace("b", "1B").replace("c", "1A").replace("d", "1D").replace("e",
                                                                                                                   "1C").replace(
                    "f", "1F").replace("g", "1E").replace("h", "11").replace("i", "10").replace("j", "13").replace("k",
                                                                                                                   "12").replace(
                    "l", "15").replace("m", "14").replace("n", "17").replace("o", "16").replace("p", "09").replace("q",
                                                                                                                   "08").replace(
                    "r", "0B").replace("s", "0A").replace("t", "0D").replace("u", "0C").replace("v", "0F").replace("w",
                                                                                                                   "0E").replace(
                    "x", "01").replace("y", "00").replace("z", "23").replace("=", "44").replace(".", "57")

                relt.append(en)
            ds = "".join(relt)
            ecode.append(ds)
        coun = 1
        with open('UserCustom.ini', 'w') as t:
            for i in ecode:
                if coun == 1:
                    t.write("[UserCustom DeviceProfile]\n")
                if coun == 35:
                    t.write("\n[BackUp DeviceProfile]\n")
                t.write("+CVars=" + str(i) + str("\n"))
                coun += 1
            t.write("\n\n")
            t.close()
Enc=enc()