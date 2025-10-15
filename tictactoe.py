def p1moves():
    print("It's Player1's turn.")
    s = int(input("What is Player1's move?(1-9) "))
    flag = False
    while flag == False:
        if 1 <= s <= 3:
            if r1[s - 1] != '-':
                s = int(input('Player1 has already done this move. Make another move.(1-9) '))
            else:
                flag = True
                r1[s - 1] = 'x'
                print(r1, r2, r3, sep= '\n')
                break
        if 4 <= s <= 6:
            if r2[s - 4] != '-':
                s = int(input('Player1 has already done this move. Make another move.(1-9) '))
            else:
                flag = True
                r2[s - 4] = 'x'
                print(r1, r2, r3, sep= '\n')
                break
        if 7 <= s <= 9:
            if r3[s - 7] != '-':
                s = int(input('Player1 has already done this move. Make another move.(1-9) '))
            else:
                flag = True
                r3[s - 7] = 'x'
                print(r1, r2, r3, sep= '\n')
                break
def p2moves():
    print("It's Player2's turn.")
    s = int(input("What is Player2's move?(1-9) "))
    flag = False
    while flag == False:
        if 1 <= s <= 3:
            if r1[s - 1] != '-':
                s = int(input('Player2 has already done this move. Make another move.(1-9) '))
            else:
                flag = True
                r1[s - 1] = 'o'
                print(r1, r2, r3, sep= '\n')
                break
        if 4 <= s <= 6:
            if r2[s - 4] != '-':
                s = int(input('Player2 has already done this move. Make another move.(1-9) '))
            else:
                flag = True
                r2[s - 4] = 'o'
                print(r1, r2, r3, sep= '\n')
                break
        if 7 <= s <= 9:
            if r3[s - 7] != '-':
                s = int(input('Player2 has already done this move. Make another move.(1-9) '))
            else:
                flag = True
                r3[s - 7] = 'o'
                print(r1, r2, r3, sep= '\n')
                break
def p1win():
    if r1 == ['x', 'x', 'x'] or r2 == ['x', 'x', 'x'] or r3 == ['x', 'x', 'x']:
        print('Player1 won!')
        flag2 = True
        return True
    elif (r1[0] == 'x' and r2[0] == 'x' and r3[0] == 'x') or (r1[1] == 'x' and r2[1] == 'x' and r3[1] == 'x') or (r1[2] == 'x' and r2[2] == 'x' and r3[2] == 'x'):
        print('Player1 won!')
        flag2 = True
        return True
    elif (r1[0] == 'x' and r2[1] == 'x' and r3[2] == 'x') or (r1[2] == 'x' and r2[1] == 'x' and r3[0] == 'x'):
        print('Player1 won!')
        flag2 = True
        return True 

def p2win():
    if r1 == ['o', 'o', 'o'] or r2 == ['o', 'o', 'o'] or r3 == ['o', 'o', 'o']:
        print('Player2 won!')
        f = True
        return True
    elif (r1[0] == 'o' and r2[0] == 'o' and r3[0] == 'o') or (r1[1] == 'o' and r2[1] == 'o' and r3[1] == 'o') or (r1[2] == 'o' and r2[2] == 'o' and r3[2] == 'o'):
        print('Player2 won!')
        f = True
        return True
    elif (r1[0] == 'o' and r2[1] == 'o' and r3[2] == 'o') or (r1[2] == 'o' and r2[1] == 'o' and r3[0] == 'o'):
        print('Player2 won!')
        f = True
        return True

print("Hello, let's play TicTacToe! :)")
print("Player1 is 'x' and Player2 is 'o'")
r1 = ['-', '-', '-']
r2 = ['-', '-', '-']
r3 = ['-', '-', '-']

f = True
z = True
while f == True:
    if '-' in r1 or '-' in r2 or '-' in r3:
        p1moves()
    if p1win() == True:
        f = False
        z = False
        break
    if '-' in r1 or '-' in r2 or '-' in r3:
        p2moves()
    if p2win() == True:
        f = False
        z = False
        break
    if '-' not in r1 and '-' not in r2 and '-' not in r3:
        print("No one wins. Womp womp..")
        break


