from textwrap import wrap
class dec:
    def decrpt(self):
        with open('UserCustomDec.ini', 'r') as f:
            text = f.read()
            word = text.split()
        dcode = []
        for ts in word:
            splt = []
            dec = wrap(ts, 2)
            for i in dec:
                de = i.replace("48", "1").replace("4B", "2").replace("4A", "3").replace("4D", "4").replace("4C",
                                                                                                           "5").replace(
                    "4F", "6").replace("4E", "7").replace("41", "8").replace("40", "9").replace("49", "0").replace("38",
                                                                                                                   "A").replace(
                    "3B", "B").replace("3A", "C").replace("3D", "D").replace("3C", "E").replace("3F", "F").replace("3E",
                                                                                                                   "G").replace(
                    "31", "H").replace("30", "I").replace("33", "J").replace("32", "K").replace("35", "L").replace("34",
                                                                                                                   "M").replace(
                    "37", "N").replace("36", "O").replace("29", "P").replace("28", "Q").replace("2B", "R").replace("2A",
                                                                                                                   "S").replace(
                    "2D", "T").replace("2C", "U").replace("2F", "V").replace("2E", "W").replace("21", "X").replace("20",
                                                                                                                   "Y").replace(
                    "23", "Z").replace("18", "a").replace("1B", "b").replace("1A", "c").replace("1D", "d").replace("1C",
                                                                                                                   "e").replace(
                    "1F", "f").replace("1E", "g").replace("11", "h").replace("10", "i").replace("13", "j").replace("12",
                                                                                                                   "k").replace(
                    "15", "l").replace("14", "m").replace("17", "n").replace("16", "o").replace("09", "p").replace("08",
                                                                                                                   "q").replace(
                    "0B", "r").replace("0A", "s").replace("0D", "t").replace("0C", "u").replace("0F", "v").replace("0E",
                                                                                                                   "w").replace(
                    "01", "x").replace("00", "y").replace("23", "z").replace("44", "=").replace("57", ".")
                splt.append(de)
            sd = "".join(splt)
            dcode.append(sd)

        with open('UserCustomDec.ini', 'w') as t:
            for i in dcode:
                t.write(i + str("\n"))
            t.close()

Dec=dec()