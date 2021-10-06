n = int(input())
l = int(input())
letter1 = ""
letter2 = ""
password = ""
for sign1 in range(1, n+1):
    for sign2 in range(1, n+1):
        for sign3 in range(1, l+1):
            for sign4 in range(1, l+1):
                for sign5 in range(1, n+1):
                    if sign5 > sign1 and sign5 > sign2:
                        if sign3 == 1:
                            letter1 = "a"
                        if sign3 == 2:
                            letter1 = "b"
                        if sign3 == 3:
                            letter1 = "c"
                        if sign3 == 4:
                            letter1 = "d"
                        if sign3 == 5:
                            letter1 = "e"
                        if sign3 == 6:
                            letter1 = "f"
                        if sign3 == 7:
                            letter1 = "g"
                        if sign3 == 8:
                            letter1 = "h"
                        if sign3 == 9:
                            letter1 = "i"
                        if sign3 == 10:
                            letter1 = "j"
                        if sign3 == 11:
                            letter1 = "k"
                        if sign3 == 12:
                            letter1 = "l"
                        if sign3 == 13:
                            letter1 = "m"
                        if sign3 == 14:
                            letter1 = "n"
                        if sign3 == 15:
                            letter1 = "o"
                        if sign3 == 16:
                            letter1 = "p"
                        if sign3 == 17:
                            letter1 = "q"
                        if sign3 == 18:
                            letter1 = "r"
                        if sign3 == 19:
                            letter1 = "s"
                        if sign3 == 20:
                            letter1 = "t"
                        if sign3 == 21:
                            letter1 = "u"
                        if sign3 == 22:
                            letter1 = "v"
                        if sign3 == 23:
                            letter1 = "w"
                        if sign3 == 24:
                            letter1 = "x"
                        if sign3 == 25:
                            letter1 = "y"
                        if sign3 == 26:
                            letter1 = "z"
                        if sign4 == 1:
                            letter2 = "a"
                        if sign4 == 2:
                            letter2 = "b"
                        if sign4 == 3:
                            letter2 = "c"
                        if sign4 == 4:
                            letter2 = "d"
                        if sign4 == 5:
                            letter2 = "e"
                        if sign4 == 6:
                            letter2 = "f"
                        if sign4 == 7:
                            letter2 = "g"
                        if sign4 == 8:
                            letter2 = "h"
                        if sign4 == 9:
                            letter2 = "i"
                        if sign4 == 10:
                            letter2 = "j"
                        if sign4 == 11:
                            letter2 = "k"
                        if sign4 == 12:
                            letter2 = "l"
                        if sign4 == 13:
                            letter2 = "m"
                        if sign4 == 14:
                            letter2 = "n"
                        if sign4 == 15:
                            letter2 = "o"
                        if sign4 == 16:
                            letter2 = "p"
                        if sign4 == 17:
                            letter2 = "q"
                        if sign4 == 18:
                            letter2 = "r"
                        if sign4 == 19:
                            letter2 = "s"
                        if sign4 == 20:
                            letter2 = "t"
                        if sign4 == 21:
                            letter2 = "u"
                        if sign4 == 22:
                            letter2 = "v"
                        if sign4 == 23:
                            letter2 = "w"
                        if sign4 == 24:
                            letter2 = "x"
                        if sign4 == 25:
                            letter2 = "y"
                        if sign4 == 26:
                            letter2 = "z"
                        password =str(sign1)+str(sign2)+letter1+letter2+str(sign5)
                        print(password, end=" ")