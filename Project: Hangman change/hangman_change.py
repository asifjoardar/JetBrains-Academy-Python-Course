import random
print("H A N G M A N")
while True:
    what = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if what == 'exit':
        break
    elif what == 'play':
        pass
    else:
        continue
    print("")
    l = ["python", "java", "kotlin", "javascript"]
    g = random.choice(l)
    s = '-' * len(g)
    t = 8
    nisi = str()
    az = "abcdefghijklmnopqrstuvwxyz"
    while t:
        print(s)
        ch = input("Input a letter: ")
        if ch in g and ch not in nisi and len(ch) == 1:
            p = list(s)
            for i in range(0,len(g)):
                if g[i] == ch:
                    p[i] = ch
            s = "".join(p)
        else:
            if len(ch) != 1:
                print("You should input a single letter")
            elif ch in nisi:
                print("You already typed this letter")
            elif ch not in az:
                print("It is not an ASCII lowercase letter")
            else:
                print("No such letter in the word")
                t -= 1
        if len(ch) == 1:
            nisi += ch
        if s == g:
            print("You guessed the word! {}".format(s))
            print("You survived!")
            break
        if not t:
            print("You are hanged!")
            break
        print("")
