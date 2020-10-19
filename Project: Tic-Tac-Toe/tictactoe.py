def show(s):
    c = 0
    print("---------")
    for i in range(2, -1, -1):
        print('| ', end='')
        for j in range(3):
            print('{} '.format(ls[j][i]), end='')
            if(ls[j][i] != ' '):
                c += 1
        print('|')
    print("---------")
    x1, z1 = 0, 0
    if (s[0][0] == s[0][1] and s[0][1] == s[0][2]):
        if (s[0][0] == 'X'):
            x1 += 1
        elif(s[0][0] == 'O'):
            z1 += 1
    if (s[1][0] == s[1][1] and s[1][1] == s[1][2]):
        if (s[1][0] == 'X'):
            x1 += 1
        elif(s[1][0] == 'O'):
            z1 += 1
    if (s[2][0] == s[2][1] and s[2][1] == s[2][2]):
        if (s[2][0] == 'X'):
            x1 += 1
        elif(s[2][0] == 'O'):
            z1 += 1
    if (s[0][0] == s[1][0] and s[1][0] == s[2][0]):
        if (s[0][0] == 'X'):
            x1 += 1
        elif(s[0][0] == 'O'):
            z1 += 1
    if (s[0][1] == s[1][1] and s[1][1] == s[2][1]):
        if (s[0][1] == 'X'):
            x1 += 1
        elif(s[0][1] == 'O'):
            z1 += 1
    if (s[0][2] == s[1][2] and s[1][2] == s[2][2]):
        if (s[0][2] == 'X'):
            x1 += 1
        elif(s[0][2] == 'O'):
            z1 += 1
    if (s[0][0] == s[1][1] and s[1][1] == s[2][2]):
        if (s[0][0] == 'X'):
            x1 += 1
        elif(s[0][0] == 'O'):
            z1 += 1
    if (s[0][2] == s[1][1] and s[1][1] == s[2][0]):
        if (s[0][2] == 'X'):
            x1 += 1
        elif(s[0][2] == 'O'):
            z1 += 1
    if (x1):
        print('X wins')
        return True
    elif (z1):
        print('O wins')
        return True
    elif (c == 9):
        print('Draw')
        return True
    return False


# START
j = 2

ls = []
ls.append([])
ls.append([])
ls.append([])

for i in range(8, -1, -1):
    ls[j].append(' ')
    j -= 1
    if (i % 3 == 0):
        j = 2

show(ls)
cnt = 0

while True:
    s1 = str(input('Enter the coordinates: > '))
    if (not s1[0].isalpha()):
        if (int(s1[0]) > 3 or int(s1[2]) > 3):
            print('Coordinates should be from 1 to 3!')
        else:
            p = int(s1[0]) - 1
            q = int(s1[2]) - 1
            if (ls[p][q] == ' '):
                if cnt % 2:
                    ls[p][q] = 'O'
                else:
                    ls[p][q] = 'X'
                if(show(ls)):
                    break
                cnt += 1
            else:
                print('This cell is occupied! Choose another one!')
    else:
        print('You should enter numbers!')
